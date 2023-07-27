INSERT INTO fact.dim_user(
	user_id ,
	username ,
	yelping_since ,
	review_count ,
	average_stars )
SELECT 
	user_id,
	name,
	yelping_since::timestamp,
	review_count::int,
	average_stars::float
FROM user_biz;