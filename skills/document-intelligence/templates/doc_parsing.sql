-- =============================================================
-- Document Intelligence SQL Templates
-- =============================================================

-- TEMPLATE 1: Ingest documents from Volume
CREATE OR REPLACE TABLE ${catalog}.bronze.documents AS
SELECT
  path,
  length,
  modificationTime,
  content
FROM read_files(
  '${volume_path}',
  format => 'binaryFile'
);

-- TEMPLATE 2: Extract text from PDFs
CREATE OR REPLACE TABLE ${catalog}.silver.document_text AS
SELECT
  path,
  ai_parse_document(content, 'text') AS extracted_text,
  current_timestamp() AS processed_at
FROM ${catalog}.bronze.documents
WHERE path LIKE '%.pdf';

-- TEMPLATE 3: Extract structured fields
CREATE OR REPLACE TABLE ${catalog}.silver.document_fields AS
SELECT
  path,
  ai_extract(
    extracted_text,
    ARRAY(${field_names})  -- e.g., 'invoice_number', 'date', 'amount'
  ) AS fields,
  current_timestamp() AS extracted_at
FROM ${catalog}.silver.document_text;

-- TEMPLATE 4: Classify documents
CREATE OR REPLACE TABLE ${catalog}.silver.document_classified AS
SELECT
  path,
  ai_classify(
    extracted_text,
    ARRAY(${categories})  -- e.g., 'invoice', 'receipt', 'contract'
  ) AS doc_type,
  current_timestamp() AS classified_at
FROM ${catalog}.silver.document_text;

-- TEMPLATE 5: Summarize documents
CREATE OR REPLACE TABLE ${catalog}.gold.document_summaries AS
SELECT
  path,
  doc_type,
  ai_summarize(extracted_text) AS summary,
  current_timestamp() AS summarized_at
FROM ${catalog}.silver.document_classified;
