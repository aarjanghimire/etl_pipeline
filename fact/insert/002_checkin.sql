INSERT INTO fact.checkin(
    business_id, 
    total_checkin
)

SELECT 
    BUSINESS_ID,
    LENGTH(date) - LENGTH(REPLACE(date, ', ', '')) + 1 AS date_count

FROM checkin;