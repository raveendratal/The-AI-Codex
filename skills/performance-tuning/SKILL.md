---
name: performance-tuning
description: Optimize Spark and Delta Lake performance through partitioning, caching, join strategies, and query tuning.
---

# Performance Tuning Skill

## When to Use
Use when queries are slow, jobs timeout, or storage costs are high.

## Delta Lake Optimization

### OPTIMIZE + ZORDER
```sql
-- Compact small files and co-locate data
OPTIMIZE main.gold.sales
  ZORDER BY (customer_id, date);

-- Incremental optimize (only recent partitions)
OPTIMIZE main.gold.sales
  WHERE date >= current_date() - INTERVAL 7 DAY;
```

### Liquid Clustering (Recommended for new tables)
```sql
-- Create table with liquid clustering
CREATE TABLE main.gold.events
  CLUSTER BY (event_date, user_id)
  AS SELECT * FROM main.silver.events;

-- Trigger clustering
OPTIMIZE main.gold.events;
```

### Statistics
```sql
ANALYZE TABLE main.gold.sales COMPUTE STATISTICS FOR ALL COLUMNS;
```

## Partitioning Strategy
```sql
-- Partition by date for time-series data
CREATE TABLE main.gold.events (
  event_id STRING, event_date DATE, payload STRING
) USING DELTA
PARTITIONED BY (event_date);
```

**Rules of thumb:**
- Partition when table > 1 TB
- Each partition should have > 1 GB of data
- Max 10,000 partitions
- Use date columns (not high-cardinality)

## Join Optimization
```python
# Broadcast small tables (< 100 MB)
from pyspark.sql.functions import broadcast
result = large_df.join(broadcast(small_df), "key")

# Check join strategy in explain plan
result.explain(True)
```

```sql
-- SQL broadcast hint
SELECT /*+ BROADCAST(dim) */
  f.*, dim.name
FROM main.gold.facts f
JOIN main.gold.dimensions dim ON f.dim_id = dim.id;
```

## Caching
```python
# Cache frequently accessed DataFrames
df.cache()
df.count()  # trigger cache materialization

# Unpersist when done
df.unpersist()
```

```sql
-- SQL caching
CACHE TABLE main.gold.dim_products;
UNCACHE TABLE main.gold.dim_products;
```

## Spark Configuration
```python
# Adaptive Query Execution (enabled by default)
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")

# Shuffle partitions (default 200, tune based on data size)
spark.conf.set("spark.sql.shuffle.partitions", "auto")
```

## Diagnostics
```sql
-- Check table file sizes
DESCRIBE DETAIL main.gold.sales;

-- Check table history
DESCRIBE HISTORY main.gold.sales;

-- Query profile
EXPLAIN EXTENDED SELECT * FROM main.gold.sales WHERE date = current_date();
```

## Best Practices
- Use Liquid Clustering over manual partitioning for new tables
- Run OPTIMIZE on a schedule (daily for active tables)
- Use ZORDER on frequently filtered columns
- Enable Photon for compute acceleration
- Avoid SELECT * — project only needed columns
- Filter early, aggregate late
