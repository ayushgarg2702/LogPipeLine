from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch
from kafka import KafkaConsumer
import json

# Connect to Elasticsearch service running in Docker
app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Assuming your Kafka consumer is correctly configured
consumer = KafkaConsumer(
    'parsed-logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Index documents in Elasticsearch
for message in consumer:
    log = message.value
    print(log)
    es.index(index='logs', doc_type='_doc', body=log)
