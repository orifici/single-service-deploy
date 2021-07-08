# Instructions

## Dependencies
```bash
pip install -r requirements.txt
```
## Running the tests
```bash
# linting
flake8 miner.py test_miner.py
# unit tests
pytest test_miner.py
```

## Running the python App (standalone)
```bash
python miner.py
```

## Building the image
```bash
docker build -t dataminer:v1.0 .
```

## Running the container (standalone)
```bash
docker run -d --name miner -p 8090:8080 --rm dataminer:v1.0
docker exec <ID> tail -f miner.log
```

## Scanning you project
```bash
snyk auth <API_TOKEN>
snyk test
```

## Publish the image
```bash
docker login <registry>
docker tag dataminer:v1.0 lorenzo/dataminer:v1.0
docker push lorenzo/dataminer:v1.0
```
