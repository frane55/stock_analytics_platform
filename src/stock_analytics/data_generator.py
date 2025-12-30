import random
import time
from datetime import datetime
import json

TICKERS = {
    "AAPL": 189.0,
    "MSFT": 420.0,
    "TSLA": 250.0
}

def generate_stock_event():
    ticker = random.choice(list(TICKERS.keys()))

    base_price = TICKERS[ticker]
    price_change = random.uniform(-1.0, 1.0)
    new_price = round(base_price + price_change, 2)

    TICKERS[ticker] = new_price

    event = {
        "ticker": ticker,
        "price": new_price,
        "volume": random.randint(100, 5000), #predstavlja simulirani broj dionica trgovanih
        "timestamp": datetime.utcnow().isoformat()
    }

    event_json = json.dumps(event, indent=4)
    return event_json

def send_event(event):
    print(event)

if __name__ == "__main__":
    while True:
        event = generate_stock_event()
        send_event(event)
        time.sleep(1)
