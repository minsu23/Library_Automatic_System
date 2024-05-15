# addBook.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class AddBookWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('도서 추가')
        self.resize(400, 300)

        layout = QVBoxLayout()

        self.lineEdit_isbn = QLineEdit()
        self.lineEdit_isbn.setPlaceholderText('ISBN')
        self.lineEdit_book_name = QLineEdit()
        self.lineEdit_book_name.setPlaceholderText('책 이름')
        self.lineEdit_publisher = QLineEdit()
        self.lineEdit_publisher.setPlaceholderText('출판사')
        self.lineEdit_author = QLineEdit()
        self.lineEdit_author.setPlaceholderText('지은이')
        self.lineEdit_category = QLineEdit()
        self.lineEdit_category.setPlaceholderText('카테고리')
        self.lineEdit_row = QLineEdit()
        self.lineEdit_row.setPlaceholderText('책장 행')
        self.lineEdit_column = QLineEdit()
        self.lineEdit_column.setPlaceholderText('책장 열')
        self.lineEdit_publish_date = QLineEdit()
        self.lineEdit_publish_date.setPlaceholderText('출판 날짜')

        self.add_button = QPushButton('추가')
        self.add_button.clicked.connect(self.addBook)

        layout.addWidget(self.lineEdit_isbn)
        layout.addWidget(self.lineEdit_book_name)
        layout.addWidget(self.lineEdit_publisher)
        layout.addWidget(self.lineEdit_author)
        layout.addWidget(self.lineEdit_category)
        layout.addWidget(self.lineEdit_row)
        layout.addWidget(self.lineEdit_column)
        layout.addWidget(self.lineEdit_publish_date)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def addBook(self):
        isbn = self.lineEdit_isbn.text()
        book_name = self.lineEdit_book_name.text()
        row = self.lineEdit_row.text()
        column = self.lineEdit_column.text()

        if not isbn or not book_name or not row or not column:
            QMessageBox.warning(self, '입력 오류', 'ISBN, 책 이름, 책장 행, 책장 열을 모두 입력해야 합니다.')
        else:
            QMessageBox.information(self, '성공', '도서가 추가되었습니다.')
            self.close()
