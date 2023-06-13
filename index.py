from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import base64
import os
import time
import json
import sys
script_folder_path = os.path.dirname((os.path.realpath(__file__)))
sys.path.append(script_folder_path)
from barcode_reader import aggregated_reader

app = Flask(__name__, static_url_path='/', static_folder='./')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

reader = aggregated_reader.AggregatedReader()
engine = ""

@app.route('/', methods=['GET', 'POST'])
@app.route('/readBarcodes', methods=['GET', 'POST'])
@cross_origin()
def read_barcodes():
    if request.method == 'POST':
        data = request.get_json()
        if 'engine' in data:
            if data['engine'] != engine:
                reader = aggregated_reader.AggregatedReader(engine=engine)
        if 'base64' in data:
            bytes_decoded = base64.b64decode(data['base64'])
            start_time = time.time()
            response=reader.decode_bytes(bytes_decoded)
            end_time = time.time()
            elapsed_time = int((end_time - start_time) * 1000)
            response["elapsedTime"] = elapsed_time
            return json.dumps(response)
    else:
        return ""
        
@app.route('/getEngines', methods=['GET', 'POST'])
@cross_origin()
def get_engines():
    if request.method == 'GET':
        engines = reader.get_engines()
        return json.dumps(engines)
    else:
        return ""

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8888) #, ssl_context='adhoc'