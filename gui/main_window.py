import os
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = r"C:\Users\김민경\OneDrive\바탕 화면\Proj_drovis\Drovis_v2-main\venv\Lib\site-packages\PyQt5\Qt5\plugins\platforms"



# gui/main_window.py
import random
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drovis - 영상 분석")
        self.resize(1000, 600)
        self.file_path = None
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        upload_layout = QHBoxLayout()
        self.upload_btn = QPushButton("영상 업로드")
        self.upload_btn.clicked.connect(self.upload_file)
        self.file_label = QLabel("업로드된 파일 없음")
        upload_layout.addWidget(self.upload_btn)
        upload_layout.addWidget(self.file_label)
        layout.addLayout(upload_layout)

        self.analyze_btn = QPushButton("분석 시작")
        self.analyze_btn.clicked.connect(self.start_analysis)
        layout.addWidget(self.analyze_btn)

        self.result_table = QTableWidget()
        self.result_table.setColumnCount(4)
        self.result_table.setHorizontalHeaderLabels(
            ["파일명", "상태", "유사도 결과", "시간"]
        )
        layout.addWidget(self.result_table)

        self.setLayout(layout)

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "영상 선택", "", "Video Files (*.mp4 *.avi)"
        )
        if file_path:
            self.file_path = file_path
            self.file_label.setText(os.path.basename(file_path))

    def start_analysis(self):
        if not self.file_path:
            QMessageBox.warning(self, "경고", "먼저 영상을 업로드하세요.")
            return

        similarity_score = round(random.uniform(0.3, 0.95), 2)

        if similarity_score >= 0.8:
            result = "상"
        elif similarity_score >= 0.5:
            result = "중"
        else:
            result = "하"

        row = self.result_table.rowCount()
        self.result_table.insertRow(row)
        self.result_table.setItem(
            row, 0, QTableWidgetItem(os.path.basename(self.file_path))
        )
        self.result_table.setItem(row, 1, QTableWidgetItem("완료"))
        self.result_table.setItem(row, 2, QTableWidgetItem(result))
        self.result_table.setItem(
            row, 3, QTableWidgetItem(datetime.now().strftime("%Y-%m-%d %H:%M"))
        )


# 단독 실행용
import os

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)

    # 현재 스크립트 기준 절대 경로로 QSS 불러오기
    qss_path = os.path.join(os.path.dirname(__file__), "styles.qss")
    with open(qss_path, "r", encoding="utf-8") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


