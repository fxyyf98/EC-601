#!/usr/bin/env python
# coding: utf-8

import tweepy
import geocoder
import json


#Twitter API credentials
consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def get_loc_trends(loc):
    #initializations
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #get location geocode
    g = geocoder.osm(loc)
    #get closest trend location
    closest_loc = api.trends_closest(g.lat,g.lng)
    #get trends around loc
    trend_topics = api.trends_place(closest_loc[0]['woeid'])
    trends = trend_topics[0]['trends']
    trend_name = []
    for trend in trends:
        trend_name.append(trend['name'])
    return trend_name

def search_tweets(keywords,item_limit):
    #initializations
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    #search for tweets using api.search
    tweets = tweepy.Cursor(api.search,q=keywords).items(item_limit)
    return tweets
    
    

if __name__ == '__main__':
    get_loc_trends('Boston')
