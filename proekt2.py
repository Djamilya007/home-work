import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QGridLayout , QLabel, QLineEdit
from PyQt5.QtWidgets import QMainWindow

class Multi(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		# первое окно
		self.firstWindow = QWidget(self)
		grid1 = QGridLayout() 
		grid1.setSpacing(20)

		self.textBlock = QLabel('')
		self.slideBtn1 = QPushButton('регистрация', self)
		self.slideBtn1.clicked.connect(self.Next1)

		grid1.addWidget(self.textBlock, 0, 0)
		grid1.addWidget(self.slideBtn1, 0, 1)


		self.textBlock = QLabel('')
		self.slideBtn2 = QPushButton('авторизация', self)
		self.slideBtn2.clicked.connect(self.Next)

		grid1.addWidget(self.textBlock, 0, 0)
		grid1.addWidget(self.slideBtn2, 0, 0)

		self.setGeometry(100, 100, 450, 250)
		self.setWindowTitle('Добро пожаловать')


		# второе окно
		self.secondWindow = QWidget(self)
		grid2 = QGridLayout() 
		grid2.setSpacing(20)

		self.nameBlock2 = QLabel('введите фамилию и имя')
		self.nameInput2 = QLineEdit(self)
		
		self.button = QPushButton('отправить', self)
		self.button.clicked.connect(self.sendForm)

		grid2.addWidget(self.nameBlock2, 0, 0)
		grid2.addWidget(self.nameInput2, 1, 0)
		grid2.addWidget(self.button, 2, 0)		

		self.firstWindow.setLayout(grid1)
		self.secondWindow.setLayout(grid2)

		self.setCentralWidget(self.firstWindow)


		self.setGeometry(100, 100, 450, 250)
		self.setWindowTitle('Авторизация')

		self.setLayout(grid1)
		self.setLayout(grid2)

		self.show()


		#третье окно
		self.thirdWindow = QWidget(self)
		grid3 = QGridLayout() 
		grid3.setSpacing(20)

		self.nameBlock3 = QLabel('Введите фамилию и имя')
		self.nameInput3 = QLineEdit(self)
		
		self.ageBlock = QLabel('Введите возраст')
		self.ageInput = QLineEdit(self)

		self.genderBlock = QLabel('Ваш класс')
		self.genderInput = QLineEdit(self)

		self.button = QPushButton('отправить', self)
		
		self.button.clicked.connect(self.sendForm1)

		grid3.addWidget(self.nameBlock3, 0, 0)
		grid3.addWidget(self.nameInput3, 1, 0)
		grid3.addWidget(self.ageBlock, 2, 0)
		grid3.addWidget(self.ageInput, 3, 0)
		grid3.addWidget(self.genderBlock, 4, 0)
		grid3.addWidget(self.genderInput, 5, 0)
		grid3.addWidget(self.button, 6, 0)		

		self.setGeometry(100, 100, 450, 250)
		self.setWindowTitle('Регистрация')

		self.thirdWindow.setLayout(grid3)
		self.setCentralWidget(self.firstWindow)
		self.setLayout(grid3)
		self.show()



		#четветое окно
		self.testWindow = QWidget(self)
		grid4 = QGridLayout() 
		grid4.setSpacing(20)

		self.testBlock = QLabel('')
		self.testBtn1 = QPushButton('тест по английскому №1', self)
		self.testBtn1.clicked.connect(self.test2)

		grid4.addWidget(self.testBlock, 0, 0)
		grid4.addWidget(self.testBtn1, 0, 1)


		self.testBlock = QLabel('Узнай свой уровень')
		self.testBtn2 = QPushButton('1.Тест по английскому №2', self)
		self.testBtn2.clicked.connect(self.test1)

		grid4.addWidget(self.testBlock, 0, 0)
		grid4.addWidget(self.testBtn2, 0, 0)

		self.setGeometry(100, 100, 450, 250)
		self.setWindowTitle('Тесты')

		self.testWindow.setLayout(grid4)

		self.setLayout(grid4)
		#пятое окно
		self.firstTestWindow = QWidget(self)
		grid5 = QGridLayout() 
		grid5.setSpacing(20)

		self.question1 = QLabel('''Where... you from?''')
		self.answer1 = QPushButton('''are''',self)
		self.answer1.clicked.connect(self.test1)
		grid5.addWidget(self.question1, 0, 0)
		grid5.addWidget(self.answer1, 0, 0)


		self.answer7 = QPushButton('''is''',self)
		self.answer7.clicked.connect(self.test1)
		grid5.addWidget(self.question1, 0, 0)
		grid5.addWidget(self.answer7, 1, 0)


		self.answer8 = QPushButton('''am''',self)
		self.answer8.clicked.connect(self.test1)
		grid5.addWidget(self.question1, 0, 0)
		grid5.addWidget(self.answer8, 0, 1)
		

		self.question2 = QLabel('''How old ...you?
			1)am, 2)is, 3)are''')
		self.answer2 = QLineEdit(self)		

		self.question3 = QLabel('''What ... your name
			1)am, 2)is, 3)are''')
		self.answer3 = QLineEdit(self)

		self.question4 = QLabel('''I ... glad to see you
			1)am, 2)is, 3)are''')
		self.answer4 = QLineEdit(self)
		self.completion1 = QPushButton('Завершить тест', self)
		self.completion1.clicked.connect(self.sendResult1)

		grid5.addWidget(self.question1, 0, 0)
		grid5.addWidget(self.answer1, 1, 0)
		grid5.addWidget(self.question2, 2, 0)
		grid5.addWidget(self.answer2, 3, 0)
		grid5.addWidget(self.question3, 4, 0)
		grid5.addWidget(self.answer3, 5, 0)
		grid5.addWidget(self.question4, 6, 0)
		grid5.addWidget(self.answer4, 7, 0)
		grid5.addWidget(self.completion1, 8, 0)



		self.firstTestWindow.setLayout(grid5)	

		self.setLayout(grid5)



		#шестое окно
		self.secondTestWindow = QWidget(self)
		grid6 = QGridLayout() 
		grid6.setSpacing(20)

		self.question_1 = QLabel('''How... you
			1)am, 2)is,are''')
		self.answer_1 = QLineEdit(self)

		self.question_2 = QLabel('''The dog... in the garden
			1)am, 2)is, 3)are''')
		self.answer_2 = QLineEdit(self)

		self.question_3 = QLabel('''My parents... workers
			1)am, 2)is, 3)are''')
		self.answer_3 = QLineEdit(self)
		self.question_4 = QLabel('''He ... not an engineer, he... a doctor
			1)am, 2)is, 3)are''')
		self.answer_4 = QLineEdit(self)

		self.completion2 = QPushButton('Завершить тест', self)
		self.completion2.clicked.connect(self.sendResult2)
 
		grid6.addWidget(self.question_1, 0, 0)
		grid6.addWidget(self.answer_1, 1, 0)
		grid6.addWidget(self.question_2, 2, 0)
		grid6.addWidget(self.answer_2, 3, 0)
		grid6.addWidget(self.question_3, 4, 0)
		grid6.addWidget(self.answer_3, 5, 0)
		grid6.addWidget(self.question_4, 6, 0)
		grid6.addWidget(self.answer_4, 7, 0)
		grid6.addWidget(self.completion2, 8, 0)


		self.secondTestWindow.setLayout(grid6)


		self.setLayout(grid6)

	def Next(self):
		self.setCentralWidget(self.secondWindow)

	def Next1(self):
		self.setCentralWidget(self.thirdWindow)

	def sendForm(self):
		f = open('Список пользователей2.txt','r') 
		list_of_name = f.read() 
		if self.nameInput2.text() in list_of_name: 
			self.nameBlock2.setText('Добро пожаловать!') 
			self.setCentralWidget(self.testWindow)
		else: 
			self.nameBlock2.setText('Вас нет в списке') 
		f.close() 
		self.nameInput2.setText('') 


	def sendForm1(self): 
		f = open('Список пользователей.txt', 'a')
		f.write(self.nameInput3.text()+ '\n')
		f.write(self.ageInput.text()+ '\n')
		f.write(self.genderInput.text()+ '\n')
		f.close() 
		self.setCentralWidget(self.testWindow)

	def sendResult1(self):
		f = open('Результаты пользователей.txt', 'a')
		f.write(self.answer1.text() + self.answer2.text() + self.answer3.text()+ self.answer4.text()+ '\n')
		f.close() 
		self.setCentralWidget(self.firstTestWindow)

	def sendResult2(self): 
		f = open('Результаты пользователей.txt', 'a')
		f.write(self.answer_1.text() + self.answer_2.text() + self.answer_3.text()+ self.answer_4.text()+ '\n')
		f.close() 

	def test1(self):
		self.setCentralWidget(self.firstTestWindow)


	def test2(self):
		self.setCentralWidget(self.secondTestWindow)


	def result(self):
		f = open('Результаты пользователей.txt','r') 
		list_of_result = f.read() 
		if self.nameInput2.text() in list_of_name: 
			self.nameBlock2.setText('Добро пожаловать!') 
			self.setCentralWidget(self.testWindow)
		else: 
			self.nameBlock2.setText('Вас нет в списке') 
		f.close() 


		self.nameInput3.setText('')
		self.ageInput.setText('')
		self.genderInput.setText('')
 


app = QApplication(sys.argv)
my_window = Multi()
sys.exit(app.exec_())