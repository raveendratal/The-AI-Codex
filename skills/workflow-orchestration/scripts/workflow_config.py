"""
Workflow Orchestration Configuration
Build multi-task Databricks Jobs programmatically.
"""

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import (
    Task, NotebookTask, TaskDependency,
    CronSchedule, JobEmailNotifications,
    ClusterSpec
)


def create_etl_workflow(
    job_name,
    notebook_base_path,
    tasks_config,
    schedule_cron="0 0 6 * * ?",
    timezone="UTC",
    notification_emails=None,
    cluster_id=None,
    spark_version="15.4.x-scala2.12",
    num_workers=2,
    node_type="i3.xlarge"
):
    """
    Create a multi-task ETL workflow.

    Args:
        job_name: Name of the job
        notebook_base_path: Base path for notebooks
        tasks_config: List of dicts with 'key', 'notebook', 'depends_on' (optional)
        schedule_cron: Quartz cron expression
        timezone: Schedule timezone
        notification_emails: List of emails for failure alerts
        cluster_id: Existing cluster ID (if None, creates job cluster)
        spark_version: Runtime version for job cluster
        num_workers: Worker count for job cluster
        node_type: Instance type for job cluster
    """
    w = WorkspaceClient()

    tasks = []
    for tc in tasks_config:
        task_kwargs = {
            "task_key": tc["key"],
            "notebook_task": NotebookTask(
                notebook_path=f"{notebook_base_path}/{tc['notebook']}",
                base_parameters=tc.get("parameters", {})
            ),
        }

        # Dependencies
        if "depends_on" in tc:
            task_kwargs["depends_on"] = [
                TaskDependency(task_key=dep) for dep in tc["depends_on"]
            ]

        # Cluster config
        if cluster_id:
            task_kwargs["existing_cluster_id"] = cluster_id
        else:
            task_kwargs["new_cluster"] = ClusterSpec(
                spark_version=spark_version,
                num_workers=num_workers,
                node_type_id=node_type
            )

        # Retry config
        if tc.get("retries"):
            task_kwargs["max_retries"] = tc["retries"]
            task_kwargs["min_retry_interval_millis"] = tc.get("retry_interval_ms", 60000)

        tasks.append(Task(**task_kwargs))

    # Create job
    job = w.jobs.create(
        name=job_name,
        tasks=tasks,
        schedule=CronSchedule(
            quartz_cron_expression=schedule_cron,
            timezone_id=timezone
        ),
        email_notifications=JobEmailNotifications(
            on_failure=notification_emails or []
        ),
        max_concurrent_runs=1
    )

    return job


if __name__ == "__main__":
    # Example: Create a Medallion ETL workflow
    tasks = [
        {"key": "bronze", "notebook": "bronze_ingest", "retries": 2},
        {"key": "silver", "notebook": "silver_transform", "depends_on": ["bronze"]},
        {"key": "gold", "notebook": "gold_aggregate", "depends_on": ["silver"]},
        {"key": "dq", "notebook": "dq_validation", "depends_on": ["gold"]},
    ]

    job = create_etl_workflow(
        job_name="Daily Medallion ETL",
        notebook_base_path="/Repos/prod/etl",
        tasks_config=tasks,
        schedule_cron="0 0 6 * * ?",
        notification_emails=["data-team@company.com"]
    )
    print(f"Created job: {job.job_id}")
