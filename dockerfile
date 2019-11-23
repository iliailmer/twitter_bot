FROM python:3.7-alpine

COPY bot/create_api.py /bot/
COPY bot/create_tweet.py /bot/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python", "create_tweet.py"]