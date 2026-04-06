"""
Feature Engineering Pipeline
Compute, register, and update features in Databricks Feature Store.
"""

from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup
from pyspark.sql import functions as F


def compute_customer_features(spark, source_table):
    """Compute customer-level features from order data."""
    return spark.table(source_table).groupBy("customer_id").agg(
        F.count("*").alias("total_orders"),
        F.sum("amount").alias("total_spend"),
        F.avg("amount").alias("avg_order_value"),
        F.min("order_date").alias("first_order_date"),
        F.max("order_date").alias("last_order_date"),
        F.datediff(F.current_date(), F.max("order_date")).alias("days_since_last_order"),
        F.countDistinct("product_id").alias("unique_products"),
    )


def compute_product_features(spark, source_table):
    """Compute product-level features."""
    return spark.table(source_table).groupBy("product_id").agg(
        F.count("*").alias("times_ordered"),
        F.sum("quantity").alias("total_quantity_sold"),
        F.avg("amount").alias("avg_price"),
        F.countDistinct("customer_id").alias("unique_buyers"),
    )


def register_features(feature_df, table_name, primary_keys, description):
    """Register a feature table in Unity Catalog."""
    fe = FeatureEngineeringClient()
    fe.create_table(
        name=table_name,
        primary_keys=primary_keys,
        df=feature_df,
        description=description
    )
    return table_name


def build_training_set(label_df, feature_tables, label_column):
    """
    Build a training set from multiple feature tables.

    Args:
        label_df: DataFrame with entity keys and labels
        feature_tables: List of dicts with 'table_name' and 'lookup_key'
        label_column: Name of the label column
    """
    fe = FeatureEngineeringClient()
    lookups = [
        FeatureLookup(
            table_name=ft["table_name"],
            lookup_key=ft["lookup_key"]
        )
        for ft in feature_tables
    ]

    training_set = fe.create_training_set(
        df=label_df,
        feature_lookups=lookups,
        label=label_column
    )
    return training_set.load_df()


if __name__ == "__main__":
    # Example: Compute and register customer features
    features = compute_customer_features(spark, "main.gold.orders")
    register_features(
        features,
        "main.features.customer_features",
        ["customer_id"],
        "Customer purchase behavior features"
    )
