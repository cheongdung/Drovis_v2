# core/models/user_DB.py
from core.db import get_user_connection

def create_user_table():
    conn = get_user_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            role TEXT DEFAULT 'user'
        )
    """)
    conn.commit()
    conn.close()
