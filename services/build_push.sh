#/bin/bash

set -e

default_version="3"
version=${1:-"$default_version"}

docker build -t zarkrun/woody_api:"$version" api
docker tag zarkrun/woody_api:"$version" zarkrun/woody_api:latest

docker build -t zarkrun/woody_rp:"$version" reverse-proxy
docker tag zarkrun/woody_rp:"$version" zarkrun/woody_rp:latest

docker build -t zarkrun/woody_database:"$version" database
docker tag zarkrun/woody_database:"$version" zarkrun/woody_database:latest

docker build -t zarkrun/woody_front:"$version" front
docker tag zarkrun/woody_front:"$version" zarkrun/woody_front:latest

# avec le "set -e" du début, je suis assuré que rien ne sera pushé si un seul build ne c'est pas bien passé

docker push zarkrun/woody_api:"$version"
docker push zarkrun/woody_api:latest

docker push zarkrun/woody_rp:"$version"
docker push zarkrun/woody_rp:latest

docker push zarkrun/woody_front:"$version"
docker push zarkrun/woody_front:latest

docker push zarkrun/woody_database:"$version"
docker push zarkrun/woody_database:latest
