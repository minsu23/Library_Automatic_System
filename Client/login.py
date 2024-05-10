# login.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy
from bookList import BookListWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 레이블 및 입력 필드 생성
        label_id = QLabel('이름:')
        label_password = QLabel('학번:')
        self.lineEdit_id = QLineEdit()
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        # 입력 필드 너비 조절
        intput_width = 200
        self.lineEdit_id.setFixedWidth(intput_width)  # 너비를 200 픽셀로 설정
        self.lineEdit_password.setFixedWidth(intput_width)  # 너비를 200 픽셀로 설정

        # ID(이름)와 Password(학번)레이아웃 설정
        layout_h_id = QHBoxLayout()
        layout_h_id.addStretch()  # 왼쪽 스페이스 추가
        layout_h_id.addWidget(label_id)
        layout_h_id.addWidget(self.lineEdit_id)
        layout_h_id.addStretch()  # 오늘쪽 스페이스 추가

        layout_h_password = QHBoxLayout()
        layout_h_password.addStretch()  # 왼쪽 스페이스 추가
        layout_h_password.addWidget(label_password)
        layout_h_password.addWidget(self.lineEdit_password)
        layout_h_password.addStretch()  # 오른쪽 스페이스 추가

        # 로그인 버튼 생성
        login_button = QPushButton('로그인')
        login_button.setFixedWidth(intput_width + 40)
        login_button.clicked.connect(self.login)

        # 로그인 버튼 레이아웃 설정
        layout_h_button = QHBoxLayout()
        layout_h_button.addStretch()
        layout_h_button.addWidget(login_button)
        layout_h_button.addStretch()

        # 전체 레이아웃 설정
        layout = QVBoxLayout()
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # 상단 스페이서
        layout.addLayout(layout_h_id)
        layout.addLayout(layout_h_password)
        layout.addLayout(layout_h_button)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))  # 하단 스페이서

        self.setLayout(layout)
        self.setWindowTitle('로그인 화면')
        self.resize(640, 360)  # 창 크기 설정

    def login(self):
        self.book_list_window = BookListWindow()
        self.book_list_window.show()
        self.hide()  # 로그인 창 숨김

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
