import os
import random
from datetime import datetime, timedelta
import pandas as pd
from google.cloud import bigquery
from prefect import task, flow

@task
def generate_market_data(num_rows=1500):
    currencies = ["EUR", "GBP", "AMD"]
    categories = ["Electronics", "Apparel", "Home", "Beauty", "Sports"]
    platforms = ["Web", "iOS", "Android"]
    
    start_date = datetime.now() - timedelta(days=30)
    
    data = []
    for i in range(num_rows):
        order_id = f"ORD-{100000 + i}"
        timestamp = start_date + timedelta(
            days=random.randint(0, 30),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        category = random.choice(categories)
        platform = random.choice(platforms)
        currency = random.choice(currencies)
        
        if currency == "EUR":
            price = round(random.uniform(10.0, 500.0), 2)
        elif currency == "GBP":
            price = round(random.uniform(8.0, 420.0), 2)
        else:
            price = round(random.uniform(4000.0, 200000.0), 2)
            
        status = "Returned" if random.random() < 0.12 else "Completed"
        
        data.append([order_id, timestamp, category, price, currency, status, platform])
        
    df = pd.DataFrame(data, columns=[
        "order_id", "timestamp", "category", "amount", "currency", "status", "platform"
    ])
    return df

@task
def generate_currency_rates():
    start_date = datetime.now() - timedelta(days=35)
    data = []
    for i in range(40):
        current_date = (start_date + timedelta(days=i)).date()
        data.append([current_date, "EUR", 1.0])
        data.append([current_date, "GBP", round(random.uniform(0.83, 0.86), 4)])
        data.append([current_date, "AMD", round(random.uniform(410.0, 430.0), 2)])
        
    df = pd.DataFrame(data, columns=["date", "currency", "rate_to_eur"])
    df["date"] = pd.to_datetime(df["date"])
    return df

@task
def load_to_bigquery(df, table_name):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp_creds.json"
    client = bigquery.Client()
    
    project_id = client.project
    dataset_id = "market_analytics_raw"
    dataset_ref = bigquery.DatasetReference(project_id, dataset_id)
    
    try:
        client.get_dataset(dataset_ref)
    except Exception:
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"
        client.create_dataset(dataset)
        
    table_ref = dataset_ref.table(table_name)
    job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")
    
    job = client.load_table_from_dataframe(df, table_ref, job_config=job_config)
    job.result()

@flow(name="Market Data ELT Hub")
def market_hub_pipeline():
    raw_orders = generate_market_data(num_rows=1500)
    raw_rates = generate_currency_rates()
    
    load_to_bigquery(raw_orders, "transactions")
    load_to_bigquery(raw_rates, "currency_rates")

if __name__ == "__main__":
    market_hub_pipeline()