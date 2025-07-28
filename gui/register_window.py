import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)
from PyQt5.QtCore import QFile, QTextStream

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("회원가입")
        self.setGeometry(100, 100, 350, 200)
        self.apply_stylesheet("Drovis_v2/gui/styles.qss")

        layout = QVBoxLayout()

        # 아이디 입력
        self.label_id = QLabel("아이디")
        self.input_id = QLineEdit()
        layout.addWidget(self.label_id)
        layout.addWidget(self.input_id)

        # 비밀번호 입력
        self.label_pw = QLabel("비밀번호")
        self.input_pw = QLineEdit()
        self.input_pw.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_pw)
        layout.addWidget(self.input_pw)

        # 비밀번호 확인
        self.label_pw2 = QLabel("비밀번호 확인")
        self.input_pw2 = QLineEdit()
        self.input_pw2.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_pw2)
        layout.addWidget(self.input_pw2)

        # 가입 버튼
        self.btn_register = QPushButton("가입하기")
        self.btn_register.clicked.connect(self.handle_register)
        layout.addWidget(self.btn_register)

        self.setLayout(layout)

    def handle_register(self):
        user_id = self.input_id.text()
        pw1 = self.input_pw.text()
        pw2 = self.input_pw2.text()

        if not user_id or not pw1 or not pw2:
            QMessageBox.warning(self, "오류", "모든 항목을 입력해주세요.")
            return

        if pw1 != pw2:
            QMessageBox.warning(self, "오류", "비밀번호가 일치하지 않습니다.")
            return

        # 여기에 회원가입 로직 추가 가능 (ex. 파일 저장, DB 연동)
        QMessageBox.information(self, "성공", f"{user_id}님, 가입을 환영합니다!")
        self.close()

    def apply_stylesheet(self, path):
        file = QFile(path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        else:
            print(f"❌ 스타일시트 로드 실패: {path}")


# 실행
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())
