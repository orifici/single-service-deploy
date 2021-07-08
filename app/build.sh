#/bin/sh

# install dependencies (or use an appropriate runner)
dnf install -y docker
dnf install -y node
npm install -g snyk
pip install -r requirements.txt

# scan the code
snyk auth $API_TOKEN
snyk test

# run the tests
flake8 miner.py test_miner.py
pytest test_miner.py

# build the image
docker build -t dataminer:v1.0 .

# publish the image
docker login registry-1.docker.io
docker tag dataminer:v1.0 lorenzo/dataminer:v1.0
docker push lorenzo/dataminer:v1.0
