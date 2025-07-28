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
from gui.upload_window import UploadWindow
from gui.history_window import HistoryWindow

class MainWindow(QMainWindow):
    def __init__(self, username="김민경"):
        super().__init__()
        self.username = username
        self.setWindowTitle(f"Welcome, {self.username}")
        self.setFixedSize(400, 300)

        # 중앙 위젯
        central_widget = QWidget()
        layout = QVBoxLayout()

        welcome_label = QLabel(f"{self.username}님, Drovis에 오신 것을 환영합니다!")
        layout.addWidget(welcome_label)

        # 분석 업로드 버튼
        upload_btn = QPushButton("영상 업로드 및 분석")
        upload_btn.clicked.connect(self.open_upload_window)
        layout.addWidget(upload_btn)

        # 분석 기록 조회 버튼
        history_btn = QPushButton("분석 기록 조회")
        history_btn.clicked.connect(self.open_history_window)
        layout.addWidget(history_btn)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # 창 초기화
        self.upload_window = None
        self.history_window = None

    def open_upload_window(self):
        self.upload_window = UploadWindow(self.username)
        self.upload_window.show()

    def open_history_window(self):
        self.history_window = HistoryWindow(self.username)
        self.history_window.show()


# 단독 실행 시 진입점
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
