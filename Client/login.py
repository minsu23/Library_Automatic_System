# login.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from bookList import BookListWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label_id = QLabel('이름:')
        label_password = QLabel('학번:')

        self.lineEdit_id = QLineEdit()
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        login_button = QPushButton('로그인')
        login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout_h_id = QHBoxLayout()
        layout_h_password = QHBoxLayout()

        layout_h_id.addWidget(label_id)
        layout_h_id.addWidget(self.lineEdit_id)
        layout_h_password.addWidget(label_password)
        layout_h_password.addWidget(self.lineEdit_password)

        layout.addLayout(layout_h_id)
        layout.addLayout(layout_h_password)
        layout.addWidget(login_button)

        self.setLayout(layout)
        self.setWindowTitle('로그인 화면')

    def login(self):
        self.book_list_window = BookListWindow()
        self.book_list_window.show()
        self.hide()  # 로그인 창을 숨깁니다.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
