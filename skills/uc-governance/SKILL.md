---
name: uc-governance
description: Apply Unity Catalog governance including access control, masking, lineage, and auditing.
---

# Unity Catalog Governance Skill

## Use Cases
- Secure sensitive data
- Enforce policies
- Track lineage

## Access Control
```sql
GRANT SELECT ON TABLE main.gold.sales TO `analyst_role`;
```

## Row-Level Security
```sql
CREATE VIEW secure_sales AS
SELECT * FROM sales WHERE region = current_user_region();
```

## Column Masking
```sql
SELECT mask(email) FROM customers;
```

## Auditing
- Enable audit logs in Unity Catalog
- Track access patterns and data usage
- Monitor grants and permission changes

## Best Practices
- Use roles, not individual users
- Centralize policies in Unity Catalog
- Apply least-privilege access
- Review lineage graphs for sensitive data flows
