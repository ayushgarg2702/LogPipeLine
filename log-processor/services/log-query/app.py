from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

@app.route('/logs', methods=['GET'])
def get_logs():
    log_type = request.args.get('logType')
    flow_name = request.args.get('flowName')
    res_code = request.args.get('resCode')
    sort_order = request.args.get('sort', 'asc')

    query = {
        "bool": {
            "must": [
                {"match": {"logType": log_type}} if log_type else {},
                {"match": {"flowName": flow_name}} if flow_name else {},
                {"match": {"res_code": res_code}} if res_code else {}
            ]
        }
    }
    
    sort = [{"timestamp": {"order": sort_order}}]
    
    response = es.search(index='logs', body={'query': query, 'sort': sort})
    return jsonify(response['hits']['hits'])

if __name__ == '__main__':
    app.run(debug=True)
