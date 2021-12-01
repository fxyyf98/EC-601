import google_nlp
import twitter_api
import pytest

## test get trend function returns trends
def test_get_trend_num():
    trends = get_loc_trends("Boston")
    assert len(trends)!=0
## test get trend function returns a list
def test_get_trend_type():
    trends = get_loc_trends("Boston")
    assert type(trends) == list
## test search tweet function returns the number of tweets we define
def test_search_tweet_num(n):
    trends = get_loc_trends("Boston")
    tweets = search_tweets(trend,n)
    assert len(tweets) = n
## test search tweet function returns tweets as string objects
def test_search_tweet_type():
    trends = get_loc_trends("Boston")
    tweets = search_tweets(trend,10)
    for tweet in tweets:
        assert type(tweet) == str
## test analyze sentiment function returns float scores
def test_sentiment_score(txt):
    assert type(analyze_text_sentiment(txt)) == float
