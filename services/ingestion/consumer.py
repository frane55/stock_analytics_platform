from kafka import KafkaConsumer
import json
from db import insert_event

consumer = KafkaConsumer(
    'stock_events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit = True,
    value_deserializer = lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    message_event = message.value
    try:
        insert_event(message_event)
    except Exception as e:
        print("bad message mustn't break the ingestion", e)

