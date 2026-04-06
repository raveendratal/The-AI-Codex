---
name: workflow-orchestration
description: Design and manage multi-task Databricks Workflows with dependencies, parameters, retry logic, and scheduling.
---

# Workflow Orchestration Skill

## When to Use
Use for building production job pipelines with task dependencies and error handling.

## Multi-Task Job (Python SDK)
```python
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import *

w = WorkspaceClient()

job = w.jobs.create(
    name="Daily ETL Pipeline",
    tasks=[
        Task(
            task_key="bronze_ingest",
            notebook_task=NotebookTask(
                notebook_path="/Repos/prod/notebooks/bronze_ingest"
            ),
            new_cluster=ClusterSpec(
                spark_version="15.4.x-scala2.12",
                num_workers=2,
                node_type_id="i3.xlarge"
            )
        ),
        Task(
            task_key="silver_transform",
            depends_on=[TaskDependency(task_key="bronze_ingest")],
            notebook_task=NotebookTask(
                notebook_path="/Repos/prod/notebooks/silver_transform"
            ),
            existing_cluster_id="<cluster-id>"
        ),
        Task(
            task_key="gold_aggregate",
            depends_on=[TaskDependency(task_key="silver_transform")],
            notebook_task=NotebookTask(
                notebook_path="/Repos/prod/notebooks/gold_aggregate"
            ),
            existing_cluster_id="<cluster-id>"
        ),
        Task(
            task_key="dq_validation",
            depends_on=[TaskDependency(task_key="gold_aggregate")],
            notebook_task=NotebookTask(
                notebook_path="/Repos/prod/notebooks/dq_checks"
            ),
            existing_cluster_id="<cluster-id>"
        ),
    ],
    schedule=CronSchedule(
        quartz_cron_expression="0 0 6 * * ?",
        timezone_id="UTC"
    ),
    email_notifications=JobEmailNotifications(
        on_failure=["team@company.com"]
    ),
    max_concurrent_runs=1
)
```

## Task Parameters
```python
# Pass parameters between tasks
Task(
    task_key="transform",
    notebook_task=NotebookTask(
        notebook_path="/notebooks/transform",
        base_parameters={
            "date": "{{job.start_time.iso_date}}",
            "env": "production"
        }
    )
)
```

## Retry & Timeout
```python
Task(
    task_key="critical_task",
    max_retries=3,
    min_retry_interval_millis=60000,  # 1 minute
    timeout_seconds=3600,  # 1 hour
    notebook_task=NotebookTask(notebook_path="/notebooks/critical")
)
```

## Conditional Tasks
```python
# Run task only if previous task fails
Task(
    task_key="alert_on_failure",
    depends_on=[TaskDependency(
        task_key="main_task",
        outcome="task_failure"
    )],
    notebook_task=NotebookTask(notebook_path="/notebooks/alert")
)
```

## Best Practices
- Use job clusters (not interactive) for production
- Set max_concurrent_runs to prevent overlaps
- Add email/Slack notifications on failure
- Use task parameters for environment config
- Monitor via system.lakeflow tables
