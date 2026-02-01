# NYC TLC Data Pipeline with Kestra, DuckDB, and AWS S3

This project implements an automated ETL pipeline that extracts New York City Taxi & Limousine Commission (TLC) data, converts it to highly optimized Parquet format, and loads it into an AWS S3 data lake.

## 🚀 Project Overview

The workflow is designed to handle large-scale CSV files efficiently within a **GitHub Codespaces** environment. It utilizes **Kestra** as the orchestrator and **DuckDB** for lightning-fast data transformation.

### Key Features
* **Dynamic Partitioning:** Processes data by taxi type (`yellow`, `green`) and year via user inputs.
* **Memory Efficiency:** Uses DuckDB to convert CSVs to Parquet, reducing file size by up to 80% before transmission.
* **Resource Management:** Implements a sequential `concurrencyLimit: 1` and automated storage purging to stay within Codespaces disk limits.
* **Secure Credential Management:** Utilizes Kestra's **KV Store** to handle AWS credentials and bucket names securely without hardcoding them in the YAML.

---

## 🛠️ Infrastructure & Setup

### 1. Orchestration
Kestra is deployed using Docker. You can find the configuration used for this setup here:
* **File:** [docker-compose.yml](../CourseWork/docker-compose.yaml)

### 2. Analytical Queries
Once the data is in S3, I use a standalone Python script with DuckDB to perform analytical queries directly on the S3 bucket to provide answers to the project questions.
* **Script:** [s3_duckdb_queries.py](./s3_query.py)

### 3. Security & KV Store
AWS credentials and global configurations are stored in **Kestra's Key-Value (KV) Store** to ensure security when pushing code to GitHub. The following keys are required:
* `AWS_ACCESS_KEY_ID`: Your IAM user access key.
* `AWS_SECRET_KEY_ID`: Your IAM user secret key.
* `bucket_name`: The target S3 bucket name.

---

## 🔄 Workflow Details



The workflow (`tlc_data_load`) follows these steps for every month selected in the input:

1.  **Variable Setup:** Dynamically generates file names and S3 paths based on the current loop iteration.
2.  **Extract:** Downloads the compressed `.csv.gz` from the GitHub source and decompresses it into a raw CSV.
    * **Precision Logging:** It includes a custom `du` + `awk` command to report the extracted file size with decimal precision (e.g., `128.3MB`) in the logs.
3.  **Transform (DuckDB):** Runs a Python script inside a `python:3.11-slim` Docker container to convert the CSV to **Parquet**. 
4.  **Load:** Uploads the final Parquet file to the specified S3 bucket. This is significantly more efficient for storage and downstream querying than traditional SQL inserts.
5.  **Purge:** Automatically triggers `PurgeCurrentExecutionFiles` after each month is processed to keep the GitHub Codespaces environment light and prevent disk space errors.

---

## 📊 Usage

1.  Import the YAML into your Kestra instance.
2.  Ensure your AWS credentials and bucket name are set in the **Kestra KV Store**.
3.  Execute the flow and select your desired `taxi` type, `year`, and `months`.
4.  Monitor the **Logs** for the `REPORT - Month X Size:` output to see real-time processing stats.

---

## 🗄️ Data Storage Structure
The data is organized in S3 using the following partition logic:
`s3://{bucket_name}/nyc-taxi/{taxi_type}/{year}/full/{file_name}.parquet`