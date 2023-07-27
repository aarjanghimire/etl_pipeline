INSERT INTO fact.fact_review (
  review_id,
  business_id,
  user_id,
  stars,
  useful,
  funny,
  cool,
  date
)
SELECT 
  review_id,
  business_id,
  user_id,
  stars::float,
  useful::int,
  funny::int,
  cool::int,
  date::timestamp
FROM review
WHERE user_id IN (SELECT user_id FROM fact.dim_user);