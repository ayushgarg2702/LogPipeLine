from kafka import KafkaProducer
import json
import time
import uuid
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

log_types = ['debugLog', 'errorLog', 'outgoingApi', 'incomingApi']

def generate_log():
    log_type = log_types[int(time.time()) % 4]
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'x-request-id': str(uuid.uuid4()),
        'flowName': 'exampleFlow',
        'logType': log_type,
        'message': 'This is a sample log message' if 'Log' in log_type else None,
        'req_body': 'Sample request body' if 'Api' in log_type else None,
        'res_body': 'Sample response body' if 'Api' in log_type else None,
        'latency': 123 if 'Api' in log_type else None,
        'res_code': 200 if 'Api' in log_type else None
    }

while True:
    log = generate_log()
    producer.send('logs', log)
    print(log)
    time.sleep(1)
