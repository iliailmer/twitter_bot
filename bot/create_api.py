"""Module for connection to Twitter API."""
import tweepy
import json
import logging
from os import environ

logger = logging.getLogger()


def create_api():
    """Function for creating the API object."""
    # with open("token.json") as f:
    #     token = json.load(f)

    # authentication

    CONSUMER_KEY = environ['KEY']
    CONSUMER_SECRET = environ['SECRET_KEY']
    ACCESS_KEY = environ['ACCESS']
    ACCESS_SECRET = environ['ACCESS_SECRET']

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
