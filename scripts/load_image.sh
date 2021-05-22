set -e

cd docker.compressed.images
aws s3 cp s3://test-bucket-acloudguru-3921/tasker-docker/tasker.tar.gz .
unzip tasker.tar.gz
docker load -i tasker.tar.gz
