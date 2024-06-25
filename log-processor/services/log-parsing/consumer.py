from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(
    'logs',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

for message in consumer:
    log = message.value
    
    # Enrichment logic based on logType
    if log['logType'] == 'errorLog':
        log['severity'] = 'high'
    elif log['logType'] == 'debugLog':
        log['severity'] = 'low'

    print(f"Parsed log: {log}")
    producer.send('parsed-logs', log)
