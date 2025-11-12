import sqlite3


conn = sqlite3.connect("db/focuswatch.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS mouse_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    x_pos TEXT,
    y_pos TEXT,
    click BOOLEAN DEFAULT FALSE,
    timestamp TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%f', 'now'))
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS key_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    release BOOLEAN,
    key TEXT,
    timestamp TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%f', 'now'))
);
""")

conn.commit()

conn.close()