import duckdb

# Connect to DuckDB in-memory database
con = duckdb.connect()

# Install and load the httpfs extension to enable S3 access
con.execute("""
INSTALL httpfs;
LOAD httpfs;
SET s3_region='eu-west-2';
""")

# Question 1. Counting records
# What is count of records for the 2024 Yellow Taxi Data?
con.sql("""
SELECT COUNT(*) AS trips
FROM 's3://kestra-tlc-data/nyc-taxi/yellow/2024/full/*.parquet';
""").show()

# Question 4. Counting zero fare trips
# How many records have a fare_amount of 0?
con.sql("""
SELECT COUNT(*)
FROM 's3://kestra-tlc-data/nyc-taxi/yellow/2024/full/*.parquet'
WHERE fare_amount = 0;
""").show()