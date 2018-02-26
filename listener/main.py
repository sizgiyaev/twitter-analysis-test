#!/usr/bin/env python3

import tweepy
from TweetListener import TweetListener
from TweetListener import Listener
from elasticsearch import Elasticsearch
import os

def main():
    consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    hashtags = os.getenv('TWITTER_HASHTAGS').split(",")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    es = Elasticsearch([{'host': os.getenv('ELASTICSEARCH_HOST'), 'port': os.getenv('ELASTICSEARCH_PORT') }])

    tl = TweetListener(auth, Listener(es), hashtags)
    tl.listener()

if __name__ == "__main__":
    main()