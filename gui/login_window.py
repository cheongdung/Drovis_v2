import os
import sys

# Qt 플랫폼 플러그인 경로 명시 (OneDrive + PyQt5 Qt5 구조)
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"C:\Users\김민경\OneDrive\바탕 화면\Proj_drovis\Drovis_v2-main\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"

# import 경로 처리 (상위 폴더를 sys.path에 추가)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

# upload_window.py의 UploadWindow 클래스 가져오기
from gui.upload_window import UploadWindow

# PyQt5 위젯 모듈들
from PyQt5.QtWidgets import (
    QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QApplication
)


# 로그인 창 클래스
class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("로그인")
        self.setFixedSize(300, 200)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("아이디")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("비밀번호")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.login_button = QPushButton("로그인")
        self.login_button.clicked.connect(self.try_login)
        layout.addWidget(self.login_button)

        self.central_widget.setLayout(layout)

        self.upload = None  # 업로드 창 핸들

    def try_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # 간단한 인증 (실제로는 DB 또는 API 연동 가능)
        if username == "admin" and password == "1234":
            self.upload = UploadWindow(username)
            self.upload.show()
            self.close()
        else:
            QMessageBox.warning(self, "로그인 실패", "아이디 또는 비밀번호가 잘못되었습니다.")


# 실행 진입점
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = LoginWindow()
    login.show()
    sys.exit(app.exec_())
