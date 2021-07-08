#/bin/sh

python miner.py > miner.log 2>&1 & \
 python -m http.server 8080 --directory www
