DROP TABLE IF EXISTS std.checkin;
CREATE TABLE std.dim_checkin(
business_id varchar references std.dim_business(business_id),
total_checkin int
);