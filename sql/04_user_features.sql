CREATE OR REPLACE TABLE user_features AS
WITH base AS (
  SELECT
    user_id,
    MIN(event_time) AS first_event_time,
    MAX(event_time) AS last_event_time,
    COUNT(*) AS total_events,
    COUNT(DISTINCT event_date) AS active_days,
    COUNT(DISTINCT session_id) AS sessions,
    COUNT(*) FILTER (WHERE event_type='view') AS views,
    COUNT(*) FILTER (WHERE event_type='cart') AS carts,
    COUNT(*) FILTER (WHERE event_type='purchase') AS purchases,
    AVG(price) FILTER (WHERE price IS NOT NULL) AS avg_price,
    SUM(price) FILTER (WHERE event_type='purchase' AND price IS NOT NULL) AS revenue
  FROM events
  GROUP BY 1
),
dataset_end AS (
  SELECT MAX(event_time) AS end_time FROM events
),
final AS (
  SELECT
    b.*,
    DATE_DIFF('day', b.first_event_time, b.last_event_time) AS lifecycle_days,
    DATE_DIFF('day', b.last_event_time, (SELECT end_time FROM dataset_end)) AS recency_days,
    (b.purchases * 1.0) / NULLIF(b.views, 0) AS view_to_purchase_rate,
    (b.carts * 1.0) / NULLIF(b.views, 0) AS view_to_cart_rate,
    (b.purchases * 1.0) / NULLIF(b.carts, 0) AS cart_to_purchase_rate,
    CASE WHEN DATE_DIFF('day', b.last_event_time, (SELECT end_time FROM dataset_end)) >= 14 THEN 1 ELSE 0 END AS churn
  FROM base b
)
SELECT * FROM final;