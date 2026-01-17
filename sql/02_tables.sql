CREATE TABLE raw.post (
    post_id SERIAL PRIMARY KEY,
    title VARCHAR(500),
    created_on TIMESTAMPTZ NOT NULL
)