import sys
from PyQt5.QtWidgets import QApplication, QWidget 
from PyQt5.QtGui import QIcon

class My_GUI(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		self.setGeometry(100, 100, 300, 300)
		self.setWindowTitle('peri')
		self.setWindowIcon(QIcon('WIN_20180131_11_23_12_Pro.jpg'))
		self.show()

app = QApplication(sys.argv)
my_window = My_GUI()
sys.exit(app.exec_())