import os
import subprocess
import duckdb
import pandas as pd


def load_raw_data(db_path):
    conn = duckdb.connect(db_path)

    transactions_data = [
        {"transaction_id": 1, "transaction_date": "2026-05-26", "currency": "EUR", "gross_amount": 150.00, "device_type": "Desktop"},
        {"transaction_id": 2, "transaction_date": "2026-05-26", "currency": "USD", "gross_amount": 200.00, "device_type": "Mobile"},
        {"transaction_id": 3, "transaction_date": "2026-05-26", "currency": "USD", "gross_amount": 50.00, "device_type": "Mobile"}
    ]
    df_transactions = pd.DataFrame(transactions_data)
    conn.execute("create or replace table raw_transactions_stage as select * from df_transactions")

    rates_data = [
        {"rate_date": "2026-05-26", "currency": "EUR", "exchange_rate": 1.00},
        {"rate_date": "2026-05-26", "currency": "USD", "exchange_rate": 0.92}
    ]
    df_rates = pd.DataFrame(rates_data)
    conn.execute("create or replace table raw_rates_stage as select * from df_rates")

    conn.close()


def run_dbt():
    result_run = subprocess.run(["dbt", "run"], capture_output=True, text=True)
    print(result_run.stdout)
    if result_run.returncode != 0:
        print(result_run.stderr)
        raise Exception("dbt run failed")

    result_test = subprocess.run(["dbt", "test"], capture_output=True, text=True)
    print(result_test.stdout)
    if result_test.returncode != 0:
        print(result_test.stderr)
        raise Exception("dbt test failed")


if __name__ == "__main__":
    db_file = "market_analytics.duckdb"
    load_raw_data(db_file)
    run_dbt()