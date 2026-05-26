# Data Stack ELT Pipeline

A production-grade Data Engineering pipeline that demonstrates automated data ingestion, orchestration, and cloud data warehousing using the Data Stack ecosystem.

## Architecture Overview
* **Data Source:** Custom Python ingestion script generating synthetic transactional market data (orders, regional currencies like AMD/GBP/EUR, platforms, and statuses).
* **Orchestration:** **Prefect** managing workflow execution, task dependencies, and state tracking.
* **Cloud Data Warehouse:** **Google BigQuery** serving as the centralized repository for raw data storage (`market_analytics_raw`).

## Tech Stack
* **Language:** Python
* **Orchestration:** Prefect
* **Storage:** Google BigQuery (Cloud Data Warehouse)
* **Data Manipulation:** Pandas

## Project Structure
* `scripts/etl_pipeline.py` - Core Python script containing Prefect flows and tasks for data generation and BigQuery loading.
* `gcp_creds.json` - Google Cloud Service Account credentials (secured and excluded via `.gitignore`).
* `.gitignore` - Safeguards sensitive infrastructure credentials and local cache files.
