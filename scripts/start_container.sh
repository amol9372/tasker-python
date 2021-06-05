#!/bin/bash

#docker run -it -v $HOME/.aws/credentials:/root/.aws/credentials:ro -p 5000:5000 -d tasker-backend

docker run -it -v $HOME/.aws/credentials:/root/.aws/credentials:ro --env-file ~/docker/env_files/tasker.env -p 5000:5000 -d tasker-backend
