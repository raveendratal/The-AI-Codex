---
name: delta-sharing
description: Share data securely across organizations using Delta Sharing and Unity Catalog sharing features.
---

# Delta Sharing Skill

## When to Use
Use for sharing data with external partners, cross-workspace access, or open-protocol data distribution.

## Sharing Types
| Type | Protocol | Recipient |
|------|----------|-----------|
| Databricks-to-Databricks | Unity Catalog | Internal workspaces |
| Open Sharing | Delta Sharing protocol | Any platform (Spark, pandas, etc.) |

## Create a Share
```sql
-- Create share
CREATE SHARE IF NOT EXISTS sales_share
COMMENT 'Shared sales data for partner analytics';

-- Add tables to share
ALTER SHARE sales_share ADD TABLE main.gold.sales;
ALTER SHARE sales_share ADD TABLE main.gold.customers
  WITH HISTORY;  -- enables time travel for recipient

-- Add with partition filter (share only specific data)
ALTER SHARE sales_share ADD TABLE main.gold.orders
  PARTITION (region = 'US');
```

## Manage Recipients
```sql
-- Create recipient (Databricks-to-Databricks)
CREATE RECIPIENT IF NOT EXISTS partner_analytics
  USING ID '<sharing-identifier>';

-- Create recipient (open sharing)
CREATE RECIPIENT IF NOT EXISTS external_partner;
-- This generates an activation link

-- Grant share to recipient
GRANT SELECT ON SHARE sales_share TO RECIPIENT partner_analytics;

-- View recipients
SHOW RECIPIENTS;
SHOW GRANTS ON SHARE sales_share;
```

## Consume Shared Data
```sql
-- Create catalog from share
CREATE CATALOG IF NOT EXISTS partner_data
  USING SHARE provider_org.sales_share;

-- Query shared data
SELECT * FROM partner_data.gold.sales LIMIT 10;
```

## Open Sharing (Python)
```python
import delta_sharing

profile = "config.share"
client = delta_sharing.SharingClient(profile)
tables = client.list_all_tables()

df = delta_sharing.load_as_pandas(f"{profile}#share_name.schema.table")
```

## Best Practices
- Use partition filters to limit shared data
- Rotate recipient tokens periodically
- Monitor share access via audit logs
- Use `WITH HISTORY` sparingly (increases storage)
- Document sharing agreements
