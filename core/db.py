# core/db.py
import sqlite3
from core.config import USER_DB_PATH, ANALYSIS_DB_PATH

def get_user_connection():
    return sqlite3.connect(USER_DB_PATH)

def get_analysis_connection():
    return sqlite3.connect(ANALYSIS_DB_PATH)
