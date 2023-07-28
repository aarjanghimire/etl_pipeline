DROP TABLE IF EXISTS fact.checkin;
CREATE TABLE fact.checkin(
business_id varchar refrences fact.business(business_id),
total_checkin int
);