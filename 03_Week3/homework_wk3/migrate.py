import duckdb

# Connect to DuckDB in-memory database
con = duckdb.connect()

# Install and load the httpfs extension to enable S3 access
con.execute("""
INSTALL httpfs;
LOAD httpfs;
SET s3_region='eu-west-2';
""")

Loop over the required months on NYC taxi site and copy them to s3
BASE_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-"
months = ["01", "02", "03", "04", "05", "06"]
BASE_S3_URL = "s3://kestra-tlc-data/nyc-taxi/yellow/2024/full/"

for month in months:
    url = f"{BASE_URL}{month}.parquet"
    s3_url = f"{BASE_S3_URL}yellow_tripdata_2024-{month}.parquet"
    con.execute(f"COPY (SELECT * FROM '{url}') TO '{s3_url}' (FORMAT 'parquet')")


