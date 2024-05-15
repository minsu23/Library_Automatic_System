# addUser.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class AddUserWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('회원 추가')
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.lineEdit_user_name = QLineEdit()
        self.lineEdit_user_name.setPlaceholderText('회원 이름')
        self.lineEdit_user_id = QLineEdit()
        self.lineEdit_user_id.setPlaceholderText('학번')
        self.lineEdit_user_passwd = QLineEdit()
        self.lineEdit_user_passwd.setPlaceholderText('비밀 번호')

        self.add_button = QPushButton('추가')
        self.add_button.clicked.connect(self.addUser)

        layout.addWidget(self.lineEdit_user_name)
        layout.addWidget(self.lineEdit_user_id)
        layout.addWidget(self.lineEdit_user_passwd)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def addUser(self):
        user_name = self.lineEdit_user_name.text()
        user_id = self.lineEdit_user_id.text()
        user_passwd= self.lineEdit_user_passwd.text()

        if not user_name or not user_id or not user_passwd:
            QMessageBox.warning(self, '입력 오류', '회원 이름과 학번을, 비번을 모두 입력해야 합니다.')
        else:
            QMessageBox.information(self, '성공', '회원이 추가되었습니다.')
            self.close()
