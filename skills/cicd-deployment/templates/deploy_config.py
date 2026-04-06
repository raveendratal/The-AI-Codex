"""
CI/CD Deployment Configuration
Helper utilities for Databricks Asset Bundle deployments.
"""

import json
import os


def generate_bundle_config(
    bundle_name,
    workspace_host,
    jobs=None,
    pipelines=None,
    targets=None
):
    """
    Generate a databricks.yml configuration programmatically.

    Args:
        bundle_name: Name of the asset bundle
        workspace_host: Databricks workspace URL
        jobs: List of job configurations
        pipelines: List of pipeline configurations
        targets: Dict of deployment targets
    """
    config = {
        "bundle": {"name": bundle_name},
        "workspace": {"host": workspace_host},
        "resources": {},
    }

    if jobs:
        config["resources"]["jobs"] = {}
        for job in jobs:
            config["resources"]["jobs"][job["key"]] = {
                "name": job["name"],
                "tasks": job.get("tasks", []),
                "schedule": job.get("schedule"),
            }

    if pipelines:
        config["resources"]["pipelines"] = {}
        for pipe in pipelines:
            config["resources"]["pipelines"][pipe["key"]] = {
                "name": pipe["name"],
                "target": pipe.get("target_schema"),
                "catalog": pipe.get("catalog"),
            }

    if targets:
        config["targets"] = targets
    else:
        config["targets"] = {
            "dev": {
                "default": True,
                "workspace": {
                    "root_path": f"/Users/${{workspace.current_user.userName}}/.bundle/{bundle_name}"
                },
            },
            "prod": {
                "workspace": {
                    "root_path": f"/Shared/.bundle/{bundle_name}"
                },
            },
        }

    return config


def validate_deployment(spark, job_name):
    """
    Validate a deployed job exists and check last run status.
    """
    from databricks.sdk import WorkspaceClient
    w = WorkspaceClient()

    jobs_list = w.jobs.list(name=job_name)
    for job in jobs_list:
        runs = w.jobs.list_runs(job_id=job.job_id, limit=1)
        for run in runs:
            return {
                "job_id": job.job_id,
                "job_name": job.settings.name,
                "last_run_state": run.state.result_state.value if run.state.result_state else "RUNNING",
                "last_run_time": str(run.start_time),
            }
    return {"error": f"Job '{job_name}' not found"}
