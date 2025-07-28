from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox
)
from PyQt5.QtCore import Qt
import json
import os

class HistoryWindow(QWidget):
    def __init__(self, history_file="data/history.json"):
        super().__init__()
        self.setWindowTitle("분석 기록")
        self.setGeometry(300, 200, 700, 500)
        self.history_file = history_file

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title = QLabel("최근 분석 기록")
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 15px;")
        layout.addWidget(title)

        # 테이블 위젯 생성
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["파일명", "위험도", "신뢰도", "날짜"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.table)

        # 버튼 영역
        btn_close = QPushButton("닫기")
        btn_close.clicked.connect(self.close)

        btn_clear = QPushButton("기록 삭제")
        btn_clear.clicked.connect(self.clear_history)

        layout.addWidget(btn_close)
        layout.addWidget(btn_clear)

        self.setLayout(layout)

        self.load_history()

    def load_history(self):
        if not os.path.exists(self.history_file):
            return

        with open(self.history_file, "r", encoding="utf-8") as f:
            history = json.load(f)

        self.table.setRowCount(len(history))

        for row, item in enumerate(history):
            self.table.setItem(row, 0, QTableWidgetItem(item["filename"]))
            self.table.setItem(row, 1, self.make_colored_item(item["result"]))
            self.table.setItem(row, 2, QTableWidgetItem(f'{item["confidence"] * 100:.1f}%'))
            self.table.setItem(row, 3, QTableWidgetItem(item["timestamp"]))


    def make_colored_item(self, level):
        item = QTableWidgetItem(level)
        if level == "상":
            item.setForeground(Qt.red)
        elif level == "중":
            item.setForeground(Qt.darkYellow)
        elif level == "하":
            item.setForeground(Qt.darkGreen)
        return item

    def clear_history(self):
        reply = QMessageBox.question(
            self, "기록 삭제", "모든 분석 기록을 삭제할까요?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            if os.path.exists(self.history_file):
                os.remove(self.history_file)
            self.table.setRowCount(0)
            QMessageBox.information(self, "삭제됨", "기록이 삭제되었습니다.")
if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = HistoryWindow()  # ← 클래스 이름 맞게!
    window.show()
    sys.exit(app.exec_())
