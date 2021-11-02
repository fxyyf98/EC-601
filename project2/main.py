import google_nlp
import twitter_api

trends = get_loc_trends("Boston")
for trend in trends:
    tweets = search_tweets(trend,10)
    score = 0
    for tweet in tweets:
        score += analyze_text_sentiment(tweet)
    print("trend:",trend)
    print("score:",score)
