---
name: document-intelligence
description: Parse documents, extract text from PDFs/images, and use SQL AI functions for intelligent data extraction.
---

# Document Intelligence Skill

## When to Use
Use for PDF parsing, OCR, document extraction, and AI-powered data analysis.

## SQL AI Functions

### Parse PDF Documents
```sql
-- Extract text from PDF files in a Volume
SELECT
  path,
  ai_parse_document(content, 'text') AS extracted_text
FROM read_files('/Volumes/main/raw/documents/', format => 'binaryFile')
WHERE path LIKE '%.pdf';
```

### Extract Structured Data from Documents
```sql
SELECT
  ai_extract(
    extracted_text,
    ARRAY('invoice_number', 'date', 'total_amount', 'vendor_name')
  ) AS extracted_fields
FROM documents;
```

### AI Classification
```sql
-- Classify documents by type
SELECT
  document_id,
  ai_classify(
    content,
    ARRAY('invoice', 'receipt', 'contract', 'report')
  ) AS document_type
FROM main.bronze.documents;
```

### AI Summarization
```sql
SELECT
  document_id,
  ai_summarize(content) AS summary
FROM main.bronze.documents;
```

### AI Sentiment Analysis
```sql
SELECT
  review_id,
  ai_analyze_sentiment(review_text) AS sentiment
FROM main.gold.customer_reviews;
```

## Python Document Processing
```python
import fitz  # PyMuPDF

def extract_pdf_text(pdf_path):
    """Extract text from a PDF file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Process PDFs from Volume
import os
volume_path = "/Volumes/main/raw/documents/"
for f in os.listdir(volume_path):
    if f.endswith(".pdf"):
        text = extract_pdf_text(os.path.join(volume_path, f))
        # Store in Delta table
```

## Best Practices
- Store raw documents in Unity Catalog Volumes
- Use `ai_parse_document` for PDF/image extraction
- Cache AI function results (they have token costs)
- Process large document batches in parallel
- Store extracted data in Silver layer for downstream use
