set -e

cd docker.compressed.images

docker run -it -v $HOME/.aws/credentials:/root/.aws/credentials:ro -p 5000:5000 -d tasker-backend
