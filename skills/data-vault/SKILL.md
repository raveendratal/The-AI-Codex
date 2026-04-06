---
name: data-vault
description: Implement Data Vault 2.0 modeling (Hub, Link, Satellite) on Delta Lake for auditable, scalable data warehouses.
---

# Data Vault Skill

## When to Use
Use for building auditable, insert-only data warehouses with full history tracking.

## Data Vault Components
| Component | Purpose | Key Columns |
|-----------|---------|-------------|
| Hub | Business keys | hash_key, business_key, load_date, source |
| Link | Relationships | hash_key, hub_fk_1, hub_fk_2, load_date, source |
| Satellite | Descriptive attributes | hash_key, hub_fk, attributes, load_date, hash_diff, source |

## Hub Example
```sql
CREATE TABLE IF NOT EXISTS main.vault.hub_customer (
  customer_hk STRING NOT NULL,
  customer_bk STRING NOT NULL,
  load_date TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
) USING DELTA;

MERGE INTO main.vault.hub_customer AS target
USING (
  SELECT md5(customer_id) AS customer_hk, customer_id AS customer_bk,
         current_timestamp() AS load_date, 'crm_system' AS record_source
  FROM main.bronze.customers
) AS source
ON target.customer_hk = source.customer_hk
WHEN NOT MATCHED THEN INSERT *;
```

## Satellite Example
```sql
CREATE TABLE IF NOT EXISTS main.vault.sat_customer (
  customer_hk STRING NOT NULL,
  name STRING, email STRING, phone STRING,
  hash_diff STRING NOT NULL,
  load_date TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
) USING DELTA;

MERGE INTO main.vault.sat_customer AS target
USING (
  SELECT md5(customer_id) AS customer_hk,
         name, email, phone,
         md5(concat(name, email, phone)) AS hash_diff,
         current_timestamp() AS load_date,
         'crm_system' AS record_source
  FROM main.bronze.customers
) AS source
ON target.customer_hk = source.customer_hk
   AND target.hash_diff = source.hash_diff
WHEN NOT MATCHED THEN INSERT *;
```

## Link Example
```sql
CREATE TABLE IF NOT EXISTS main.vault.link_order_customer (
  link_hk STRING NOT NULL,
  order_hk STRING NOT NULL,
  customer_hk STRING NOT NULL,
  load_date TIMESTAMP NOT NULL,
  record_source STRING NOT NULL
) USING DELTA;
```

## Best Practices
- Use MD5/SHA-256 for hash keys
- Hub tables are insert-only (never update)
- Use hash_diff in Satellites for change detection
- Separate raw vault from business vault
