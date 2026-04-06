-- =============================================================
-- Lakehouse Federation Query Templates
-- =============================================================

-- TEMPLATE 1: Create connection
CREATE CONNECTION IF NOT EXISTS ${connection_name}
  TYPE ${db_type}  -- POSTGRESQL, MYSQL, SQLSERVER, SNOWFLAKE, BIGQUERY
  OPTIONS (
    host '${host}',
    port '${port}',
    user secret('${secret_scope}', '${user_key}'),
    password secret('${secret_scope}', '${password_key}')
  );

-- TEMPLATE 2: Create foreign catalog
CREATE FOREIGN CATALOG IF NOT EXISTS ${catalog_name}
  USING CONNECTION ${connection_name}
  OPTIONS (database '${database_name}');

-- TEMPLATE 3: Materialize external data as Delta (for performance)
CREATE OR REPLACE TABLE main.silver.${table_name} AS
SELECT *
FROM ${foreign_catalog}.${schema}.${table_name}
WHERE ${incremental_filter};  -- e.g., updated_at >= current_date() - INTERVAL 1 DAY

-- TEMPLATE 4: Cross-source analytical join
SELECT
  d.*, e.*
FROM main.gold.${delta_table} d
JOIN ${foreign_catalog}.${schema}.${external_table} e
  ON d.${join_key} = e.${join_key}
WHERE d.${filter_column} >= current_date() - INTERVAL ${lookback_days} DAY;

-- TEMPLATE 5: Monitor connection health
SELECT 1 AS health_check
FROM ${foreign_catalog}.${schema}.${table_name}
LIMIT 1;
