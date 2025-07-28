# core/services/auth.py
import sqlite3
import bcrypt
from core.db import get_user_connection

def register_user(username, password, email, role='user'):
    conn = get_user_connection()
    cur = conn.cursor()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    try:
        cur.execute("INSERT INTO users (username, password, email, role) VALUES (?, ?, ?, ?)",
                    (username, hashed_pw, email, role))
        conn.commit()
        return True, "회원가입 성공"
    except sqlite3.IntegrityError:
        return False, "이미 존재하는 아이디 또는 이메일"
    finally:
        conn.close()

def verify_user(username, password):
    conn = get_user_connection()
    cur = conn.cursor()
    cur.execute("SELECT password, role FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    conn.close()
    if row and bcrypt.checkpw(password.encode(), row[0].encode()):
        return True, row[1]
    return False, None
