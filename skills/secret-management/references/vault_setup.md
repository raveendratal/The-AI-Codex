# Secret Scope Setup Guide

## Prerequisites
- Databricks CLI configured
- Workspace admin access (for scope creation)

## Step-by-Step: Databricks-Backed Scope

```bash
# 1. Create scope
databricks secrets create-scope --scope production-secrets

# 2. Add secrets
databricks secrets put-secret --scope production-secrets --key db-host --string-value "myhost.database.com"
databricks secrets put-secret --scope production-secrets --key db-user --string-value "admin"
databricks secrets put-secret --scope production-secrets --key db-password  # prompts for value

# 3. Set ACLs
databricks secrets put-acl --scope production-secrets --principal data-engineers --permission READ
databricks secrets put-acl --scope production-secrets --principal admins --permission MANAGE

# 4. Verify
databricks secrets list --scope production-secrets
databricks secrets get-acl --scope production-secrets --principal data-engineers
```

## Step-by-Step: AWS Secrets Manager

```bash
# 1. Create secret in AWS
aws secretsmanager create-secret --name /databricks/prod/db-credentials \
  --secret-string '{"host":"myhost.com","user":"admin","password":"secret"}'

# 2. Create Databricks scope backed by AWS
databricks secrets create-scope --scope aws-prod \
  --scope-backend-type AWS_SECRETS_MANAGER \
  --backend-aws-resource-name arn:aws:secretsmanager:us-east-1:123456789:secret:/databricks/prod

# 3. IAM Policy (attach to Databricks instance profile)
# Allow: secretsmanager:GetSecretValue, secretsmanager:ListSecrets
```

## Secret Rotation Checklist
- [ ] Rotate secrets every 90 days
- [ ] Update all dependent jobs/notebooks
- [ ] Verify access after rotation
- [ ] Update external vault if applicable
- [ ] Document rotation in audit log
