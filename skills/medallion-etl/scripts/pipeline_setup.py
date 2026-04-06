"""
Medallion ETL Pipeline Setup
Configures Auto Loader streaming ingestion into Bronze layer.
"""

def create_bronze_stream(spark, source_path, target_table, checkpoint_path, file_format="json"):
    """
    Create a streaming Auto Loader pipeline to ingest raw data into Bronze.

    Args:
        spark: SparkSession
        source_path: Path to raw data (e.g., /mnt/raw/orders or s3://bucket/raw/)
        target_table: Fully qualified Bronze table name (e.g., main.bronze.orders)
        checkpoint_path: Checkpoint location for streaming recovery
        file_format: Source file format (json, csv, parquet, avro)
    """
    df = (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", file_format)
        .option("cloudFiles.inferColumnTypes", "true")
        .option("cloudFiles.schemaEvolutionMode", "addNewColumns")
        .load(source_path)
    )

    # Add ingestion metadata
    from pyspark.sql.functions import current_timestamp, input_file_name
    df = df.withColumn("_ingestion_timestamp", current_timestamp()) \
           .withColumn("_source_file", input_file_name())

    query = (
        df.writeStream
        .format("delta")
        .option("checkpointLocation", checkpoint_path)
        .option("mergeSchema", "true")
        .trigger(availableNow=True)
        .toTable(target_table)
    )

    return query


def optimize_table(spark, table_name, zorder_columns=None):
    """
    Optimize a Delta table with optional ZORDER.

    Args:
        spark: SparkSession
        table_name: Fully qualified table name
        zorder_columns: List of columns to ZORDER by
    """
    if zorder_columns:
        cols = ", ".join(zorder_columns)
        spark.sql(f"OPTIMIZE {table_name} ZORDER BY ({cols})")
    else:
        spark.sql(f"OPTIMIZE {table_name}")


if __name__ == "__main__":
    # Example usage
    create_bronze_stream(
        spark=spark,
        source_path="/mnt/raw/orders",
        target_table="main.bronze.orders",
        checkpoint_path="/chk/bronze/orders",
        file_format="json"
    )
