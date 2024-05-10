# bookList.py
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QHBoxLayout, QHeaderView, QApplication, QComboBox, QLineEdit, QPushButton

class BookListWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 검색 구성요소 설정
        self.comboBox = QComboBox()
        self.comboBox.addItems(['Book Name', 'Author', 'Publisher', 'Category'])  # 검색 가능한 속성들 추가
        self.lineEdit_search = QLineEdit()
        self.searchButton = QPushButton('Search')
        self.searchButton.clicked.connect(self.searchBooks)  # 검색 버튼에 클릭 이벤트 연결

        # 검색 행 레이아웃 설정
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.comboBox)
        search_layout.addWidget(self.lineEdit_search)
        search_layout.addWidget(self.searchButton)

        # 테이블 위젯 설정
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Book Name', 'Author', 'Publisher', 'Category'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 예제 데이터 삽입
        for i in range(10):
            self.tableWidget.setItem(i, 0, QTableWidgetItem("Example Book " + str(i+1)))
            self.tableWidget.setItem(i, 1, QTableWidgetItem("Author " + str(i+1)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem("Publisher " + str(i+1)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem("Category " + str(i+1)))

        # 메인 레이아웃 설정
        layout = QVBoxLayout()
        layout.addLayout(search_layout)  # 검색 행 레이아웃을 메인 레이아웃에 추가
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)
        self.setWindowTitle('Book List')

        self.resize(1280, 720)  # 창 크기 설정

    def searchBooks(self):
        # 검색 로직 구현
        # 여기서는 검색 로직을 구현하지 않음 실제로 필요한 검색 기능을 여기에 추가
        print(f"Searching for {self.comboBox.currentText()} containing '{self.lineEdit_search.text()}'")

    def closeEvent(self, event):
        QApplication.quit()  # 도서 목록 창이 닫힐 때 애플리케이션을 종료
