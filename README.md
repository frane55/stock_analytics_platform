# Stock Analytics Platform

Real-time platform for ingesting, storing, and analyzing stock market data using Kafka and Python.

## Stock Market Event

A stock market event represents a single trade snapshot
generated in real time.

what does a stock event consist of?
it's a simulation of a real life event so we have a symbol which represents
a certain company, timestamp of a change then we have the price change
and finally the volume which is the number of shares traded.

## Event Serialization

Stock events are serialized to JSON format
before being sent to the streaming platform.

Possible future extensions:

- event_type
- data_source
- ingestion_timestamp

## Kafka Topic

Topic name: stock_events  
Description: Real-time stream of simulated stock market events.

## Kafka Consumer Behavior

Consumers read events sequentially from a topic
and track their progress using offsets.

future goals: build a pipeline
