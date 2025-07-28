import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QPushButton, QVBoxLayout
)

# 경로 문제 해결: 상위 경로에 Drovis_v2 등록
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(PARENT_DIR)

# 다른 창 import (Drovis_v2/gui/upload_window.py 등)
from gui.login_window import LoginWindow
from gui.register_window import RegisterWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drovis")
        self.setFixedSize(1200, 1000)

        # 중앙 위젯
        central_widget = QWidget()
        layout = QVBoxLayout()

        welcome_label = QLabel("마약 드로퍼 탐지를 도와주는 Drovis입니다.")
        layout.addWidget(welcome_label)

        # 로그인 버튼
        login_btn = QPushButton("로그인")
        login_btn.clicked.connect(self.open_login_window)
        layout.addWidget(login_btn)

        # 회원가입 버튼
        register_btn = QPushButton("회원가입")
        register_btn.clicked.connect(self.open_register_window)
        layout.addWidget(register_btn)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 창 초기화
        self.login_window = None
        self.register_window = None

    def open_login_window(self):
        self.login_window = LoginWindow()
        self.login_window.show()
        self.close()

    def open_register_window(self):
        self.register_window = RegisterWindow()
        self.register_window.show()


# 단독 실행 시 진입점
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
