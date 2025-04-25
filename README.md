[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)

# 🧠 Tweet Sentiment Pipeline

This project is a real-time sentiment analysis dashboard that:
- 🔄 Fetches live tweets using the Twitter API (via Tweepy)
- 🧠 Analyzes sentiments using HuggingFace Transformers (RoBERTa)
- 🗃️ Stores results in SQLite
- 📊 Visualizes insights in an interactive Streamlit dashboard

## 🚀 Live Demo
👉 [View Dashboard](https://tweet-sense-ai-v7kxmwyerb9wawid6c9aam.streamlit.app/)  

## 💡 Features
- Real-time sentiment analysis on tweets
- HuggingFace-powered classification (Positive / Neutral / Negative)
- SQLite integration for local persistence
- Filters by sentiment and keyword
- Charts: bar, pie, and trend over time
- Deployed via Streamlit Cloud

## 🛠️ Stack Used
- Python 3.9
- Tweepy (Twitter API)
- HuggingFace Transformers
- SQLite
- Pandas, Altair, Matplotlib
- Streamlit (frontend)

## 📦 To Run Locally

```bash
git clone https://github.com/RupeshAkula98/tweet-sense-ai.git
cd tweet-sense-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
