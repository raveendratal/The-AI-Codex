---
name: dashboard-gen
description: Generate business dashboards using SQL and Databricks SQL.
---

# Dashboard Generation Skill

## Workflow
1. Identify KPIs
2. Query Gold tables
3. Build SQL views
4. Create dashboard

## Example KPI Query
```sql
SELECT
  date,
  SUM(revenue) AS total_revenue,
  COUNT(DISTINCT customer_id) AS customers
FROM main.gold.sales
GROUP BY date;
```

## Dashboard Components
- Revenue trends (line chart)
- Customer growth (area chart)
- Top products (bar chart)
- KPI summary cards

## Best Practices
- Use aggregated Gold tables for performance
- Optimize queries with proper indexing
- Use caching for frequently accessed dashboards
- Build reusable SQL views for common metrics
