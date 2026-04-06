---
name: lakehouse-federation
description: Query external databases (PostgreSQL, MySQL, SQL Server, Snowflake, BigQuery) directly from Databricks using Lakehouse Federation.
---

# Lakehouse Federation Skill

## When to Use
Use for querying external databases without data movement, or for hybrid architectures.

## Supported Sources
| Source | Connection Type |
|--------|-----------------|
| PostgreSQL | JDBC |
| MySQL | JDBC |
| SQL Server | JDBC |
| Snowflake | Native connector |
| BigQuery | Native connector |
| Redshift | JDBC |

## Create Foreign Connection
```sql
-- Create connection to PostgreSQL
CREATE CONNECTION IF NOT EXISTS pg_production
  TYPE POSTGRESQL
  OPTIONS (
    host 'pghost.example.com',
    port '5432',
    user secret('db-scope', 'pg-user'),
    password secret('db-scope', 'pg-password')
  );
```

## Create Foreign Catalog
```sql
-- Register external database as a catalog
CREATE FOREIGN CATALOG IF NOT EXISTS pg_prod
  USING CONNECTION pg_production
  OPTIONS (database 'production');

-- Query external data directly
SELECT * FROM pg_prod.public.customers LIMIT 10;
```

## Cross-Source Joins
```sql
-- Join Delta table with PostgreSQL table
SELECT
  o.order_id,
  o.amount,
  c.name,
  c.email
FROM main.gold.orders o
JOIN pg_prod.public.customers c
  ON o.customer_id = c.id;
```

## MySQL Connection
```sql
CREATE CONNECTION mysql_conn
  TYPE MYSQL
  OPTIONS (
    host 'mysql.example.com',
    port '3306',
    user secret('db-scope', 'mysql-user'),
    password secret('db-scope', 'mysql-password')
  );

CREATE FOREIGN CATALOG mysql_prod
  USING CONNECTION mysql_conn
  OPTIONS (database 'ecommerce');
```

## Snowflake Connection
```sql
CREATE CONNECTION sf_conn
  TYPE SNOWFLAKE
  OPTIONS (
    host 'account.snowflakecomputing.com',
    user secret('sf-scope', 'user'),
    password secret('sf-scope', 'password'),
    sfWarehouse 'COMPUTE_WH'
  );
```

## Best Practices
- Use secrets for all credentials
- Apply predicate pushdown (WHERE clauses push to source)
- Cache frequently accessed external data as Delta tables
- Monitor query performance across sources
- Use federation for reads; use Delta for analytical workloads
