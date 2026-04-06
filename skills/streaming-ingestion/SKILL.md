---
name: streaming-ingestion
description: Build real-time streaming pipelines using Kafka, Kinesis, Event Hubs, and Structured Streaming on Databricks.
---

# Streaming Ingestion Skill

## When to Use
Use for real-time data ingestion from message brokers and event streams.

## Supported Sources
- Apache Kafka / Confluent Cloud
- AWS Kinesis
- Azure Event Hubs
- Delta Lake as streaming source

## Kafka Streaming Example
```python
df = (spark.readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "<broker>:9092")
  .option("subscribe", "orders")
  .option("startingOffsets", "latest")
  .load())

from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

schema = StructType() \
  .add("order_id", StringType()) \
  .add("amount", DoubleType())

parsed = df.select(from_json(col("value").cast("string"), schema).alias("data")).select("data.*")

parsed.writeStream \
  .format("delta") \
  .option("checkpointLocation", "/chk/kafka_orders") \
  .trigger(processingTime="10 seconds") \
  .toTable("main.bronze.kafka_orders")
```

## Kinesis Example
```python
df = (spark.readStream
  .format("kinesis")
  .option("streamName", "orders-stream")
  .option("region", "us-east-1")
  .option("initialPosition", "TRIM_HORIZON")
  .load())
```

## Trigger Modes
| Mode | Use Case |
|------|----------|
| `processingTime` | Micro-batch at fixed intervals |
| `availableNow` | Process all available, then stop |
| `continuous` | Ultra-low latency (experimental) |

## Best Practices
- Use schema registry for Kafka/Avro
- Set watermarks for late data handling
- Monitor streaming metrics via Spark UI
- Use `availableNow` for cost-effective batch-like streaming
- Store secrets in Databricks Secret Scopes
