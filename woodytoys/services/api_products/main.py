import uuid
from datetime import datetime
import json
import threading

from flask import Flask, request
from flask_cors import CORS

import redis

import woody

app = Flask('my_api')
CORS(app, resources={r"/api/*": {"origins": "*"}})

r = redis.Redis(host='redis', port=6379, db=0)
t = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

@app.get('/api/ping')
def ping():
    return 'ping'



# ### 2. Product Service ###
@app.route('/api/products', methods=['GET'])
@app.route('/api/products/', methods=['GET'])
def add_product():
    product = request.args.get('product') or ""
    # 1) on ajoute en base
    woody.add_product(str(product))

    # 2) on met a jour le cache "last product" immédiatement
    cache_key_last = "products:last"
    # meme TTL que pour la récupération
    ttl = 60
    r.setex(cache_key_last, ttl, product)

    return str(product) or "none"

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    cache_key = f"product:{product_id}"
    cache = r.get(cache_key)
    if cache:
        return f"{datetime.now()}: {cache.decode('utf-8')}"

    product = woody.get_product(product_id)
    r.setex(cache_key, 60, product)
    return f"{datetime.now()}: {product}"


@app.route('/api/products/last', methods=['GET'])
def get_last_product():
    cache_key = "products:last"
    cache = r.get(cache_key)
    if cache:
        return f"{datetime.now()}: {cache.decode('utf-8')}"

    last_product = woody.get_last_product()
    r.setex(cache_key, 60, last_product)
    return f"{datetime.now()}: {last_product}"


def process_order(order_id, order):
    status = woody.make_heavy_validation(order)
    woody.save_order(order_id,status,order)

def listen_for_orders():
    pubsub = t.pubsub()
    pubsub.subscribe('orders')
    for message in pubsub.listen():
        if message['type'] == 'message':
            data = json.loads(message["data"])
            process_order(data["order_id"],data["order"])

if __name__ == "__main__":
    w = threading.Thread(target=listen_for_orders)
    w.start()
    woody.launch_server(app, host='0.0.0.0', port=5000)