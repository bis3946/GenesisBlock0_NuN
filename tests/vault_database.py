import sqlite3
import os

DB_PATH = os.getenv("VAULT_DB_PATH", "vault.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS blocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            timestamp TEXT,
            observer TEXT,
            hash TEXT UNIQUE,
            echo TEXT,
            shadow TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_block(block):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT OR IGNORE INTO blocks (data, timestamp, observer, hash, echo, shadow)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (block.data, block.timestamp, block.observer, block.hash, block.echo, block.shadow))
    conn.commit()
    conn.close()
