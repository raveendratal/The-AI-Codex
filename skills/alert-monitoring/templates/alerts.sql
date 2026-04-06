-- =============================================================
-- Alert Query Templates
-- =============================================================

-- ALERT 1: Data Freshness
-- Trigger: When status = 'STALE'
SELECT
  '${table_name}' AS monitored_table,
  MAX(${timestamp_column}) AS last_update,
  TIMESTAMPDIFF(HOUR, MAX(${timestamp_column}), current_timestamp()) AS hours_since_update,
  CASE
    WHEN MAX(${timestamp_column}) < current_timestamp() - INTERVAL ${max_staleness_hours} HOUR
    THEN 'STALE' ELSE 'FRESH'
  END AS status
FROM ${catalog}.${schema}.${table_name};

-- ALERT 2: Null Spike Detection
-- Trigger: When null_pct > threshold
SELECT
  '${column_name}' AS monitored_column,
  COUNT(*) AS total_rows,
  SUM(CASE WHEN ${column_name} IS NULL THEN 1 ELSE 0 END) AS null_count,
  ROUND(SUM(CASE WHEN ${column_name} IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS null_pct,
  CASE
    WHEN SUM(CASE WHEN ${column_name} IS NULL THEN 1 ELSE 0 END) * 100.0 / COUNT(*) > ${null_threshold_pct}
    THEN 'ALERT' ELSE 'OK'
  END AS status
FROM ${catalog}.${schema}.${table_name};

-- ALERT 3: Volume Anomaly (Z-score based)
-- Trigger: When status = 'ANOMALY'
WITH daily_counts AS (
  SELECT DATE(${timestamp_column}) AS dt, COUNT(*) AS row_count
  FROM ${catalog}.${schema}.${table_name}
  WHERE ${timestamp_column} >= current_date() - INTERVAL 30 DAY
  GROUP BY DATE(${timestamp_column})
),
stats AS (
  SELECT AVG(row_count) AS avg_count, STDDEV(row_count) AS std_count
  FROM daily_counts WHERE dt < current_date()
)
SELECT
  d.dt, d.row_count, s.avg_count, s.std_count,
  ROUND((d.row_count - s.avg_count) / NULLIF(s.std_count, 0), 2) AS z_score,
  CASE WHEN ABS((d.row_count - s.avg_count) / NULLIF(s.std_count, 0)) > 2
    THEN 'ANOMALY' ELSE 'NORMAL'
  END AS status
FROM daily_counts d, stats s
WHERE d.dt = current_date();
