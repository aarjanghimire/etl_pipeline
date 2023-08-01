INSERT INTO std.dim_business(
	business_id ,
	business_name ,
	address ,
	categories ,
	city ,
	state ,
	review_count ,
	stars )
SELECT 
	business_id,
	name,
	address,
	string_to_array(categories, ',') as categories,
	city,
	state,
	review_count::integer,
	stars:: float
from raw.business;