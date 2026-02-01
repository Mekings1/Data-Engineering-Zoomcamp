import duckdb

# Connect to DuckDB in-memory database
con = duckdb.connect()


# Install and load the httpfs extension to enable S3 access
con.execute("""
INSTALL httpfs;
LOAD httpfs;
SET s3_region='eu-west-2';
""")

# with our parquet files in S3 we can now run SQL queries directly on them
# Query to count the number of trips in the yellow taxi 2020 full dataset
con.sql("""
SELECT COUNT(*) AS trips
FROM 's3://kestra-tlc-data/nyc-taxi/yellow/2020/full/*.parquet'
""").show()


# Query to count the number of trips in the green taxi 2020 full dataset
con.sql("""
SELECT COUNT(*) AS trips
FROM 's3://kestra-tlc-data/nyc-taxi/green/2020/full/*.parquet'
""").show()


# Query to count the number of trips in the yellow taxi March 2021 dataset
con.sql("""
SELECT COUNT(*) AS trips
FROM 's3://kestra-tlc-data/nyc-taxi/yellow/2021/full/yellow_tripdata_2021-03.csv.parquet'
""").show()