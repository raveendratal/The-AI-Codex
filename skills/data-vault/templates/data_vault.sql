-- =============================================================
-- Data Vault 2.0 Template
-- Hub + Satellite + Link generation
-- =============================================================

-- HUB: Business entity registration
CREATE TABLE IF NOT EXISTS ${catalog}.vault.hub_${entity} (
  ${entity}_hk STRING NOT NULL COMMENT 'Hash of business key',
  ${entity}_bk STRING NOT NULL COMMENT 'Business key',
  load_date TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
) USING DELTA
TBLPROPERTIES ('delta.autoOptimize.optimizeWrite' = 'true');

MERGE INTO ${catalog}.vault.hub_${entity} AS target
USING (
  SELECT DISTINCT
    md5(${business_key}) AS ${entity}_hk,
    ${business_key} AS ${entity}_bk,
    current_timestamp() AS load_date,
    '${source_system}' AS record_source
  FROM ${catalog}.${staging_schema}.${source_table}
) AS source
ON target.${entity}_hk = source.${entity}_hk
WHEN NOT MATCHED THEN INSERT *;

-- SATELLITE: Attribute history
CREATE TABLE IF NOT EXISTS ${catalog}.vault.sat_${entity} (
  ${entity}_hk STRING NOT NULL,
  ${attribute_columns},
  hash_diff STRING NOT NULL COMMENT 'Hash of attribute values',
  load_date TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
) USING DELTA;

MERGE INTO ${catalog}.vault.sat_${entity} AS target
USING (
  SELECT
    md5(${business_key}) AS ${entity}_hk,
    ${attribute_select},
    md5(concat_ws('|', ${attribute_list})) AS hash_diff,
    current_timestamp() AS load_date,
    '${source_system}' AS record_source
  FROM ${catalog}.${staging_schema}.${source_table}
) AS source
ON target.${entity}_hk = source.${entity}_hk
   AND target.hash_diff = source.hash_diff
WHEN NOT MATCHED THEN INSERT *;
