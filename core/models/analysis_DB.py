# core/models/analysis_DB.py
from core.db import get_analysis_connection

def create_analysis_table():
    conn = get_analysis_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS analysis (
			    id INTEGER PRIMARY KEY AUTOINCREMENT,
			    user_id TEXT NOT NULL,
			    filename TEXT NOT NULL,
			    result TEXT NOT NULL,
			    uploaded_at TEXT NOT NULL,
			    memo TEXT
				);
    """)
    conn.commit()
    conn.close()