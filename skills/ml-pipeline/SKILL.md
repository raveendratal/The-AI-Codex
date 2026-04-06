---
name: ml-pipeline
description: Build, train, track, and deploy ML models using MLflow in Databricks.
---

# ML Pipeline Skill

## Workflow
1. Load features from Gold layer
2. Train model
3. Log with MLflow
4. Register model
5. Deploy

## Training Example
```python
import mlflow
from sklearn.ensemble import RandomForestClassifier

with mlflow.start_run():
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    mlflow.sklearn.log_model(model, "model")
```

## Model Registry
```python
mlflow.register_model("runs:/<run_id>/model", "sales_model")
```

## Deployment
- Batch scoring via Spark UDF
- Real-time endpoint via Model Serving

## Best Practices
- Use feature store for consistent features
- Track experiments with MLflow
- Version models in Unity Catalog
- Include signature and input_example in log_model calls
