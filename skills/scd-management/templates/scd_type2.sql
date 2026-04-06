-- =============================================================
-- SCD Type 2 Template
-- Parameterized for any dimension table
-- =============================================================

-- Prerequisites: Target table must have these columns:
--   ${primary_key}, is_current (BOOLEAN), start_date (DATE),
--   end_date (DATE), updated_at (TIMESTAMP)

-- STEP 1: Close changed records
MERGE INTO ${catalog}.${schema}.${target_table} AS target
USING ${catalog}.${staging_schema}.${source_table} AS source
ON target.${primary_key} = source.${primary_key}
   AND target.is_current = true
WHEN MATCHED AND (
  ${change_detection_columns}  -- e.g.: target.col1 <> source.col1 OR target.col2 <> source.col2
) THEN UPDATE SET
  target.is_current = false,
  target.end_date = current_date(),
  target.updated_at = current_timestamp();

-- STEP 2: Insert new/changed records as current
INSERT INTO ${catalog}.${schema}.${target_table}
SELECT
  source.*,
  true AS is_current,
  current_date() AS start_date,
  NULL AS end_date,
  current_timestamp() AS updated_at
FROM ${catalog}.${staging_schema}.${source_table} source
LEFT ANTI JOIN ${catalog}.${schema}.${target_table} target
  ON target.${primary_key} = source.${primary_key}
  AND target.is_current = true
  AND NOT (${change_detection_columns});

-- STEP 3: Insert brand new records
INSERT INTO ${catalog}.${schema}.${target_table}
SELECT
  source.*,
  true AS is_current,
  current_date() AS start_date,
  NULL AS end_date,
  current_timestamp() AS updated_at
FROM ${catalog}.${staging_schema}.${source_table} source
WHERE NOT EXISTS (
  SELECT 1 FROM ${catalog}.${schema}.${target_table} target
  WHERE target.${primary_key} = source.${primary_key}
);
