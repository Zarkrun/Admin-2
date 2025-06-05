import uuid
from datetime import datetime

from flask import Flask, request
from flask_cors import CORS

import redis

import woody

app = Flask('my_api')
cors = CORS(app)

r = redis.Redis(host='redis', port=6379, db=0)


@app.get('/api/ping')
def ping():
    return 'ping'


# ### 1. Misc service ### (note: la traduction de miscellaneous est 'divers'
@app.route('/api/misc/time', methods=['GET'])
def get_time():
    return f'misc: {datetime.now()}'


@app.route('/api/misc/heavy', methods=['GET'])
def get_heavy():
    # TODO TP9: cache ?
    name = request.args.get('name')
    cache = r.get(name)
    if cache:
        return f'{datetime.now()}: {cache}'
    s = woody.make_some_heavy_computation(name)
    r.setex(name, 60, s)
    # on rajoute la date pour pas que le resultat ne soit mis en cache par le browser
    return f'{datetime.now()}: {s}'


if __name__ == "__main__":
    woody.launch_server(app, host='0.0.0.0', port=5000)