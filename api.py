from flask import Flask
from flask_cors import CORS
import json
import random
import time

app = Flask(__name__)
CORS(app)

i = 0
times = int(time.time()*1000)
@app.route('/', methods=['POST', 'GET'])
def hello_world():
    global i,times
    i += 100
    times = times + 60*1000
    return json.dumps([random.randint(1, 100), times])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)