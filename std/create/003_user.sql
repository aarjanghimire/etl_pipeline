DROP TABLE IF EXISTS std.dim_user CASCADE;
CREATE table std.dim_user(
	user_id varchar primary key,
	username varchar,
	yelping_since timestamp,
	review_count int,
	average_stars float )