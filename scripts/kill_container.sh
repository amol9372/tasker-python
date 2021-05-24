#!/bin/bash

echo "Killing all active containers"
docker kill $(docker ps -q)

docker rm $(docker ps -a -q)

