# Unity Catalog Governance Policies Reference

## Access Control Matrix

| Role            | Bronze | Silver | Gold  | Models |
|-----------------|--------|--------|-------|--------|
| Data Engineer   | RW     | RW     | RW    | R      |
| Data Scientist  | R      | R      | RW    | RW     |
| Analyst         | -      | R      | R     | -      |
| Admin           | RW     | RW     | RW    | RW     |

## Standard Grants

```sql
-- Analyst role: read-only on Gold
GRANT USAGE ON CATALOG main TO `analyst_role`;
GRANT USAGE ON SCHEMA main.gold TO `analyst_role`;
GRANT SELECT ON SCHEMA main.gold TO `analyst_role`;

-- Data Engineer: full access
GRANT ALL PRIVILEGES ON CATALOG main TO `data_engineer_role`;

-- Data Scientist: Gold + Models
GRANT USAGE ON CATALOG main TO `data_scientist_role`;
GRANT SELECT ON SCHEMA main.gold TO `data_scientist_role`;
GRANT CREATE TABLE ON SCHEMA main.gold TO `data_scientist_role`;
```

## PII Handling
- Tag PII columns with `COMMENT 'PII'`
- Apply column masking functions
- Use row-level security views for region-scoped access

## Audit Requirements
- Enable system audit logs
- Review access weekly
- Alert on anomalous access patterns
