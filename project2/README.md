# EC601-project2
A tutorial of Twitter API and Google NLP.

## Description
- This project mostly make use of the `api.search` and `api.trend_place` functions from tweepy, and the `language.analyze_sentiment` function from google cloud language.
- `get_loc_trends(loc)` developed from `api.trend_place` gets the input parameter loc as location and returns the top twitter trends around that location.
- `search_tweets(keywords,item_limit)` developed from `api.search` gets the input keyword and search for relevent tweets on twitter and returns the text content.
- `analyze_text_sentiment(text)` developed from `language.analyze_sentiment` gets the input text and return the sentiment score and magnitude for this text.
- Make use of the functions I developed above could obtain popular events aound the location you are interested and search for tweets about that trend, then you can do sentiment analysis on these tweets to see how people feel about these trends.
- Or you can use these functions seperately for different purposes.

## User storys
- As a taveller, I want to know what's going on around the place I'm going.
- As a taveller, I want to know what people say about the place I'going.
- As a taveller, I want to know how people feel about the place I'm going.
- As a user, I want to understand what's people's attitude toward these popular events.
- ...

## Tests
I searched the trends at Boston to search for relevent tweets and tested the sentiment of these tweets, and analyzed the result to show a overall attitude about the trend.

## Reference
- https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3/index.html
- https://github.com/tweepy/tweepy
- https://blog.csdn.net/weixin_40221833/article/details/79522834
