# Tweet Sentiment Pipeline

A real-time sentiment analysis tool built using Twitter API, HuggingFace Transformers, SQLite, and Streamlit.

## Features
- Fetches real tweets using Tweepy
- Applies AI-powered sentiment analysis (RoBERTa)
- Stores results in a local SQLite database
- Visualizes tweet sentiments with charts and filters

## How to Run

```bash
git clone <repo_url>
cd tweet-sentiment-pipeline
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt