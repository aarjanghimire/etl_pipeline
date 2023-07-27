DROP TABLE IF EXISTS review;
CREATE TABLE review (
    review_id VARCHAR,
    user_id VARCHAR,
    business_id VARCHAR,
    stars VARCHAR,
    useful VARCHAR,
    funny VARCHAR,
    cool VARCHAR,
    text TEXT,
    date VARCHAR
);
