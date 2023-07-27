DROP TABLE fact.dim_user CASCADE;
CREATE table fact.dim_user(
	user_id varchar primary key,
	username varchar,
	yelping_since timestamp,
	review_count int,
	average_stars float )