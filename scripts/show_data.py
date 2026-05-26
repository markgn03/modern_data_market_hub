import duckdb

def show_final_mart():
    conn = duckdb.connect("market_analytics.duckdb")
    
    query = "SELECT * FROM fct_market_analytics"
    df = conn.execute(query).df()
    
    print(df.to_string())
    
    conn.close()

if __name__ == "__main__":
    show_final_mart()