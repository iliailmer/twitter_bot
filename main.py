import tweepy
import json

with open("token.json") as f:
    token = json.load(f)

# authentication

auth = tweepy.OAuthHandler(token['key'], token['key_secret'])

auth.set_access_token(token['access'], token['access_secret'])

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
