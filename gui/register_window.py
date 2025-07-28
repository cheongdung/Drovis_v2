import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QMessageBox, QComboBox, QHBoxLayout
)
from core.services.auth import register_user

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("회원가입")
        self.setFixedSize(350, 400)

        layout = QVBoxLayout()

        # 아이디 입력
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("아이디 입력 (예: user123)")
        layout.addWidget(QLabel("아이디"))
        layout.addWidget(self.id_input)

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

    def handle_register(self):
        username = self.id_input.text().strip()
        email = self.email_input.text().strip()
        pw1 = self.pw_input.text()
        pw2 = self.pw2_input.text()
        role_map = {
            "일반 사용자": "user",
            "경찰": "police",
            "관리자": "admin"
        }
        role = role_map.get(self.role_box.currentText(), "user")

        if not username or not email or not pw1 or not pw2:
            QMessageBox.warning(self, "입력 오류", "모든 항목을 입력해주세요.")
            return

        if pw1 != pw2:
            QMessageBox.warning(self, "비밀번호 오류", "비밀번호가 일치하지 않습니다.")
            return

        # 회원가입 시도 (register_user 내부에서 bcrypt 해시 처리 및 중복 검사)
        success, message = register_user(username, pw1, email, role)
        if success:
            QMessageBox.information(self, "가입 완료", f"{username}님, 가입을 환영합니다!")
            self.close()
        else:
            QMessageBox.warning(self, "가입 실패", message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())
