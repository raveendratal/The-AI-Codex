---
name: secret-management
description: Securely manage credentials, API keys, and connection strings using Databricks Secret Scopes and external vaults.
---

# Secret Management Skill

## When to Use
Use for storing and retrieving credentials without hardcoding in notebooks.

## Secret Scopes

### Databricks-Backed Scope
```python
# Create scope (via CLI or API)
# databricks secrets create-scope --scope my-scope

# Store secret
# databricks secrets put-secret --scope my-scope --key db-password

# Retrieve in notebook
password = dbutils.secrets.get(scope="my-scope", key="db-password")
```

### AWS Secrets Manager Backed
```python
# Create scope backed by AWS Secrets Manager
# databricks secrets create-scope --scope aws-secrets \
#   --scope-backend-type AWS_SECRETS_MANAGER \
#   --backend-aws-resource-name arn:aws:secretsmanager:us-east-1:123456:secret:my-secret

# Use exactly like Databricks-backed scope
api_key = dbutils.secrets.get(scope="aws-secrets", key="api-key")
```

## Common Patterns

### JDBC Connection
```python
jdbc_url = dbutils.secrets.get("db-scope", "jdbc-url")
username = dbutils.secrets.get("db-scope", "username")
password = dbutils.secrets.get("db-scope", "password")

df = spark.read.format("jdbc") \
  .option("url", jdbc_url) \
  .option("user", username) \
  .option("password", password) \
  .option("dbtable", "orders") \
  .load()
```

### Kafka Credentials
```python
df = spark.readStream.format("kafka") \
  .option("kafka.bootstrap.servers", broker) \
  .option("kafka.security.protocol", "SASL_SSL") \
  .option("kafka.sasl.mechanism", "PLAIN") \
  .option("kafka.sasl.jaas.config",
    f'kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required '
    f'username="{dbutils.secrets.get("kafka", "user")}" '
    f'password="{dbutils.secrets.get("kafka", "pass")}";') \
  .option("subscribe", "topic") \
  .load()
```

## Managing Scopes
```python
# List scopes
dbutils.secrets.listScopes()

# List keys in scope
dbutils.secrets.list("my-scope")

# Grant access
# databricks secrets put-acl --scope my-scope --principal users --permission READ
```

## Best Practices
- Never print or log secret values
- Use separate scopes per environment (dev/prod)
- Rotate secrets regularly
- Grant minimum required permissions
- Use AWS Secrets Manager for enterprise key rotation
