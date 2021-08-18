#!/bin/bash

echo "Killing all active containers"

if [ ! -z "$(docker ps -q)" ]
then
   docker ps -q >> /tmp/code-deploy_tasker/killed_containers
   docker kill $(docker ps -q)
fi
   

if [ ! -z "$(docker ps -a -q)" ]
then
   docker rm $(docker ps -a -q)
fi

#docker kill $(docker ps -q)

#docker rm $(docker ps -a -q)

