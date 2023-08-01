DROP table IF EXISTS std.fact_review;
CREATE TABLE std.fact_review(
	review_id varchar primary key,
	business_id varchar references std.dim_business(business_id),
	user_id varchar references std.dim_user(user_id),
	stars float,
	useful int,
	funny int,
  	cool int,
	date timestamp)