import os
import time
import tweepy
import torch
import sqlite3
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# Load environment variables
load_dotenv()
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Initialize Twitter API client
client = tweepy.Client(bearer_token=BEARER_TOKEN)

# Load sentiment model and tokenizer
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Define sentiment labels
labels = ['Negative', 'Neutral', 'Positive']

# Function to get sentiment
def get_sentiment(text):
    tokens = tokenizer(text, return_tensors="pt", truncation=True)
    with torch.no_grad():
        output = model(**tokens)
        scores = F.softmax(output.logits, dim=1)
        predicted_class = torch.argmax(scores).item()
        confidence = scores[0][predicted_class].item()
    return labels[predicted_class], round(confidence, 2)

# Function to search and process tweets
def search_tweets(query, max_results=10):
    try:
        response = client.search_recent_tweets(query=query, max_results=max_results)
    except tweepy.TooManyRequests:
        print("⚠️ Rate limit hit. Waiting for 60 seconds...")
        time.sleep(60)
        return

    tweets = response.data

    if tweets:
        conn = sqlite3.connect("tweets.db")
        cursor = conn.cursor()

        for tweet in tweets:
            sentiment, confidence = get_sentiment(tweet.text)

            # Print to terminal
            print(f"\nTweet: {tweet.text}")
            print(f"Sentiment: {sentiment} (Confidence: {confidence})")

            # Insert into database
            cursor.execute('''
                INSERT INTO tweets (text, sentiment, confidence)
                VALUES (?, ?, ?)
            ''', (tweet.text, sentiment, confidence))

        conn.commit()
        conn.close()
    else:
        print("No tweets found.")

# Entry point
if __name__ == "__main__":
    search_tweets("AI")  # You can change the keyword here