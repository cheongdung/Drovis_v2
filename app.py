# app.py
import sys, os
from PyQt5.QtWidgets import QApplication
from gui.login_window import LoginWindow
from core.models import create_user_table, create_analysis_table  # ✅ 간결하게 import 가능

# DB 폴더 자동 생성
if not os.path.exists("database"):
    os.makedirs("database")

# DB 테이블 생성
create_user_table()
create_analysis_table()

# 앱 실행
app = QApplication(sys.argv)
login = LoginWindow()
login.show()
sys.exit(app.exec_())
