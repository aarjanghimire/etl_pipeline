DROP TABLE fact.dim_business CASCADE;
CREATE TABLE fact.dim_business(
	business_id varchar primary key,
	business_name varchar,
	address varchar,
	categories text[],
	city varchar,
	state varchar,
	review_count int,
	stars float
	);