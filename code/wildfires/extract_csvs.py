import pandas as pd
import sqlite3

conn = sqlite3.connect("database.sqlite")

subreddits = pd.read_sql("SELECT subreddit, COUNT(*) FROM May2015 GROUP BY subreddit ORDER BY COUNT(*) DESC;", conn)
data = pd.read_sql(f"SELECT * FROM May2015 WHERE subreddit = 'Showerthoughts'", conn)
data['created_utc'] = pd.to_datetime(data['created_utc'], unit='s')
print(subreddits.subreddit[100:125])
for name in subreddits.subreddit[50:75]:
    data = pd.read_sql(f"SELECT * FROM May2015 WHERE subreddit = '{name}'", conn)
    data.to_csv(f'{name}.csv')


from easytimer import tick, tock

for i in range(5):
    tick("DISTINCT")
    subreddits = pd.read_sql("SELECT DISTINCT(subreddit) FROM May2015;", conn)

    tick("GROUP BY")
    subreddits = pd.read_sql("SELECT subreddit FROM May2015 GROUP BY subreddit;", conn)

tock()