---
name: feature-store
description: Build and manage ML features using Databricks Feature Store and Unity Catalog feature engineering.
---

# Feature Store Skill

## When to Use
Use for creating reusable, governed ML features with point-in-time correctness.

## Workflow
1. Compute features from Gold tables
2. Register in Feature Store
3. Create training sets with point-in-time joins
4. Serve features for inference

## Create Feature Table
```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

# Compute features
feature_df = spark.sql("""
  SELECT
    customer_id,
    COUNT(*) AS total_orders,
    AVG(amount) AS avg_order_value,
    MAX(order_date) AS last_order_date,
    DATEDIFF(current_date(), MAX(order_date)) AS days_since_last_order
  FROM main.gold.orders
  GROUP BY customer_id
""")

# Register feature table
fe.create_table(
    name="main.features.customer_features",
    primary_keys=["customer_id"],
    df=feature_df,
    description="Customer purchase behavior features"
)
```

## Create Training Set
```python
from databricks.feature_engineering import FeatureLookup

training_labels = spark.table("main.gold.customer_labels")

training_set = fe.create_training_set(
    df=training_labels,
    feature_lookups=[
        FeatureLookup(
            table_name="main.features.customer_features",
            lookup_key="customer_id"
        )
    ],
    label="churn"
)

training_df = training_set.load_df()
```

## Update Features
```python
fe.write_table(
    name="main.features.customer_features",
    df=updated_features_df,
    mode="merge"  # or "overwrite"
)
```

## Best Practices
- Use Unity Catalog for feature governance
- Define clear primary keys
- Include timestamp columns for time-series features
- Schedule feature refresh jobs
- Use `mode='merge'` for incremental updates
