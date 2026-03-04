CREATE OR REPLACE TABLE events AS
SELECT * FROM read_parquet('data/processed/events_clean.parquet');