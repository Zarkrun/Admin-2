#!/bin/bash

set -e

default_version="4"
version=${1:-"$default_version"}

# 🛠️ Build API ORDERS
docker build -t zarkrun/woody_api_orders:"$version" api_orders
docker tag zarkrun/woody_api_orders:"$version" zarkrun/woody_api_orders:latest

# 🛠️ Build API PRODUCTS
docker build -t zarkrun/woody_api_products:"$version" api_products
docker tag zarkrun/woody_api_products:"$version" zarkrun/woody_api_products:latest

# 🛠️ Build API MISC
docker build -t zarkrun/woody_api_misc:"$version" api_misc
docker tag zarkrun/woody_api_misc:"$version" zarkrun/woody_api_misc:latest

# 🛠️ Build REVERSE PROXY
docker build -t zarkrun/woody_rp:"$version" reverse-proxy
docker tag zarkrun/woody_rp:"$version" zarkrun/woody_rp:latest

# 🛠️ Build DATABASE
docker build -t zarkrun/woody_database:"$version" database
docker tag zarkrun/woody_database:"$version" zarkrun/woody_database:latest

# 🛠️ Build FRONT
docker build -t zarkrun/woody_front:"$version" front
docker tag zarkrun/woody_front:"$version" zarkrun/woody_front:latest

# 🚀 Push all images
docker push zarkrun/woody_api_orders:"$version"
docker push zarkrun/woody_api_orders:latest

docker push zarkrun/woody_api_products:"$version"
docker push zarkrun/woody_api_products:latest

docker push zarkrun/woody_api_misc:"$version"
docker push zarkrun/woody_api_misc:latest

docker push zarkrun/woody_rp:"$version"
docker push zarkrun/woody_rp:latest

docker push zarkrun/woody_front:"$version"
docker push zarkrun/woody_front:latest

docker push zarkrun/woody_database:"$version"
docker push zarkrun/woody_database:latest
