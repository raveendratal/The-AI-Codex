-- =============================================================
-- Medallion ETL Template: Bronze → Silver → Gold
-- =============================================================

-- STEP 1: Silver Layer - Clean and deduplicate
CREATE OR REPLACE TABLE ${catalog}.silver.${table_name} AS
SELECT DISTINCT *
FROM ${catalog}.bronze.${table_name}
WHERE ${primary_key} IS NOT NULL
  AND _ingestion_timestamp >= current_date() - INTERVAL 1 DAY;

-- STEP 2: Gold Layer - Business aggregations
CREATE OR REPLACE TABLE ${catalog}.gold.${gold_table_name} AS
SELECT
  ${group_by_columns},
  COUNT(*) AS record_count,
  current_timestamp() AS last_updated
FROM ${catalog}.silver.${table_name}
GROUP BY ${group_by_columns};

-- STEP 3: Optimize
OPTIMIZE ${catalog}.gold.${gold_table_name}
  ZORDER BY (${zorder_columns});
