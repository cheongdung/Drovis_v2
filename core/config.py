# core/config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Config:
    USER_DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'users.db')
    ANALYSIS_DB_PATH = os.path.join(BASE_DIR, '..', 'database', 'analysis.db')
    UPLOAD_FOLDER = os.path.join(BASE_DIR, '..', 'uploads')
    MODEL_FOLDER = os.path.join(BASE_DIR, '..', 'ai_models')