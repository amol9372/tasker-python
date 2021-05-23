set -e

ls -altr
gunzip tasker.tar.gz
docker load -i tasker.tar
