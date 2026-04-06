---
name: alert-monitoring
description: Set up SQL alerts, job health monitoring, pipeline observability, and custom alerting on Databricks.
---

# Alert & Monitoring Skill

## When to Use
Use for setting up proactive alerting on data quality, pipeline health, and business KPIs.

## SQL Alert Types

### 1. Data Freshness Alert
```sql
-- Alert if no new data in 24 hours
SELECT
  CASE WHEN MAX(updated_at) < current_timestamp() - INTERVAL 24 HOUR
    THEN 'STALE' ELSE 'FRESH'
  END AS status,
  MAX(updated_at) AS last_update
FROM main.gold.sales;
```

### 2. Row Count Anomaly
```sql
-- Alert if daily row count drops below threshold
SELECT
  COUNT(*) AS today_rows,
  CASE WHEN COUNT(*) < 1000 THEN 'ALERT' ELSE 'OK' END AS status
FROM main.gold.sales
WHERE date = current_date();
```

### 3. Business KPI Alert
```sql
-- Alert if revenue drops > 20% vs last week
WITH current_week AS (
  SELECT SUM(revenue) AS revenue FROM main.gold.sales
  WHERE date >= current_date() - INTERVAL 7 DAY
),
last_week AS (
  SELECT SUM(revenue) AS revenue FROM main.gold.sales
  WHERE date BETWEEN current_date() - INTERVAL 14 DAY AND current_date() - INTERVAL 7 DAY
)
SELECT
  c.revenue AS current_revenue,
  l.revenue AS previous_revenue,
  ROUND((c.revenue - l.revenue) / l.revenue * 100, 2) AS pct_change,
  CASE WHEN c.revenue < l.revenue * 0.8 THEN 'ALERT' ELSE 'OK' END AS status
FROM current_week c, last_week l;
```

## Job Health Monitoring
```sql
-- Check failed jobs in last 24 hours
SELECT
  job_id,
  run_id,
  result_state,
  start_time,
  end_time
FROM system.lakeflow.job_run_timeline
WHERE period_start_time >= current_date() - INTERVAL 1 DAY
  AND result_state = 'FAILED';
```

## Best Practices
- Set alerts with appropriate evaluation frequency (5-60 min)
- Use notification destinations (email, Slack, PagerDuty)
- Create severity levels (INFO, WARNING, CRITICAL)
- Monitor both technical and business metrics
