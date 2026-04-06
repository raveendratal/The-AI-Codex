-- =============================================================
-- Dashboard SQL Templates
-- =============================================================

-- KPI 1: Revenue Trend (Daily)
CREATE OR REPLACE VIEW ${catalog}.gold.v_revenue_trend AS
SELECT
  date,
  SUM(revenue) AS total_revenue,
  SUM(revenue) - LAG(SUM(revenue)) OVER (ORDER BY date) AS revenue_change,
  COUNT(DISTINCT order_id) AS total_orders
FROM ${catalog}.gold.sales
GROUP BY date
ORDER BY date;

-- KPI 2: Customer Growth
CREATE OR REPLACE VIEW ${catalog}.gold.v_customer_growth AS
SELECT
  DATE_TRUNC('month', first_purchase_date) AS cohort_month,
  COUNT(DISTINCT customer_id) AS new_customers,
  SUM(COUNT(DISTINCT customer_id)) OVER (ORDER BY DATE_TRUNC('month', first_purchase_date)) AS cumulative_customers
FROM ${catalog}.gold.customers
GROUP BY DATE_TRUNC('month', first_purchase_date)
ORDER BY cohort_month;

-- KPI 3: Top Products
CREATE OR REPLACE VIEW ${catalog}.gold.v_top_products AS
SELECT
  product_name,
  SUM(quantity) AS total_sold,
  SUM(revenue) AS total_revenue,
  RANK() OVER (ORDER BY SUM(revenue) DESC) AS revenue_rank
FROM ${catalog}.gold.sales
GROUP BY product_name
ORDER BY total_revenue DESC
LIMIT 20;

-- KPI 4: Summary Card Metrics
CREATE OR REPLACE VIEW ${catalog}.gold.v_summary_metrics AS
SELECT
  SUM(revenue) AS total_revenue,
  COUNT(DISTINCT customer_id) AS total_customers,
  COUNT(DISTINCT order_id) AS total_orders,
  AVG(revenue) AS avg_order_value
FROM ${catalog}.gold.sales
WHERE date >= current_date() - INTERVAL 30 DAY;
