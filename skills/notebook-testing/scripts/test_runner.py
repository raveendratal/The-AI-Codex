"""
Notebook Test Runner
Utilities for running data validation tests on Databricks.
"""

from datetime import datetime


class DataTestSuite:
    """A simple test suite for data validation."""

    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.results = []

    def assert_no_nulls(self, df, columns, test_name=None):
        """Check that specified columns have no null values."""
        for col in columns:
            null_count = df.filter(f"`{col}` IS NULL").count()
            self.results.append({
                "test": test_name or f"no_nulls_{col}",
                "status": "PASS" if null_count == 0 else "FAIL",
                "detail": f"{null_count} nulls found in {col}",
                "timestamp": datetime.now().isoformat()
            })

    def assert_unique(self, df, columns, test_name=None):
        """Check uniqueness on specified columns."""
        total = df.count()
        distinct = df.select(columns).distinct().count()
        dupes = total - distinct
        self.results.append({
            "test": test_name or f"unique_{'_'.join(columns)}",
            "status": "PASS" if dupes == 0 else "FAIL",
            "detail": f"{dupes} duplicates found",
            "timestamp": datetime.now().isoformat()
        })

    def assert_row_count(self, df, min_rows, max_rows=None, test_name=None):
        """Check row count within expected range."""
        count = df.count()
        passed = count >= min_rows and (max_rows is None or count <= max_rows)
        self.results.append({
            "test": test_name or "row_count",
            "status": "PASS" if passed else "FAIL",
            "detail": f"Count: {count} (expected: {min_rows}-{max_rows or 'inf'})",
            "timestamp": datetime.now().isoformat()
        })

    def assert_values_in_set(self, df, column, valid_values, test_name=None):
        """Check that all values in a column are within an expected set."""
        invalid = df.filter(~df[column].isin(valid_values)).count()
        self.results.append({
            "test": test_name or f"valid_values_{column}",
            "status": "PASS" if invalid == 0 else "FAIL",
            "detail": f"{invalid} invalid values in {column}",
            "timestamp": datetime.now().isoformat()
        })

    def assert_referential_integrity(self, child_df, parent_df, child_key, parent_key, test_name=None):
        """Check that all child keys exist in parent."""
        orphans = child_df.join(parent_df, child_df[child_key] == parent_df[parent_key], "left_anti").count()
        self.results.append({
            "test": test_name or f"ref_integrity_{child_key}",
            "status": "PASS" if orphans == 0 else "FAIL",
            "detail": f"{orphans} orphan records",
            "timestamp": datetime.now().isoformat()
        })

    def summary(self):
        """Return test summary."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r["status"] == "PASS")
        failed = total - passed
        return {
            "suite": self.suite_name,
            "total": total,
            "passed": passed,
            "failed": failed,
            "pass_rate": f"{passed/total*100:.1f}%" if total > 0 else "N/A",
            "results": self.results
        }

    def to_dataframe(self, spark):
        """Convert results to a Spark DataFrame."""
        return spark.createDataFrame(self.results)


if __name__ == "__main__":
    # Example usage
    suite = DataTestSuite("Silver Orders Validation")
    orders = spark.table("main.silver.orders")

    suite.assert_no_nulls(orders, ["order_id", "customer_id"])
    suite.assert_unique(orders, ["order_id"])
    suite.assert_row_count(orders, min_rows=100)

    summary = suite.summary()
    print(f"Tests: {summary['total']} | Passed: {summary['passed']} | Failed: {summary['failed']}")
    display(suite.to_dataframe(spark))
