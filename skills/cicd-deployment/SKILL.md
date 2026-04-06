---
name: cicd-deployment
description: Implement CI/CD pipelines for Databricks using Databricks Asset Bundles (DABs), GitHub Actions, and Terraform.
---

# CI/CD Deployment Skill

## When to Use
Use for automating deployment of notebooks, jobs, pipelines, and infrastructure.

## Databricks Asset Bundles (DABs)
```yaml
# databricks.yml
bundle:
  name: my-data-pipeline

workspace:
  host: https://<workspace-url>

resources:
  jobs:
    etl_job:
      name: "Daily ETL Pipeline"
      tasks:
        - task_key: bronze_ingestion
          notebook_task:
            notebook_path: ./notebooks/bronze_ingestion
        - task_key: silver_transform
          depends_on:
            - task_key: bronze_ingestion
          notebook_task:
            notebook_path: ./notebooks/silver_transform
      schedule:
        quartz_cron_expression: "0 0 6 * * ?"
        timezone_id: UTC

targets:
  dev:
    default: true
    workspace:
      root_path: /Users/${workspace.current_user.userName}/.bundle/${bundle.name}
  prod:
    workspace:
      root_path: /Shared/.bundle/${bundle.name}
      host: https://<prod-workspace>
```

## GitHub Actions Workflow
```yaml
# .github/workflows/deploy.yml
name: Deploy to Databricks
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: databricks/setup-cli@main
      - run: databricks bundle validate -t prod
      - run: databricks bundle deploy -t prod
```

## Terraform Example
```hcl
resource "databricks_job" "etl" {
  name = "Daily ETL"
  task {
    task_key = "bronze"
    notebook_task {
      notebook_path = "/Repos/prod/notebooks/bronze"
    }
  }
  schedule {
    quartz_cron_expression = "0 0 6 * * ?"
    timezone_id = "UTC"
  }
}
```

## Best Practices
- Use DABs for native Databricks deployments
- Separate dev/staging/prod targets
- Run tests before deployment
- Use service principals for CI/CD authentication
- Version control all configurations
