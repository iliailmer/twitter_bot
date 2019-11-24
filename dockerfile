FROM ubuntu:latest

COPY bot/create_api.py /bot/
COPY bot/get_weather.py /bot/
COPY bot/create_tweet.py /bot/
COPY bot/cities.csv /bot/
COPY bot/server.py /bot/
COPY requirements.txt /tmp


RUN apt-get update \
    && apt-get install -y python3-pip python3-dev \
    && cd /usr/local/bin \
    && ln -s /usr/bin/python3 python \
    && pip3 install --upgrade pip
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python", "create_tweet.py"]