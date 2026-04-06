---
name: schema-evolution
description: Manage Delta Lake schema evolution, migrations, and backward compatibility for production tables.
---

# Schema Evolution Skill

## When to Use
Use when source schemas change and you need to evolve Delta tables safely.

## Schema Evolution Modes
| Mode | Behavior | Risk |
|------|----------|------|
| `mergeSchema` | Add new columns automatically | Low |
| `overwriteSchema` | Replace schema entirely | High |
| Manual ALTER | Controlled column changes | Low |

## Auto Schema Evolution (Streaming)
```python
df.writeStream.format("delta") \
  .option("mergeSchema", "true") \
  .option("checkpointLocation", "/chk/table") \
  .toTable("main.silver.events")
```

## Manual Schema Changes
```sql
-- Add column
ALTER TABLE main.silver.orders ADD COLUMN discount DOUBLE COMMENT 'Order discount';

-- Rename column
ALTER TABLE main.silver.orders RENAME COLUMN discount TO discount_pct;

-- Change column type (safe widening)
ALTER TABLE main.silver.orders ALTER COLUMN amount TYPE DECIMAL(12, 2);

-- Drop column
ALTER TABLE main.silver.orders DROP COLUMN temp_field;

-- Set NOT NULL constraint
ALTER TABLE main.silver.orders ALTER COLUMN order_id SET NOT NULL;
```

## Schema Validation
```python
def validate_schema(spark, table_name, expected_columns):
    """Validate table schema matches expected columns."""
    actual = {f.name: str(f.dataType) for f in spark.table(table_name).schema.fields}
    missing = [c for c in expected_columns if c not in actual]
    extra = [c for c in actual if c not in expected_columns]
    return {"missing": missing, "extra": extra, "valid": len(missing) == 0}
```

## Migration Pattern
```sql
-- 1. Create new table with updated schema
CREATE TABLE main.silver.orders_v2 AS
SELECT *, CAST(NULL AS DOUBLE) AS new_column
FROM main.silver.orders;

-- 2. Validate
SELECT COUNT(*) FROM main.silver.orders_v2;

-- 3. Swap
ALTER TABLE main.silver.orders RENAME TO main.silver.orders_backup;
ALTER TABLE main.silver.orders_v2 RENAME TO main.silver.orders;
```

## Best Practices
- Use `mergeSchema` for additive changes only
- Test schema changes in dev before prod
- Always backup before destructive changes
- Document schema versions in table properties
- Use column comments for documentation
