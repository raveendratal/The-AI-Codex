# Databricks 300+ Developer Prompt Library (Fully Expanded Markdown Edition)

This document provides the complete, expanded, GitHub-ready Markdown containing **all 365 Databricks developer prompts** across PySpark, SQL, Delta Lake, Unity Catalog, Lakeflow (DLT), AI Assistant, MLflow, Feature Store, Mosaic AI, RAG / Vector Search, and Agent Systems.

---

# Section 1 — PySpark Prompts (60)

## DataFrame Creation
1. Generate PySpark code to create a DataFrame with sample data for customers (id, name, age, city).
2. Write PySpark code to read a CSV from a UC volume into a Delta table.
3. Create a PySpark schema for nested JSON with arrays and structs.

## Transformations
4. Convert multiple columns to proper datatypes using withColumn + cast.
5. Perform multi-level aggregation using groupBy + agg.
6. Filter rows using complex AND/OR boolean expressions.
7. Flatten nested struct, map, and array columns.

## Joins
8. Write PySpark code for inner, left, right, full, semi, anti joins.
9. Optimize joins using broadcast().
10. Handle skew joins using salting.

## Window Functions
11. Use row_number(), rank(), dense_rank().
12. Get first/last purchase per customer via window.
13. Compute rolling averages with time-based windows.

## String & Date Functions
14. Extract year, month, week, quarter.
15. Clean text with regexp_replace.
16. Calculate timestamp differences.

## Delta + PySpark
17. MERGE INTO using PySpark for Delta Lake.
18. Time travel queries in PySpark.
19. Implement CDC logic (inserts, updates, deletes).

## Streaming
20. Use Auto Loader for incremental ingestion.
21. Stream data to Bronze with checkpoints.
22. Handle late data via watermarks.

## Optimization
23. Reduce shuffle by strategic repartitioning.
24. Use coalesce vs repartition properly.
25. Apply partitioning & bucketing strategies.

## ML + PySpark
26. Vectorize columns for ML.
27. Train/test split with seed-controlled randomness.
28. Build PySpark ML pipeline (RandomForest example).

## UDFs & Pandas UDFs
29. Create a Python UDF for masking PII.
30. Use Pandas UDFs for batch feature engineering.

## Advanced Use Cases
31. Pivot/unpivot datasets.
32. Explode complex structures.
33. Detect duplicates with windows.
34. Mask or hash sensitive fields.
35. Build chained transformations for KPIs.
36. Generate surrogate keys.

## Additional Prompts
37. Join multiple tables dynamically.
38. Validate schema against expected schema.
39. Implement ETL audit logging.
40. Generate profiling statistics.
41. Build reusable ETL function.
42. Use map/flatMap.
43. Conditional operations with when/otherwise.
44. Parse JSON strings into struct columns.
45. Rename 100+ columns dynamically.
46. Read Parquet, ORC, Avro from UC Volumes.
47. Write both streaming & batch output to Delta.
48. Implement event sessionization.
49. Sliding window aggregations.
50. PySpark unit test generation.
51. KPI calculations per region/time.
52. Split DataFrame into multiple DataFrames.
53. Retry logic with exponential backoff.
54. Broadcast join hints.
55. Detect null-heavy columns.
56. Detect schema drift.
57. Convert PySpark ↔ Pandas safely.
58. Modular ETL patterns.
59. Metadata-driven ETL generator.
60. Build historical rebuild pipelines.

---

# Section 2 — SQL Lakehouse Prompts (45)

## Table Creation & Loading
1. Create UC table with schema and constraints.
2. Insert sample records via VALUES.
3. Create external table using UC Volumes.

## Selects + Filtering
4. Select columns by substring match.
5. Convert column names to snake_case.
6. Replace NULLs using COALESCE.

## Joins
7. Write inner, left, right, full joins.
8. Join 3+ tables using aliases.

## Aggregations
9. SUM/AVG/MIN/MAX by region/date.
10. CASE WHEN aggregations.

## Window SQL
11. Rolling averages (7 days).
12. Rank customers by spend.

## Delta SQL
13. MERGE INTO (SCD upsert pattern).
14. Time travel using VERSION AS OF.
15. VACUUM operations.

## Optimization
16. OPTIMIZE ZORDER BY best practices.
17. ANALYZE TABLE COMPUTE STATISTICS.

## Transformations
18. Pivot data by month.
19. Unpivot via stack().
20. Explode JSON arrays.

## Governance
21. GRANT permissions.
22. Row-level policies.
23. Secure views.

## Analytics
24. MoM growth.
25. SCD Type 2 logic.

## Advanced SQL Prompts
26. Time-series modeling in SQL.
27. Generate surrogate primary keys.
28. Fuzzy matching with SOUNDEX.
29. SQL schema drift detection.
30. Table diff comparison.
31. Generate audit-trail queries.
32. Metadata-driven SQL templates.
33. Create dimension & fact models.
34. KPI generation logic.
35. Aggregate-ready marts for BI tools.
36. Compute churn metrics.
37. Create retention cohorts.
38. Multi-step transformations in SQL.
39. Recursive SQL patterns.
40. Materialized view creation.
41. SQL-based anomaly detection.
42. Parameterized SQL templates.
43. JSON parsing using SQL.
44. Geospatial SQL prompts.
45. Performance-optimized filter patterns.

---

# Section 3 — Delta Lake & Optimization Prompts (30)

1. Inspect Delta transaction logs.
2. Show Delta metadata (stats, files, partitions).
3. Optimize with ZORDER BY.
4. Auto-optimize and auto-compaction.
5. Incremental MERGE INTO.
6. CDC MERGE patterns.
7. Query Change Data Feed.
8. Schema evolution patterns.
9. Enforce Delta constraints.
10. Restore table via VERSION AS OF.
11. Advanced partition pruning.
12. Small-file compaction pipeline.
13. Multi-cluster write techniques.
14. Generate Delta constraints.
15. Advanced retention management.
16. Delta table performance dashboard queries.
17. Optimize tables for BI workloads.
18. Data skipping analysis.
19. File size tuning for ingestion tasks.
20. Bloom filter index usage.
21. Rewriting tables with V2 writer.
22. Migrate Parquet to Delta.
23. Merge performance troubleshooting.
24. Vacuuming patterns.
25. Concurrency control patterns.
26. Idempotent MERGE operations.
27. Delete + dedupe workflows.
28. Historical rebuild via Delta logs.
29. Delta CDC ingestion from Kafka.
30. Benchmarking Delta operations.

---

# Section 4 — Unity Catalog Prompts (35)

1. Create catalog + schema + table.
2. Create external UC Volume.
3. Managed vs external tables.
4. GRANT/REVOKE examples.
5. Column-level security implementation.
6. Row-level filters via policies.
7. Create UC Functions (Python/SQL).
8. Multi-env UC architecture design.
9. UC Model Registry use cases.
10. UC Vector Search index governance.
11. UC lineage visualization queries.
12. UC tags & metadata.
13. Secure compute and data isolation.
14. Cross-workspace data access.
15. Create service principals.
16. Unity Catalog audit logging.
17. Tokenization + masking strategies.
18. RBAC best practices.
19. Migrate Hive tables to UC.
20. Table-level versioning best practices.
21. Catalog-per-domain pattern.
22. Schema-per-product-line pattern.
23. Data sharing via Delta Sharing.
24. Access control troubleshooting.
25. Multi-cloud UC deployment strategy.
26. Object naming conventions.
27. Dev/Test/Prod UC separation.
28. UC migration workflows.
29. Unity Catalog CLI usage.
30. Validate UC permissions programmatically.
31. Fine-grained access via views.
32. Deny policies and ACL troubleshooting.
33. Cross-account sharing strategy.
34. Confidential compute patterns.
35. UC security hardening guide.

---

# Section 5 — Lakeflow / DLT Prompts (30)

1. Create Bronze/Silver/Gold DLT pipeline.
2. Add data quality expectations.
3. CDC ingestion with DLT.
4. SQL DLT transformation pipeline.
5. Schema evolution with DLT.
6. Auto Loader + DLT integration.
7. Modular DLT pipeline code.
8. DLT pipeline deployment via API.
9. DLT metrics extraction queries.
10. Time-based incremental ingestion.
11. Route bad data to quarantine table.
12. Orchestrate DLT with Workflows.
13. Trigger-based DLT jobs.
14. Multi-pipeline orchestration.
15. Dynamic DLT pipeline generation.
16. DLT lineage extraction.
17. DLT performance tuning.
18. Implement SCD2 with DLT.
19. Complex joins inside DLT.
20. Stateful DLT transformations.
21. Reprocessing pipeline design.
22. Ensure idempotent transformations.
23. Streaming + batch hybrid pipelines.
24. Multi-hop quality checks.
25. High-availability DLT patterns.
26. CBC ingestion for legacy systems.
27. Metadata-driven DLT generator.
28. Fault-tolerant DLT design.
29. Schema registry integration.
30. Multi-environment DLT workflows.

---

# Section 6 — Databricks AI Assistant Prompts (30)

## Coding
1. Optimize PySpark for performance.
2. Convert Python ETL to DLT.
3. Rewrite code using best practices.
4. Generate modular code templates.
5. Convert SQL to PySpark & vice versa.

## Debugging
6. Explain stack traces.
7. Propose PySpark fixes.
8. Fix schema mismatch issues.
9. Debug pipeline failures.
10. Identify performance bottlenecks.

## Documentation
11. Auto-generate pipeline documentation.
12. Create design docs for ETL.
13. Generate transformation lineage docs.
14. Write API docs for notebooks.

## More AI Assistant Prompts
15. Convert legacy jobs to Workflows.
16. Optimize SQL queries.
17. Suggest ZORDER columns.
18. Generate unit tests.
19. Build feature engineering code.
20. Generate MLflow tracking code.
21. Convert notebooks to modules.
22. Refactor code for readability.
23. Suggest logging improvements.
24. Create reusable helpers.
25. Build metadata-driven patterns.
26. Extract logic into functions.
27. Propose pipeline automation.
28. Assist with cluster sizing.
29. Propose CI/CD setup.
30. Generate data validation rules.

---

# Section 7 — MLflow + ML Engineering Prompts (30)

1. Create MLflow experiment.
2. Log params/metrics.
3. Log artifacts & plots.
4. Use MLflow Tracing for LLMs.
5. Register models in UC Registry.
6. Transition model stages.
7. Download & load models.
8. Create custom model signatures.
9. Serve models via Model Serving.
10. Monitor model latency.
11. Build PySpark ML pipelines.
12. sklearn MLflow integration.
13. Train/test split utilities.
14. Evaluate model drift.
15. Generate model cards.
16. Feature importance analysis.
17. Cross-validation automation.
18. Hyperparameter tuning.
19. Deploy inference pipelines.
20. Real-time inference design.
21. GPU-accelerated model serving.
22. Model lineage extraction.
23. Model rollback strategy.
24. Multi-model orchestration.
25. Automate retraining workflows.
26. Debug model failures.
27. Migration guide: legacy registry → UC.
28. Batch inference pipelines.
29. Online inference patterns.
30. ML observability dashboards.

---

# Section 8 — Feature Store Prompts (20)

1. Create Feature Table.
2. Offline feature lookup.
3. Online feature lookup.
4. Validate feature consistency.
5. Create point-in-time training sets.
6. Streaming feature pipelines.
7. Batch feature pipelines.
8. Feature monitoring metrics.
9. Feature schema validation.
10. Feature importance tracking.
11. Materialize feature views.
12. Join multiple feature tables.
13. Delete outdated features safely.
14. Update features incrementally.
15. Feature TTL strategy.
16. Model-to-feature lineage.
17. Feature versioning.
18. Online store performance tuning.
19. Metadata-driven feature creation.
20. Multi-environment feature store design.

---

# Section 9 — Mosaic AI / Model Serving Prompts (25)

1. Create serverless Model Serving endpoint.
2. Optimize inference with batching.
3. Set GPU/CPU autoscaling.
4. Build custom LLM routes.
5. Generate embedding API code.
6. Register LLM models in UC.
7. LLM fine-tuning workflows.
8. Prompt engineering examples.
9. Monitor LLM latency.
10. Prevent LLM hallucinations.
11. Implement guardrails for LLMs.
12. LLM cost monitoring with MLflow.
13. Multi-model fallback.
14. Create high-throughput inference pipeline.
15. Token usage analytics.
16. Compile models for optimized runtime.
17. Use quantization for speed.
18. Load-balancing inference endpoints.
19. Deploy multiple model versions.
20. Canary-release LLMs.
21. Integrate LLMs with RAG.
22. Build chatbot inference endpoints.
23. Build multimodal inference.
24. Secure model serving endpoints.
25. Production-grade LLM architecture design.

---

# Section 10 — Vector Search + RAG Prompts (35)

1. Create Vector Search index.
2. Generate embeddings.
3. Metadata-enriched search.
4. Hybrid ANN search.
5. Build complete RAG pipeline.
6. Chunking for optimal retrieval.
7. Implement cross-encoder re-ranking.
8. Real-time RAG for chatbots.
9. Filter retrieval via metadata.
10. Multi-hop retrieval logic.
11. Evaluate retrieval quality.
12. RAG hallucination detection.
13. LLM-driven search tuning.
14. Multi-index retrieval patterns.
15. Build structured RAG pipelines.
16. Use Delta Sync for vector tables.
17. Refresh embeddings incrementally.
18. RAG caching patterns.
19. Temporal-aware RAG retrieval.
20. Long-context RAG techniques.
21. Vector database troubleshooting.
22. ANN recall tuning.
23. Build knowledge-grounded LLMs.
24. Index sharding strategy.
25. Federated vector search.
26. Memory-efficient embeddings.
27. Compress embeddings.
28. Optimize embedding generation.
29. Bulk ingestion to index.
30. Retrieval monitoring patterns.
31. Reranking pipeline design.
32. Approximate nearest neighbor tuning.
33. Document scoring logic.
34. Query rewriting for better retrieval.
35. RAG system observability.

---

# Section 11 — AI Agent Development Prompts (25)

1. Build SQL-enabled agent with UC tools.
2. Create ReAct-style agent for pipelines.
3. Multi-agent collaboration patterns.
4. Add guardrails for safety.
5. Build agent with Python tools.
6. Create REST-calling agent.
7. Create LLM-powered ETL agent.
8. RAG-enabled agent patterns.
9. Tools for Data Engineering agents.
10. Tools for ML agents.
11. Tools for SQL optimization agents.
12. Debugging-focused agents.
13. Model governance agents.
14. Agent evaluation scoring.
15. Semantic search agent.
16. Monitoring and logging for agents.
17. LLM + Workflow orchestration agent.
18. Self-healing pipeline agent.
19. Schema drift resolution agent.
20. Secure data access agent.
21. Multi-tool calling agent prompts.
22. Planning prompts for complex tasks.
23. Chain-of-thought constrained agent prompts.
24. SQL-to-PySpark converting agent.
25. Agent for generating full project scaffolds.

---

# END OF DOCUMENT

