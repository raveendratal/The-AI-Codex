-- =============================================================
-- Schema Migration Template
-- Safe schema evolution with rollback support
-- =============================================================

-- STEP 1: Document current schema
DESCRIBE TABLE EXTENDED ${catalog}.${schema}.${table_name};

-- STEP 2: Create backup
CREATE TABLE ${catalog}.${schema}.${table_name}_backup
DEEP CLONE ${catalog}.${schema}.${table_name};

-- STEP 3: Apply migrations
-- Add new columns
ALTER TABLE ${catalog}.${schema}.${table_name}
  ADD COLUMN ${new_column_name} ${new_column_type}
  COMMENT '${column_comment}';

-- Set default value via UPDATE (if needed)
UPDATE ${catalog}.${schema}.${table_name}
SET ${new_column_name} = ${default_value}
WHERE ${new_column_name} IS NULL;

-- STEP 4: Validate migration
SELECT
  COUNT(*) AS total_rows,
  COUNT(${new_column_name}) AS non_null_new_col,
  COUNT(*) - COUNT(${new_column_name}) AS null_new_col
FROM ${catalog}.${schema}.${table_name};

-- STEP 5: Update table properties
ALTER TABLE ${catalog}.${schema}.${table_name}
  SET TBLPROPERTIES ('schema.version' = '${new_version}', 'schema.updated' = current_timestamp());

-- ROLLBACK (if needed)
-- DROP TABLE ${catalog}.${schema}.${table_name};
-- ALTER TABLE ${catalog}.${schema}.${table_name}_backup RENAME TO ${catalog}.${schema}.${table_name};
