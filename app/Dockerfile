FROM python:3.9-alpine

COPY requirements.txt /
COPY templates/ /templates/
COPY miner.py run_miner.sh /

RUN mkdir www && \
  pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

ENTRYPOINT ["sh", "run_miner.sh"]
