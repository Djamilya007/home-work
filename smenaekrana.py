import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout,QMainWindow


class Change(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.window1 = QWidget()
		grid = QGridLayout()
		grid.setSpacing(20)

		self.firstBtn = QPushButton("Нажми 1")
		self.secondBtn = QPushButton("Нажми 2")
		self.thirdBtn = QPushButton("Нажми 3")
		grid.addWidget(self.firstBtn,0,0)
		grid.addWidget(self.secondBtn,1,0)
		grid.addWidget(self.thirdBtn,2,0)
		self.firstBtn.clicked.connect(self.next)
		self.window1.setLayout(grid)

		# Второе окно

		self.window2 = QWidget()
		grid2 = QGridLayout()
		grid2.setSpacing(20)
		self.firstText = QLabel("Да пребудет с тобой сила")
		self.fourthBtn = QPushButton("Не работаает")
		grid2.addWidget(self.firstText,0,0)
		grid2.addWidget(self.fourthBtn,0,1)
		self.window2.setLayout(grid2)


		self.setCentralWidget(self.window1)


		self.setGeometry(100,100,700,500)
		self.setWindowTitle('Program')
		self.show()

	def next(self):
		self.setCentralWidget(self.window2)


app = QApplication(sys.argv)
my_window = Change()
sys.exit(app.exec_())



