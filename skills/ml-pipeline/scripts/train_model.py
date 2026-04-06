"""
ML Pipeline - Model Training Script
Train, log, and register models using MLflow on Databricks.
"""

import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import pandas as pd


def train_and_log_model(
    spark,
    feature_table,
    target_column,
    experiment_name,
    model_name,
    test_size=0.2,
    n_estimators=100,
    max_depth=10
):
    """
    Train a RandomForest model, log to MLflow, and register.

    Args:
        spark: SparkSession
        feature_table: Fully qualified Gold table with features
        target_column: Name of the target/label column
        experiment_name: MLflow experiment name
        model_name: Name for model registry
        test_size: Train/test split ratio
        n_estimators: Number of trees
        max_depth: Max tree depth
    """
    # Load features
    df = spark.table(feature_table).toPandas()
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=42
    )

    # Set experiment
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run():
        # Train
        model = RandomForestClassifier(
            n_estimators=n_estimators,
            max_depth=max_depth,
            random_state=42
        )
        model.fit(X_train, y_train)

        # Evaluate
        y_pred = model.predict(X_test)
        metrics = {
            "accuracy": accuracy_score(y_test, y_pred),
            "f1_score": f1_score(y_test, y_pred, average="weighted"),
            "precision": precision_score(y_test, y_pred, average="weighted"),
            "recall": recall_score(y_test, y_pred, average="weighted"),
        }

        # Log parameters and metrics
        mlflow.log_params({"n_estimators": n_estimators, "max_depth": max_depth})
        mlflow.log_metrics(metrics)

        # Log model with signature
        from mlflow.models import infer_signature
        signature = infer_signature(X_train, y_pred)
        mlflow.sklearn.log_model(
            model, "model",
            signature=signature,
            input_example=X_train.head(5)
        )

        # Register model
        run_id = mlflow.active_run().info.run_id
        mlflow.register_model(f"runs:/{run_id}/model", model_name)

        print(f"Model registered: {model_name}")
        print(f"Metrics: {metrics}")

    return metrics


if __name__ == "__main__":
    # Example usage
    train_and_log_model(
        spark=spark,
        feature_table="main.gold.customer_features",
        target_column="churn",
        experiment_name="/Users/shared/churn_experiment",
        model_name="churn_model"
    )
