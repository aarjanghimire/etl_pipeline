INSERT INTO std.fact_review (
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
FROM raw.review
WHERE user_id IN (SELECT user_id FROM std.dim_user);