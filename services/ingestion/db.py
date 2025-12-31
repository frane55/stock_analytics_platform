import duckdb

conn = duckdb.connect("../data/stocks.duckdb")

conn.execute("""
    CREATE TABLE IF NOT EXISTS stock_events (
        ticker TEXT,
        price DOUBLE,
        volume INTEGER,
        timestamp TIMESTAMP
    )
""")

def insert_event(event):
    ticker = event['ticker']
    price = event['price']
    volume = event['volume']
    timestamp = event['timestamp']
    try:
        conn.execute("""
        INSERT INTO stock_events(ticker, price, volume, timestamp)
        VALUES (?,?,?,?)
        """, (ticker, price, volume, timestamp))
        conn.commit()
    except Exception as e:
        print("error while inserting event", e)


#testing
#insert_event({
#  "ticker": "AAPL",
#  "price": 123.45,
#  "volume": 1000,
#  "timestamp": "2025-01-01T12:00:00"
#})


import duckdb
con = duckdb.connect("services/data/stocks.duckdb")
con.execute("SELECT * FROM stock_events").fetchall()