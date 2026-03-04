CREATE OR REPLACE TABLE user_week_counts AS
SELECT
  user_id,
  COUNT(DISTINCT event_week) AS active_weeks,
  MAX(CASE WHEN event_type='view' THEN 1 ELSE 0 END) AS used_view,
  MAX(CASE WHEN event_type='cart' THEN 1 ELSE 0 END) AS used_cart,
  MAX(CASE WHEN event_type='purchase' THEN 1 ELSE 0 END) AS used_purchase
FROM events
GROUP BY 1;

CREATE OR REPLACE TABLE adoption_retention AS
SELECT
  CASE WHEN used_view=1 THEN 'view' ELSE 'no_view' END AS feature,
  AVG(CASE WHEN active_weeks >= 2 THEN 1 ELSE 0 END) AS retention_rate,
  COUNT(*) AS users
FROM user_week_counts
GROUP BY 1

UNION ALL
SELECT
  CASE WHEN used_cart=1 THEN 'cart' ELSE 'no_cart' END AS feature,
  AVG(CASE WHEN active_weeks >= 2 THEN 1 ELSE 0 END) AS retention_rate,
  COUNT(*) AS users
FROM user_week_counts
GROUP BY 1

UNION ALL
SELECT
  CASE WHEN used_purchase=1 THEN 'purchase' ELSE 'no_purchase' END AS feature,
  AVG(CASE WHEN active_weeks >= 2 THEN 1 ELSE 0 END) AS retention_rate,
  COUNT(*) AS users
FROM user_week_counts
GROUP BY 1;