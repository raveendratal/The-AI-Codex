---
name: cost-optimization
description: Optimize Databricks costs through cluster sizing, query tuning, storage optimization, and serverless strategies.
---

# Cost Optimization Skill

## When to Use
Use to reduce compute and storage costs across your Lakehouse.

## Key Areas

### 1. Cluster Right-Sizing
```python
# Check cluster utilization
metrics = spark.sql("""
  SELECT
    cluster_id,
    AVG(cpu_utilization) AS avg_cpu,
    AVG(memory_utilization) AS avg_mem,
    COUNT(*) AS total_jobs
  FROM system.compute.cluster_metrics
  WHERE timestamp >= current_date() - INTERVAL 7 DAY
  GROUP BY cluster_id
""")
```

### 2. Query Optimization
```sql
-- Find expensive queries
SELECT
  statement_id,
  executed_by,
  total_duration_ms,
  rows_produced,
  statement_text
FROM system.query.history
WHERE start_time >= current_date() - INTERVAL 7 DAY
ORDER BY total_duration_ms DESC
LIMIT 20;
```

### 3. Storage Optimization
```sql
-- Clean up old files
VACUUM catalog.schema.table RETAIN 168 HOURS;

-- Optimize file sizes
OPTIMIZE catalog.schema.table
  WHERE date >= current_date() - INTERVAL 30 DAY
  ZORDER BY (user_id);

-- Analyze table stats
ANALYZE TABLE catalog.schema.table COMPUTE STATISTICS FOR ALL COLUMNS;
```

### 4. Serverless Migration
- Move interactive workloads to Serverless SQL Warehouses
- Use `availableNow` trigger for streaming cost savings
- Leverage Photon for query acceleration

## Cost Monitoring
```sql
SELECT
  workspace_id,
  sku_name,
  usage_date,
  SUM(usage_quantity) AS total_dbus
FROM system.billing.usage
WHERE usage_date >= current_date() - INTERVAL 30 DAY
GROUP BY ALL
ORDER BY total_dbus DESC;
```

## Best Practices
- Use auto-scaling clusters with appropriate min/max
- Enable Spot instances for non-critical workloads
- Schedule jobs during off-peak hours
- Use result caching on SQL warehouses
- Partition large tables by date
