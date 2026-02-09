# Module 3 — Data Warehousing (Homework)

This project contains my solution for **Module 3: Data Warehousing** of the Data Engineering Zoomcamp by DataTalksClub.

The goal of this module was to demonstrate how large analytical datasets can be stored, queried, and optimized using cloud-based data warehousing tools. While the official examples used Google Cloud Storage and BigQuery, this implementation achieves similar results using **Amazon S3 and DuckDB**.

---

## 📌 Objective

* Ingest remote Parquet datasets
* Store them in cloud object storage
* Query them efficiently using an analytical engine
* Demonstrate cost-efficient and scalable data warehousing principles

---

## 🏗️ Architecture Overview

This homework implements a lightweight **lakehouse-style workflow**:

1. Remote Parquet Sources
2. Amazon S3 (Object Storage)
3. DuckDB (Analytical Query Engine)

Data is queried directly from Parquet files stored in S3 without loading it into a traditional database.

```
Remote Parquet → S3 → DuckDB Queries
```

---

## ⚙️ Workflow

### Step 1: Ingest Parquet Files

* Remote Parquet files are ingested directly into S3
* Local downloads are skipped to reduce storage usage
* File paths are organized by year and month
* [Ingestion Script](./migrate.py)

### Step 2: Query with DuckDB

* DuckDB is used to read Parquet files directly from S3
* Queries are executed using DuckDB’s vectorized and columnar execution engine
* No dedicated database server is required
* [Query Script](./queries.py)

---

## 🚀 Key Technologies

* **Amazon S3** — Object storage for Parquet files
* **DuckDB** — In-process analytical database engine
* **Parquet** — Columnar storage format for analytics
* **Python** — Orchestration and scripting

---

## ✅ Key Features

* Direct querying of Parquet files from cloud storage
* Incremental, memory-efficient data processing
* No heavy database setup
* Cost-efficient storage and compute
* Scalable for large analytical workloads

---


## 💡 Why This Approach

This implementation demonstrates that modern data warehousing principles can be applied without relying on heavyweight cloud platforms.

Benefits include:

* Lower infrastructure cost
* Simpler deployment
* Faster experimentation
* Direct analytics on object storage

This approach reflects a practical, cloud-agnostic data engineering workflow.


