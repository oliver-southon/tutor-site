import sqlite3 as sql 

conn = sql.connect('peers.db')
c = conn.cursor()

c.execute(
    """
    CREATE TABLE IF NOT EXISTS peer (
        peer_id INTEGER NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        language TEXT NOT NULL,
        desc TEXT,
        date TEXT,
        amount_owed INTEGER,
        PRIMARY KEY (peer_id)
    )
    """
)

conn.close()