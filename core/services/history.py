import sqlite3
from core.config import Config

DB_PATH = Config.ANALYSIS_DB_PATH  # 예: ./database/analysis.db

def get_history(user_id: str):
    """
    특정 사용자의 분석 기록 전체를 최신순으로 조회.
    Returns: 리스트(dict)
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM analysis WHERE user_id = ? ORDER BY uploaded_at DESC",
            (user_id,)
        )
        rows = cur.fetchall()
        # dict list로 리턴
        return [dict(row) for row in rows]
    finally:
        conn.close()

def update_memo(record_id: int, user_id: str, memo: str):
    """
    분석 기록의 메모 수정
    Returns: True(성공) or False(권한없음/없음)
    """
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        # 기록 존재/권한 확인
        cur.execute("SELECT * FROM analysis WHERE id = ? AND user_id = ?", (record_id, user_id))
        if cur.fetchone() is None:
            return False  # Not found or not owner

        cur.execute(
            "UPDATE analysis SET memo = ? WHERE id = ? AND user_id = ?",
            (memo, record_id, user_id)
        )
        conn.commit()
        return True
    finally:
        conn.close()

def delete_history(record_id: int, user_id: str):
    """
    분석 기록 삭제 (소유자만)
    Returns: True(성공) or False(권한없음/없음)
    """
    conn = sqlite3.connect(DB_PATH)
    try:
        cur = conn.cursor()
        # 기록 존재/권한 확인
        cur.execute("SELECT * FROM analysis WHERE id = ? AND user_id = ?", (record_id, user_id))
        if cur.fetchone() is None:
            return False
        cur.execute("DELETE FROM analysis WHERE id = ? AND user_id = ?", (record_id, user_id))
        conn.commit()
        return True
    finally:
        conn.close()

