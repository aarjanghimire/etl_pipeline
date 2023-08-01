DROP TABLE IF EXISTS raw.business;
CREATE TABLE raw.business (
    name VARCHAR,
    city VARCHAR,
    address VARCHAR,
    categories VARCHAR,
    hours VARCHAR,
    review_count VARCHAR,
    postal_code VARCHAR,
    stars VARCHAR,
    state VARCHAR,
    is_open VARCHAR,
    latitude VARCHAR,
    business_id VARCHAR,
    longitude VARCHAR,
    attributes JSON
)