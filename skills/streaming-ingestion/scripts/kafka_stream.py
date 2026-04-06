"""
Streaming Ingestion - Kafka Consumer Pipeline
Configurable Kafka-to-Delta streaming with schema parsing and watermarking.
"""

from pyspark.sql.functions import from_json, col, current_timestamp, expr
from pyspark.sql.types import StructType


def create_kafka_stream(
    spark,
    bootstrap_servers,
    topic,
    target_table,
    checkpoint_path,
    schema,
    trigger_interval="30 seconds",
    watermark_column=None,
    watermark_delay="10 minutes",
    starting_offsets="latest"
):
    """
    Create a Kafka-to-Delta streaming pipeline.

    Args:
        spark: SparkSession
        bootstrap_servers: Kafka broker addresses
        topic: Kafka topic name
        target_table: Fully qualified Delta table
        checkpoint_path: Checkpoint location
        schema: StructType for JSON payload parsing
        trigger_interval: Micro-batch interval
        watermark_column: Column for watermark (optional)
        watermark_delay: Late data tolerance
        starting_offsets: earliest / latest
    """
    raw = (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", bootstrap_servers)
        .option("subscribe", topic)
        .option("startingOffsets", starting_offsets)
        .option("failOnDataLoss", "false")
        .load()
    )

    # Parse JSON value
    parsed = (
        raw.select(
            from_json(col("value").cast("string"), schema).alias("data"),
            col("topic"),
            col("partition"),
            col("offset"),
            col("timestamp").alias("kafka_timestamp")
        )
        .select("data.*", "topic", "partition", "offset", "kafka_timestamp")
        .withColumn("_ingestion_timestamp", current_timestamp())
    )

    # Apply watermark if specified
    if watermark_column:
        parsed = parsed.withWatermark(watermark_column, watermark_delay)

    # Write to Delta
    query = (
        parsed.writeStream
        .format("delta")
        .option("checkpointLocation", checkpoint_path)
        .option("mergeSchema", "true")
        .trigger(processingTime=trigger_interval)
        .toTable(target_table)
    )

    return query


def create_kinesis_stream(
    spark,
    stream_name,
    region,
    target_table,
    checkpoint_path,
    schema,
    initial_position="TRIM_HORIZON"
):
    """
    Create a Kinesis-to-Delta streaming pipeline.
    """
    raw = (
        spark.readStream
        .format("kinesis")
        .option("streamName", stream_name)
        .option("region", region)
        .option("initialPosition", initial_position)
        .load()
    )

    parsed = (
        raw.select(
            from_json(col("data").cast("string"), schema).alias("data")
        )
        .select("data.*")
        .withColumn("_ingestion_timestamp", current_timestamp())
    )

    query = (
        parsed.writeStream
        .format("delta")
        .option("checkpointLocation", checkpoint_path)
        .trigger(availableNow=True)
        .toTable(target_table)
    )

    return query
