# Performance Tuning Quick Reference

## Common Performance Issues & Fixes

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Slow reads | Small files | `OPTIMIZE` table |
| Slow filters | No ZORDER/clustering | Add ZORDER on filter columns |
| Join timeouts | Large shuffle | Use broadcast for small tables |
| OOM errors | Data skew | Salting or AQE skew join |
| Slow writes | Too many partitions | Reduce partition count |
| High storage | No VACUUM | Schedule regular VACUUM |

## File Size Targets
- Target file size: 128 MB - 1 GB
- Use `DESCRIBE DETAIL` to check current sizes
- `OPTIMIZE` compacts files to target size

## ZORDER Column Selection
1. Columns frequently used in WHERE/JOIN
2. High cardinality columns (IDs, dates)
3. Maximum 4 ZORDER columns (diminishing returns)
4. Order by selectivity (most selective first)

## AQE (Adaptive Query Execution) Settings
```
spark.sql.adaptive.enabled = true
spark.sql.adaptive.coalescePartitions.enabled = true
spark.sql.adaptive.skewJoin.enabled = true
spark.sql.adaptive.localShuffleReader.enabled = true
```

## Photon Checklist
- [x] Use Photon-enabled runtime
- [x] Use Delta format (not Parquet directly)
- [x] Avoid UDFs where possible (use built-in functions)
- [x] Use SQL or DataFrame API (not RDD)

## Monitoring Queries
```sql
-- Top slow queries
SELECT statement_id, total_duration_ms, rows_produced
FROM system.query.history
WHERE start_time >= current_date() - INTERVAL 1 DAY
ORDER BY total_duration_ms DESC
LIMIT 10;

-- Table sizes
SELECT table_catalog, table_schema, table_name,
       data_source_format, total_size
FROM system.information_schema.tables
WHERE total_size IS NOT NULL
ORDER BY total_size DESC;
```
