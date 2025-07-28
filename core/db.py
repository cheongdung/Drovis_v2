# core/db.py
import sqlite3
from core.config import Config

def get_user_connection():
    return sqlite3.connect(Config.USER_DB_PATH)

def get_analysis_connection():
    return sqlite3.connect(Config.ANALYSIS_DB_PATH)
