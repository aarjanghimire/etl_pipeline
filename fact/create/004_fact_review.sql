DROP table fact.fact_review;
CREATE TABLE fact.fact_review(
	review_id varchar primary key,
	business_id varchar references fact.dim_business(business_id),
	user_id varchar references fact.dim_user(user_id),
	stars float,
	useful int,
	funny int,
  	cool int,
	date timestamp)