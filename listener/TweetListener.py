#!/usr/bin/env python3

import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream
from elasticsearch import Elasticsearch
import json

class Listener(StreamListener):
   
    def __init__(self, es):
        self._es = es

    def on_data(self, data):
        try:
            data = json.loads(data)
            self._es.index(index='tweets', 
                            doc_type='tweets', 
                            body={  "user" : data['user']['screen_name'],
                                    "tweet" : data['text'],
                                    "created_at" : data['created_at']
                                    } )
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

class TweetListener(object):
    
    def __init__(self, auth, listener, hashtags):
        self._hashtags = hashtags
        self._listener = listener
        self._auth = auth

    def listener(self):
        twitter_stream = Stream(self._auth, self._listener)
        twitter_stream.filter(track=self._hashtags)