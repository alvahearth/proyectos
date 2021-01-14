import sqlite3

conn = sqlite3.connect("music.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS tracks")
cur.execute("CREATE TABLE tracks(title TEXT, plays INTEGER)")

cur.execute("INSERT INTO tracks (title , plays) VALUES ('Goodbye', 20)")

cur.execute("INSERT INTO tracks (title, plays) VALUES ('We move formward', 45)")

conn.commit()

print("Tracks: ")
cur.execute("SELECT title,plays FROM tracks")
for row in cur:
    print(row)
    
cur.execute("DELETE FROM tracks WHERE plays < 100")
conn.commit()

conn.close()