
import tweepy
import pandas as pd
from textblob import TextBlob

# Twitter API credentials
api_key = "pQuUHOLEvtqwwBygkS0gRTOHR"
api_key_secret = "6ixfC9GVAg84pSsrppGqzhtTdZXX8pFiiAT4NJH4KDr0vKtN3Y"
access_token = "1867975772243435520-jq4OIMzEoDW6iEvFIXXZHyj9SXWtp7"
access_token_secret = "CPrc3HpEcPAhFQR3d9milumjlDcNoTvTljatIRWo2Rlly"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAP4vxgEAAAAAHUIX0FVaPLrWFBux4W7XR7bk%2FGg%3DOosTZt6KxZKA0BeUHKNGBR9eqb3TgQqKpOvaNICBGlx1Fnuv28"

# Authenticate using Bearer Token (API v2)
client = tweepy.Client(bearer_token=bearer_token)

# Query Twitter data
query = "Python"  # Replace with your keyword
response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=["created_at", "text"])

# Parse data
tweets = response.data
data = [{"Date": tweet.created_at, "Tweet": tweet.text} for tweet in tweets]

# Create DataFrame
df = pd.DataFrame(data)

# Sentiment Analysis
def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    return "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"

df["Sentiment"] = df["Tweet"].apply(analyze_sentiment)

# Save DataFrame to CSV
df.to_csv("twitter_sentiment_analysis.csv", index=False)

# Print DataFrame
print(df)
