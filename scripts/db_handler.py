import sqlite3

# Connect to SQLite DB (creates file if it doesn't exist)
conn = sqlite3.connect("tweets.db")
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        sentiment TEXT,
        confidence REAL
    )
''')

conn.commit()
conn.close()