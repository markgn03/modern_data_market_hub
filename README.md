# Market Analytics Data Pipeline

## Overview
This repository contains an end-to-end ELT data pipeline simulating a modern data stack. It processes multi-currency market transactions, standardizes financial metrics to a base currency (EUR), and applies business logic to categorize transactions.

## Architecture
* Data Warehouse: DuckDB
* Transformation: dbt (Data Build Tool)
* Orchestration & Ingestion: Python

## Project Structure
* `scripts/`: Python scripts for data ingestion and pipeline orchestration
* `models/staging/`: dbt models for data cleansing and type casting
* `models/marts/`: Final business-level aggregations and enriched data marts
* `tests/`: Automated data quality checks defined in dbt

## Setup & Execution
python -m venv venv
venv\Scripts\activate
pip install duckdb pandas dbt-duckdb

python scripts/etl_pipeline.py

python scripts/show_data.py