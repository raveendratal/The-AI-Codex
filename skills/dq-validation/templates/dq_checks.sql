-- =============================================================
-- Data Quality Checks Template
-- =============================================================

-- CHECK 1: Null Check on required columns
SELECT
  '${table_name}' AS table_name,
  '${column_name}' AS column_name,
  'null_check' AS check_type,
  COUNT(*) AS null_count,
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END AS status
FROM ${catalog}.${schema}.${table_name}
WHERE ${column_name} IS NULL;

-- CHECK 2: Duplicate Check on primary key
SELECT
  '${table_name}' AS table_name,
  '${primary_key}' AS column_name,
  'duplicate_check' AS check_type,
  COUNT(*) AS duplicate_count,
  CASE WHEN COUNT(*) = 0 THEN 'PASS' ELSE 'FAIL' END AS status
FROM (
  SELECT ${primary_key}, COUNT(*) cnt
  FROM ${catalog}.${schema}.${table_name}
  GROUP BY ${primary_key}
  HAVING COUNT(*) > 1
);

-- CHECK 3: Row Count Threshold
SELECT
  '${table_name}' AS table_name,
  'row_count' AS check_type,
  COUNT(*) AS total_rows,
  CASE WHEN COUNT(*) >= ${min_row_threshold} THEN 'PASS' ELSE 'FAIL' END AS status
FROM ${catalog}.${schema}.${table_name};

-- CHECK 4: Freshness Check
SELECT
  '${table_name}' AS table_name,
  'freshness_check' AS check_type,
  MAX(${timestamp_column}) AS latest_record,
  CASE
    WHEN MAX(${timestamp_column}) >= current_date() - INTERVAL ${max_staleness_days} DAY
    THEN 'PASS' ELSE 'FAIL'
  END AS status
FROM ${catalog}.${schema}.${table_name};
