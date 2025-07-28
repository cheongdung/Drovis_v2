<<<<<<< Updated upstream
asdfdjhfkjafhdasjdf
=======
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import QFile, QTextStream

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("로그인")
        self.setGeometry(100, 100, 600, 400)

        self.apply_stylesheet("Drovis_v2/gui/styles.qss")  # 상대경로

    


        # 레이아웃 설정
        layout = QVBoxLayout()

        layout.setContentsMargins(40, 40, 40, 40)  # 왼, 위, 오, 아래 여백
        layout.setSpacing(20)  # 위젯 간 여백

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

        # 로그인 버튼
        self.btn_login = QPushButton("로그인")
        self.btn_login.clicked.connect(self.handle_login)
        layout.addWidget(self.btn_login)

        self.setLayout(layout)

    def handle_login(self):
        user_id = self.input_id.text()
        user_pw = self.input_pw.text()

        if user_id == "admin" and user_pw == "1234":
            QMessageBox.information(self, "성공", "로그인 성공!")
        else:
            QMessageBox.warning(self, "실패", "아이디 또는 비밀번호가 틀렸습니다.")

    def apply_stylesheet(self, path):
        file = QFile(path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())



    def apply_stylesheet(self, path):
        file = QFile(path)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        else:
            print(f"❌ 스타일시트 로드 실패: {path}")


# 실행 부분
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())
>>>>>>> Stashed changes
