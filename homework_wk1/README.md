# Docker, SQL, and Terraform Homework

This folder contains the solutions for the homework on Docker, SQL, and Terraform.  
The files, scripts, and commands used to solve the homework are included here.  

Where answers involve shell or SQL commands, they are documented directly in this README.

---

## Question 1: Understanding Docker Images

**Task:** Run `python:3.13` Docker image and use `bash` as entrypoint.  
Determine the version of `pip` in the image.

**Command used:**

```bash
docker run -it --entrypoint=bash python:3.13
pip --version
```

## Question 2: Understanding Docker networking and docker-compose

**Task:** Given the following`docker-compose.yaml`, what is the `hostname` and `port` that pgadmin should use to connect to the postgres database?
``` yaml
services:
  db:
    container_name: postgres
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```
**Command used:**
```bash
cd homework_wk1 
docker compose up
```
**Answer:** `postgres:5432` and `db:5432`   
**Explanation** Inside Docker Compose, containers talk to each other over the internal Docker network, not via localhost or the published host port.


## Question 3: Counting short trips

**Task:** For the trips in November 2025 (lpep_pickup_datetime between '2025-11-01' and '2025-12-01', exclusive of the upper bound), how many trips had a trip_distance of less than or equal to 1 mile?        
<br>
**N/B** In this section the [Notebook](ingestion.ipynb) was used to extract and load the dataset into postgres container and answers are queried from the `pgAdmin` interface.

**Answer implemented in script:** [green taxi queries](queries.sql)

## Question 4: Longest trip for each day

**Task:** Which was the pick up day with the longest trip distance? Only consider trips with trip_distance less than 100 miles (to exclude data errors).

**Answer implemented in script:** [green taxi queries](queries.sql)

## Question 5: Biggest pickup zone

**Task:** Which was the pickup zone with the largest total_amount (sum of all trips) on November 18th, 2025?

**Answer implemented in script:** [green taxi queries](queries.sql)

## Question 6: Biggest tip

**Task:** For the passengers picked up in the zone named "East Harlem North" in November 2025, which was the drop off zone that had the largest tip?

**Answer implemented in script:** [green taxi queries](queries.sql)

## Question 7: Terraform

## AWS Authentication

Before running Terraform, the AWS environment was configured locally using the AWS CLI.
This step ensures Terraform can authenticate with AWS and create resources using the correct credentials and region.

```bash
aws configure
```
Terraform automatically reads these credentials from the AWS CLI configuration, so no credentials are hardcoded in the Terraform files or committed to GitHub.

Once the AWS CLI was configured, Terraform commands were executed using the existing Terraform files in this folder [Terraform Project](../Week%201/Terraform/).  
``` bash 
terraform init
terraform plan
terraform apply
terraform destroy
```

