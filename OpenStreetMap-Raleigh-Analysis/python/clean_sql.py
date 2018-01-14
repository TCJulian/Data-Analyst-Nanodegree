import sqlite3

file_path = "C:\Users\sample_path\sqlite\OSMproject\OSM_db"

conn = sqlite3.connect(file_path)
cursor = conn.cursor()

# Remove carriage returns characters from specific columns
cursor.execute("UPDATE nodes SET timestamp=REPLACE(timestamp, '\r', '')")
cursor.execute("UPDATE nodes_tags SET type=REPLACE(type, '\r', '')")
cursor.execute("UPDATE ways SET timestamp=REPLACE(timestamp, '\r', '')")
cursor.execute("UPDATE ways_tags SET type=REPLACE(type, '\r', '')")

conn.commit()
conn.close()
