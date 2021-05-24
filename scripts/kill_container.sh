#!/bin/bash

cd  /tmp/code-deploy_tasker/
rm -f *

echo "Killing all active containers"
docker kill $(docker ps -q)

docker rm $(docker ps -a -q)

