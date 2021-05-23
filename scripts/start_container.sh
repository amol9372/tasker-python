set -e


docker run -it -v $HOME/.aws/credentials:/root/.aws/credentials:ro -p 5000:5000 -d tasker-backend
