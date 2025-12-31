from kafka import KafkaProducer
import json
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from src.stock_analytics.data_generator import generate_stock_event


producer = KafkaProducer(
    bootstrap_servers = "localhost:9092",
    value_serializer = lambda v: v.encode('utf-8')

)

while True:
    event = generate_stock_event()
    producer.send('stock_events', value=event)
    time.sleep(2)