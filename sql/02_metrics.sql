-- Funnel metrics (daily)
CREATE OR REPLACE TABLE funnel_daily AS
SELECT
  event_date,
  COUNT(DISTINCT CASE WHEN event_type='view' THEN user_id END) AS viewers,
  COUNT(DISTINCT CASE WHEN event_type='cart' THEN user_id END) AS carters,
  COUNT(DISTINCT CASE WHEN event_type='purchase' THEN user_id END) AS purchasers,
  (purchasers * 1.0) / NULLIF(viewers, 0) AS view_to_purchase_rate
FROM events
GROUP BY 1
ORDER BY 1;

-- Retention cohorts: first_seen_week vs active_week
CREATE OR REPLACE TABLE retention_weekly AS
WITH first_seen AS (
  SELECT user_id, MIN(event_week) AS cohort_week
  FROM events
  GROUP BY 1
),
activity AS (
  SELECT user_id, event_week
  FROM events
  GROUP BY 1,2
)
SELECT
  f.cohort_week,
  a.event_week AS active_week,
  COUNT(DISTINCT a.user_id) AS active_users
FROM first_seen f
JOIN activity a USING(user_id)
GROUP BY 1,2
ORDER BY 1,2;