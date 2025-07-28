# core/services/save_analysis.py

import sqlite3
from datetime import datetime

# DB 경로는 config에서 불러오기를 권장
from core.config import Config

DB_PATH = Config.ANALYSIS_DB_PATH  # 예: "./database/analysis.db"

def save_analysis_result(user_id: str, filename: str, result: str):
    """
    분석 결과를 SQLite DB에 직접 저장 (analysis 테이블 기준)
    """
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.cursor()
        # 업로드 시간 now
        now = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

        # 컬럼명은 실제 테이블 구조에 맞게 조정 (예시: id는 autoincrement)
        cursor.execute(
            """
            INSERT INTO analysis (user_id, filename, result, uploaded_at)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, filename, result, now)
        )
        conn.commit()
    finally:
        conn.close()