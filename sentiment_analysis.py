
import tweepy
import pandas as pd
from textblob import TextBlob

# Twitter API credentials
api_key = "your_api_key"
api_key_secret = "your_key_secret"
access_token = "your_acess_token"
access_token_secret = "your_acess_token_secret"
bearer_token = "your_bearer_token"

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
