---
name: dq-validation
description: Perform enterprise-grade data quality checks including nulls, duplicates, schema validation, and thresholds.
---

# Data Quality Validation Skill

## When to Use
Use after Silver/Gold transformations to validate data integrity.

## Checks

### 1. Null Check
```sql
SELECT COUNT(*) FROM table WHERE column IS NULL;
```

### 2. Duplicate Check
```sql
SELECT column, COUNT(*)
FROM table
GROUP BY column
HAVING COUNT(*) > 1;
```

### 3. Schema Validation
- Compare expected vs actual schema using `DESCRIBE TABLE`
- Validate column types, nullability, and order

### 4. Threshold Check
```sql
SELECT COUNT(*) FROM table HAVING COUNT(*) < 100;
```

## Output
- Pass / Fail status per check
- Error summary with affected row counts

## Best Practices
- Store results in an audit table
- Integrate with alerts (SNS / email)
- Run DQ checks as part of pipeline orchestration
