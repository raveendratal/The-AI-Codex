---
name: scd-management
description: Implement Slowly Changing Dimensions (Type 1, 2, 3) using Delta Lake MERGE for dimensional modeling.
---

# SCD Management Skill

## When to Use
Use for maintaining dimension tables with historical tracking in Silver/Gold layers.

## SCD Types
| Type | Behavior | History |
|------|----------|---------|
| Type 1 | Overwrite | No history |
| Type 2 | Add new row, close old | Full history |
| Type 3 | Add column for previous value | Limited history |

## SCD Type 1 (Overwrite)
```sql
MERGE INTO main.silver.dim_customer AS target
USING main.bronze.customer_updates AS source
ON target.customer_id = source.customer_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```

## SCD Type 2 (Historical)
```sql
-- Step 1: Close existing records
MERGE INTO main.silver.dim_customer AS target
USING main.bronze.customer_updates AS source
ON target.customer_id = source.customer_id
   AND target.is_current = true
WHEN MATCHED AND (
  target.email <> source.email OR target.address <> source.address
) THEN UPDATE SET
  target.is_current = false,
  target.end_date = current_date(),
  target.updated_at = current_timestamp();

-- Step 2: Insert new current records
INSERT INTO main.silver.dim_customer
SELECT
  customer_id, name, email, address,
  true AS is_current,
  current_date() AS start_date,
  NULL AS end_date,
  current_timestamp() AS updated_at
FROM main.bronze.customer_updates source
WHERE NOT EXISTS (
  SELECT 1 FROM main.silver.dim_customer target
  WHERE target.customer_id = source.customer_id
    AND target.is_current = true
    AND target.email = source.email
    AND target.address = source.address
);
```

## Best Practices
- Use surrogate keys for Type 2
- Add `is_current`, `start_date`, `end_date` columns
- Enable Change Data Feed on source tables
- Partition by `is_current` for query performance
