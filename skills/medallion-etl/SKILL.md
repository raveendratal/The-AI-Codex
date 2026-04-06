---
name: medallion-etl
description: Build scalable Medallion (Bronze → Silver → Gold) pipelines using Delta Lake and Auto Loader.
---

# Medallion ETL Skill

## When to Use
Use for ingestion, transformation, and building layered data pipelines.

## Workflow
1. Ingest raw data into Bronze (Auto Loader / batch)
2. Clean and deduplicate in Silver
3. Aggregate into Gold
4. Validate data quality
5. Optimize performance (ZORDER, partitioning)

## Bronze (Streaming Example)
```python
df = spark.readStream.format("cloudFiles") \
  .option("cloudFiles.format", "json") \
  .load("/mnt/raw/orders")

df.writeStream.format("delta") \
  .option("checkpointLocation", "/chk/orders") \
  .start("/mnt/bronze/orders")
```

## Silver Transformation
```sql
CREATE OR REPLACE TABLE main.silver.orders AS
SELECT DISTINCT * FROM main.bronze.orders
WHERE order_id IS NOT NULL;
```

## Gold Aggregation
```sql
CREATE OR REPLACE TABLE main.gold.sales AS
SELECT customer_id, SUM(amount) total_sales
FROM main.silver.orders
GROUP BY customer_id;
```

## Best Practices
- Enable Change Data Feed
- Use Unity Catalog
- Avoid hardcoding paths
- Use partitioning + ZORDER
