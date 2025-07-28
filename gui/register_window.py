import sys
import os
import json
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QComboBox, QHBoxLayout
)


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("회원가입")
        self.setFixedSize(350, 400)

        layout = QVBoxLayout()

        # ID 입력
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("아이디 입력 (예: user123)")
        layout.addWidget(QLabel("아이디"))
        layout.addWidget(self.id_input)

        # ID 중복확인 버튼
        id_check_layout = QHBoxLayout()
        self.check_button = QPushButton("중복 확인")
        self.check_button.clicked.connect(self.check_username)
        self.status_label = QLabel("")
        id_check_layout.addWidget(self.check_button)
        id_check_layout.addWidget(self.status_label)
        layout.addLayout(id_check_layout)

        # 이메일 입력
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("이메일 입력 (예: user@example.com)")
        layout.addWidget(QLabel("이메일"))
        layout.addWidget(self.email_input)

        # 비밀번호 입력
        self.pw_input = QLineEdit()
        self.pw_input.setPlaceholderText("비밀번호 입력 (8자 이상)")
        self.pw_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel("비밀번호"))
        layout.addWidget(self.pw_input)

        # 비밀번호 확인
        self.pw2_input = QLineEdit()
        self.pw2_input.setPlaceholderText("비밀번호 다시 입력")
        self.pw2_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel("비밀번호 확인"))
        layout.addWidget(self.pw2_input)

        # 사용자 역할 선택
        self.role_box = QComboBox()
        self.role_box.addItems(["일반 사용자", "경찰", "관리자"])
        layout.addWidget(QLabel("사용자 유형"))
        layout.addWidget(self.role_box)

        # 가입 버튼
        self.register_btn = QPushButton("가입하기")
        self.register_btn.clicked.connect(self.handle_register)
        layout.addWidget(self.register_btn)

        self.setLayout(layout)

    def check_username(self):
        username = self.id_input.text()
        if not username:
            self.status_label.setText("❗ 아이디를 입력하세요")
            self.status_label.setStyleSheet("color: orange;")
            return

        if self.is_duplicate_username(username):
            self.status_label.setText("이미 사용 중")
            self.status_label.setStyleSheet("color: red;")
        else:
            self.status_label.setText("사용 가능")
            self.status_label.setStyleSheet("color: green;")

    def is_duplicate_username(self, username, user_file="data/users.json"):
        if not os.path.exists(user_file):
            return False
        with open(user_file, "r", encoding="utf-8") as f:
            try:
                users = json.load(f)
                return any(user["username"] == username for user in users)
            except json.JSONDecodeError:
                return False

    def handle_register(self):
        username = self.id_input.text()
        email = self.email_input.text()
        pw1 = self.pw_input.text()
        pw2 = self.pw2_input.text()
        role = self.role_box.currentText()

        if not username or not email or not pw1 or not pw2:
            QMessageBox.warning(self, "입력 오류", "모든 항목을 입력해주세요.")
            return

        if pw1 != pw2:
            QMessageBox.warning(self, "비밀번호 오류", "비밀번호가 일치하지 않습니다.")
            return

        if self.is_duplicate_username(username):
            QMessageBox.warning(self, "중복 오류", "이미 존재하는 아이디입니다.")
            return

        # 사용자 정보 저장
        user_file = "data/users.json"
        os.makedirs("data", exist_ok=True)
        users = []
        if os.path.exists(user_file):
            with open(user_file, "r", encoding="utf-8") as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = []

        users.append({
            "username": username,
            "email": email,
            "password": pw1,  # 실제로는 해시 암호화 필요
            "role": role
        })

        with open(user_file, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=2)

        QMessageBox.information(self, "가입 완료", f"{username}님, 가입을 환영합니다!")
        self.close()


# 단독 실행용
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())
