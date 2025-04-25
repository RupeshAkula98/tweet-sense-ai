import sqlite3
import pandas as pd
import streamlit as st
import altair as alt
import matplotlib.pyplot as plt

# Connect to SQLite and create table if it doesn't exist
conn = sqlite3.connect("tweets.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tweets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        sentiment TEXT,
        confidence REAL
    )
""")
conn.commit()

# Read data if exists
df = pd.read_sql_query("SELECT * FROM tweets", conn)
conn.close()

# Handle empty data gracefully
if df.empty:
    st.warning("⚠️ No tweet data found in database. Run the sentiment pipeline to populate it.")
    st.stop()
df = pd.read_sql_query("SELECT * FROM tweets", conn)
conn.close()

# Add row_id for timeline (simulate time order)
df['row_id'] = range(1, len(df) + 1)

# Title
st.title("📊 Tweet Sentiment Dashboard")
st.markdown("Analyze real-time tweet sentiments with AI-powered classification.")

# Sidebar filters
st.sidebar.header("🔍 Filters")
sentiment_filter = st.sidebar.multiselect(
    "Filter by Sentiment:",
    options=["Positive", "Neutral", "Negative"],
    default=["Positive", "Neutral", "Negative"]
)

search_keyword = st.sidebar.text_input("Search tweets by keyword:")

# Apply filters
filtered_df = df[df["sentiment"].isin(sentiment_filter)]
if search_keyword:
    filtered_df = filtered_df[filtered_df["text"].str.contains(search_keyword, case=False, na=False)]

# Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Positive", len(df[df.sentiment == "Positive"]))
col2.metric("Neutral", len(df[df.sentiment == "Neutral"]))
col3.metric("Negative", len(df[df.sentiment == "Negative"]))

# Bar chart
st.subheader("📈 Sentiment Distribution (Bar Chart)")
bar_chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X("sentiment:N", title="Sentiment"),
    y=alt.Y("count():Q", title="Tweet Count"),
    color="sentiment:N"
).properties(width=600)
st.altair_chart(bar_chart)

# Pie chart
st.subheader("📊 Sentiment Share (Pie Chart)")
pie_data = filtered_df["sentiment"].value_counts()
fig, ax = plt.subplots()
ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
ax.axis("equal")
st.pyplot(fig)

# Timeline trend chart
st.subheader("📉 Sentiment Confidence Trend (Fetch Order)")
trend_chart = alt.Chart(filtered_df).mark_line(point=True).encode(
    x=alt.X("row_id:Q", title="Tweet Order (Oldest to Newest)"),
    y=alt.Y("confidence:Q", title="Sentiment Confidence"),
    color="sentiment:N",
    tooltip=["text", "sentiment", "confidence"]
).interactive().properties(width=700)
st.altair_chart(trend_chart)

# Tweet Table
st.subheader("🗂️ Filtered Tweets")
st.dataframe(filtered_df[['text', 'sentiment', 'confidence']])