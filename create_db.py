import sqlite3 as sql 

conn = sql.connect('peers.db')
c = conn.cursor()

c.execute(
    """
    CREATE TABLE IF NOT EXISTS peer (
        peer_id INTEGER,
        first_name TEXT NOT NULL,
        last_name TEXT,
        age INTEGER,
        email TEXT NOT NULL,
        language TEXT,
        desc TEXT,
        contact_method TEXT,
        date_joined TEXT,
        amount_owed INTEGER,
        PRIMARY KEY (peer_id)
    )
    """
)

conn.close()