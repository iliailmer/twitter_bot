import tweepy
import json
import logging

logger = logging.getLogger()


def create_api():
    with open("token.json") as f:
        token = json.load(f)

    # authentication

    auth = tweepy.OAuthHandler(token['key'], token['key_secret'])

    auth.set_access_token(token['access'], token['access_secret'])

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
