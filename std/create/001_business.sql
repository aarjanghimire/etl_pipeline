DROP TABLE if exists std.dim_business CASCADE;

CREATE TABLE std.dim_business(
	business_id varchar primary key,
	business_name varchar,
	address varchar,
	categories text[],
	city varchar,
	state varchar,
	review_count int,
	stars float
	);