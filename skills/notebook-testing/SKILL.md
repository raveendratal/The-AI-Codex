---
name: notebook-testing
description: Implement unit tests, integration tests, and data validation tests for Databricks notebooks and pipelines.
---

# Notebook Testing Skill

## When to Use
Use for validating notebook logic, data transformations, and pipeline outputs.

## Test Types
| Type | Scope | Tools |
|------|-------|---------|
| Unit | Functions, UDFs | pytest, unittest |
| Integration | End-to-end pipeline | Nutter, dbx |
| Data Validation | Output correctness | Great Expectations, custom |

## Unit Testing with pytest
```python
# test_transforms.py
import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import *

@pytest.fixture(scope="session")
def spark():
    return SparkSession.builder.master("local").getOrCreate()

def test_dedup_removes_duplicates(spark):
    data = [(1, "a"), (1, "a"), (2, "b")]
    df = spark.createDataFrame(data, ["id", "val"])
    result = df.dropDuplicates()
    assert result.count() == 2

def test_null_filter(spark):
    data = [(1, "a"), (2, None), (3, "c")]
    df = spark.createDataFrame(data, ["id", "val"])
    result = df.filter(df.val.isNotNull())
    assert result.count() == 2
```

## Data Assertion Helpers
```python
def assert_no_nulls(df, columns):
    """Assert no null values in specified columns."""
    for col in columns:
        null_count = df.filter(f"{col} IS NULL").count()
        assert null_count == 0, f"Found {null_count} nulls in {col}"

def assert_unique(df, columns):
    """Assert uniqueness on specified columns."""
    total = df.count()
    distinct = df.select(columns).distinct().count()
    assert total == distinct, f"Found {total - distinct} duplicates"

def assert_row_count(df, min_rows, max_rows=None):
    """Assert row count within expected range."""
    count = df.count()
    assert count >= min_rows, f"Expected >= {min_rows} rows, got {count}"
    if max_rows:
        assert count <= max_rows, f"Expected <= {max_rows} rows, got {count}"
```

## Integration Testing with Nutter
```python
from runtime.nutterfixture import NutterFixture

class TestSilverTransform(NutterFixture):
    def assertion_silver_not_empty(self):
        df = spark.table("main.silver.orders")
        assert df.count() > 0

    def assertion_no_nulls_in_pk(self):
        df = spark.table("main.silver.orders")
        assert df.filter("order_id IS NULL").count() == 0

result = TestSilverTransform().execute_tests()
print(result.to_string())
```

## Best Practices
- Test transformations with small, known datasets
- Run tests before deploying to production
- Include negative test cases
- Automate tests in CI/CD pipeline
- Use temporary tables for test isolation
