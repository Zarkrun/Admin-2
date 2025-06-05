import uuid
from datetime import datetime
import json
from flask import Flask, request
from flask_cors import CORS

import redis

import woody

app = Flask('my_api')
cors = CORS(app)

r = redis.Redis(host='redis', port=6379, decode_responses = True)


@app.get('/ping')
def ping():
    return 'ping'

# ### 3. Order Service
@app.route('/do', methods=['GET'])
def create_order():
    # very slow process because some payment validation is slow (maybe make it asynchronous ?)
    # order = request.get_json()
    product = request.args.get('order')
    order_id = str(uuid.uuid4())

    # TODO TP10: this next line is long, intensive and can be done asynchronously ... maybe use a message broker ?
    process_order(order_id, product)


    return f"Your process {order_id} has been created with this product : {product}"


@app.route('/', methods=['GET'])
def get_order():
    order_id = request.args.get('order_id')
    status = woody.get_order(order_id)

    return f'order "{order_id}": {status}'


# #### 4. internal Services
def process_order(order_id, order):
    # ...
    # ... do many check and stuff
    r.publish("order", json.dumps({order_id:order_id,order:order}))


if __name__ == "__main__":
    woody.launch_server(app, host='0.0.0.0', port=5000)
