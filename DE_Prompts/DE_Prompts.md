Below is a **mega-collection of 150 detailed, production-grade prompts** for **Data Engineering, PySpark, Spark SQL, Data Modeling, and Lakehouse Design**.
These are written for **Databricks AI Assistant, ChatGPT, Claude, Gemini, Qwen, Grok, Perplexity**, or any LLM used for engineering work.

---

# # ✅ **150 Detailed Developer Prompts for Data Engineering, PySpark, Spark SQL & Data Modeling**

---

# # **SECTION A — PySpark Prompts (50 Prompts)**

High-quality prompts for transformations, optimization, ETL pipelines, and performance tuning.

---

## **1. DataFrame Creation & Schema Handling**

1. “Generate PySpark code that creates a DataFrame with 10 sample rows for a retail orders dataset including order_id, customer_id, product_id, quantity, price, order_ts.”
2. “Create a PySpark schema for a nested JSON file containing customer → orders → items arrays. Show sample code to read it from a UC Volume.”
3. “Write PySpark code to infer schema from JSON files, store it, and validate new batches against the stored schema.”
4. “Create a reusable PySpark utility to print schema differences between two DataFrames.”

---

## **2. Transformations**

5. “Write PySpark code to normalize all column names to snake_case for a given DataFrame.”
6. “Transform string date columns into DATE type with multiple fallback formats.”
7. “Clean text columns by trimming whitespace, removing special characters, and lowercasing values.”
8. “Convert complex nested JSON columns into normalized Bronze, Silver, Gold layers using explode() and selectExpr().”
9. “Write a robust PySpark pipeline that handles missing values, null replacement, type casting, and data validations.”

---

## **3. Aggregations & Window Functions**

10. “Create PySpark code that calculates average spend per customer per month using window functions.”
11. “Find the top 3 selling products per region using dense_rank().”
12. “Compute rolling 7-day averages for website traffic using PySpark time windows.”
13. “Calculate session durations using lead() and lag() based on event timestamps.”
14. “Detect anomalies in financial transactions using z-score computed in a window function.”

---

## **4. Joins & Keys**

15. “Generate examples of inner, left, right, full, semi, and anti joins with business explanations.”
16. “Optimize joins between a large fact table and small dimension table using broadcast join.”
17. “Implement skew join mitigation using salting techniques.”
18. “Write PySpark code that joins 5 tables dynamically based on metadata configuration.”
19. “Show how to detect unintended cartesian joins and prevent them.”

---

## **5. Performance Optimization**

20. “Rewrite slow PySpark code to eliminate unnecessary shuffles and improve performance.”
21. “Explain when to use repartition() vs coalesce() and provide PySpark examples.”
22. “Implement partition pruning and predicate pushdown optimization with Delta tables.”
23. “Show PySpark code that benchmarks execution time of various transformations.”
24. “Convert a DataFrame with many small files into optimized partitions using repartitionByRange.”

---

## **6. Streaming & Auto Loader**

25. “Write PySpark Structured Streaming job to ingest JSON logs using Auto Loader with cloudFiles options.”
26. “Implement watermark + windowed aggregation for streaming session data.”
27. “Create a streaming Bronze → Silver → Gold pipeline with checkpointing and deduplication.”
28. “Show how to merge streaming CDC records into a Delta table in real time.”
29. “Create a fault-tolerant PySpark streaming job with retries and recovery logic.”

---

## **7. UDFs & Pandas UDFs**

30. “Write a Python UDF for masking PII fields such as email and phone.”
31. “Create a Pandas UDF that calculates rolling metrics for finance datasets.”
32. “Convert a UDF into native PySpark functions for performance optimization.”
33. “Show how to handle serialization errors in UDFs.”

---

## **8. ETL Frameworks & Utilities**

34. “Generate metadata-driven PySpark ETL framework with config JSON file.”
35. “Write PySpark code to implement SCD Type 2 logic using MERGE INTO.”
36. “Build a multi-table ingestion framework using Auto Loader + dynamic schema.”
37. “Implement standard audit columns (insert_ts, update_ts, job_id) in all pipelines.”
38. “Extract column-level statistics (null %, cardinality, skew) for Data Quality reporting.”

---

## **9. Advanced Scenarios**

39. “Convert nested JSON attributes into Delta tables with correct data types and lineage logging.”
40. “Write PySpark code to perform union of DataFrames with mismatched schemas.”
41. “Implement PySpark logic for detecting duplicates based on composite keys.”
42. “Dynamically flatten complex schema structures using recursion.”
43. “Write PySpark logic to create synthetic test data for large workloads.”
44. “Implement business rules validation with pass/fail/quarantine outputs.”
45. “Create reusable logger class for PySpark ETL jobs.”
46. “Write PySpark logic to detect and correct timezone inconsistencies.”
47. “Build delta-based incremental load pipeline using file metadata.”
48. “Compute survival analysis metrics for churn prediction using PySpark.”
49. “Write PySpark code that reads 300+ files in parallel with optimized partitioning.”
50. “Generate PySpark unit tests using pytest + chispa.”

---

# # **SECTION B — Spark SQL Prompts (50 Prompts)**

---

## **10. SQL Table DDLs**

51. “Generate CREATE TABLE SQL for a normalized retail schema with constraints and comments.”
52. “Create a unified SQL DDL standard for enterprise Lakehouse tables.”
53. “Write SQL to create a Delta external table on a UC Volume.”

---

## **11. SQL Transformations**

54. “Write SQL to remove duplicate rows based on composite keys.”
55. “SQL to pivot monthly sales by category and region.”
56. “Unpivot 12 month columns into key/value structure.”
57. “Parse and flatten a JSON column into separate table columns.”

---

## **12. Joins, Filters, & Aggregations**

58. “Optimize SQL join between fact table (200M rows) and dimension table (1k rows).”
59. “Write SQL to calculate MoM, QoQ, YTD metrics.”
60. “SQL for window-based sessionization.”
61. “SQL to compute ABC classification by revenue contribution.”

---

## **13. Delta Lake SQL**

62. “Create SQL MERGE pattern for SCD Type 2.”
63. “Perform Delta time travel using VERSION AS OF.”
64. “Generate SQL to ZORDER a large table on customer_id and date.”
65. “Show SQL to VACUUM tables safely with retention checks.”

---

## **14. Analytical SQL**

66. “Compute RFM (Recency, Frequency, Monetary) metrics using SQL.”
67. “Detect anomalies in data using statistical SQL functions.”
68. “Perform cohort analysis by signup month.”
69. “Compute customer lifetime value using window functions.”

---

## **15. Governance SQL**

70. “Create dynamic row-level security view in SQL.”
71. “Apply column-level masking using secure functions.”
72. “SQL script to check table-level access and role permissions.”

---

## **16. Advanced SQL Prompts**

73. “Generate SQL for log parsing into structured format.”
74. “Build recursive SQL queries for hierarchical data.”
75. “Compute geographical distance using SQL haversine formula.”
76. “Top-K ranking per partition using ROW_NUMBER.”
77. “SQL differencing queries to compare two tables.”
78. “SQL to compute churn and retention curves.”
79. “Dimensional model query patterns for BI tools.”
80. “Full SQL script for data quality validation checks.”

---

# # **SECTION C — Data Engineering Prompts (30 Prompts)**

---

## **17. DE Architecture**

81. “Design a Bronze/Silver/Gold Lakehouse pipeline for real-time e-commerce data.”
82. “Propose an enterprise ingestion architecture with Auto Loader + DLT + Workflows.”
83. “Define SCD, CDC, UPSERT, late-arriving data strategies for Lakehouse.”

---

## **18. Pipeline Orchestration**

84. “Generate Databricks Workflow DAG for 8-stage ETL pipeline.”
85. “Create a CI/CD plan for DE pipelines using Git & Databricks Repos.”
86. “Design multi-environment (dev/qa/prod) Lakehouse release lifecycle.”

---

## **19. Data Quality & Observability**

87. “Build DQ framework with rules, thresholds, metrics & alerts.”
88. “Implement anomaly detection on tables using automated statistical checks.”
89. “Generate column profiling pipeline for 1,000+ tables.”

---

## **20. Metadata-Driven Engineering**

90. “Create dataset inventory metadata table template.”
91. “Build a metadata-driven ingestion engine with PySpark.”
92. “Design lineage-aware ETL framework using Delta logs.”

---

## **21. Performance & Cost Optimization**

93. “Optimize compute cost for Auto Loader streaming ingestion.”
94. “Suggest ZORDER + clustering strategy for high-cardinality tables.”
95. “Design storage layout for multi-TB tables for BI query performance.”

---

## **22. CDC / Real-Time DE Scenarios**

96. “Create design for Kafka → Auto Loader → Bronze → Silver CDC pipeline.”
97. “Generate watermarking and deduplication strategy for event streams.”
98. “Implement UPSERT logic for CDC records with MERGE.”

---

# # **SECTION D — Data Modeling Prompts (20 Prompts)**

---

## **23. Dimensional Modeling**

99. “Design a star schema for e-commerce analytics with fact tables + dimensions.”
100. “Model an SCD Type 2 dimension for customer profiles.”
101. “Create a dimensional model for financial transactions with slowly changing attributes.”

---

## **24. Data Vault Modeling**

102. “Generate Hubs, Links, Satellites for a Data Vault 2.0 design.”
103. “Convert a transactional schema into a raw vault + business vault model.”
104. “Design PIT (Point-In-Time) tables for historical queries.”

---

## **25. Lakehouse Modeling**

105. “Model Bronze → Silver → Gold transformations for clickstream analytics.”
106. “Design Gold-level semantic models for BI with aggregates & serving layers.”
107. “Create modeling guidelines for Delta Lake tables including naming, partitioning, ZORDER.”

---

## **26. Consumer Layer Modeling**

108. “Design a holistic semantic layer for Qlik/Power BI/Looker on top of Gold tables.”
109. “Create KPI definitions and their SQL implementations.”
110. “Define data contracts between DE & BI teams.”

 
