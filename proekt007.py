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

		
		#четвертое окно
		self.text1Window = QWidget(self)
		grid4 = QGridLayout() 
		grid4.setSpacing(20)

		self.textBlock4 = QLabel('''Артикль - это слово ставящееся перед существительным, для его определения,
он указывает на уровень знакомства с существительным или на степень его уникальности.
Всего в английском три вида артиклей: "an" [ən], "a" [æ]  и "the" [ðə], которые делятся на две группы:
"Неопределённые артикли" и "Определённые артикли".
Неопределённый артикль a/an употребляется:
1. Перед исчисляемым существительным в единственном числе, когда оно употребляется впервые. 
2. Перед исчисляемым существительным в единственном числе, когда оно обозначает представителя класса предметов.
3. Когда существительное является частью составного именного сказуемого.
4. В некоторых выражениях, обозначающих количество.  
5. В выражениях, обозначающих цену, скорость, и т.д.
6. В восклицаниях перед исчисляемым существительным в единственном числе.
7. Когда артикль можно заменить словом "one" (один).
8. После quite, such
Определённый артикль the употребляется:
1.С объектами, единственными в своём роде.
2. Перед существительным, которое ранее уже употреблялось
3. Перед существительным, после которого есть определение, выраженное фразой или придаточным предложением.
4. Перед прилагательным в превосходной степени.
5. Перед порядковыми числительными.
6. Перед only в значении "единственный"''')
		self.textInput4 = QLineEdit(self)

		self.completion1 = QPushButton('Далее', self)
		self.completion1.clicked.connect(self.Next2)

		grid4.addWidget(self.textBlock4, 0, 0)
		grid4.addWidget(self.textInput4, 1, 0)
		grid4.addWidget(self.completion1, 6, 0)     

		self.text1Window.setLayout(grid4)   
		self.setLayout(grid4)

		#пятое  окно
		self.text2Window = QWidget(self)
		grid5 = QGridLayout() 
		grid5.setSpacing(20)


		self.textInput5 = QLineEdit(self)

		self.completion2 = QPushButton('Закрыть', self)
		self.completion2.clicked.connect(self.Next3)
 
		grid5.addWidget(self.textBlock4, 0, 0)
		grid5.addWidget(self.textInput4, 1, 0)
		grid5.addWidget(self.completion1, 6, 0)     

		self.text2Window.setLayout(grid5)
		self.setLayout(grid5)

		#шестое  окно
		self.testWindow = QWidget(self)
		grid6 = QGridLayout() 
		grid6.setSpacing(20)

		self.testBlock = QLabel('Узнай свой уровень')
		self.testBtn2 = QPushButton('Пройти тест', self)
		self.testBtn2.clicked.connect(self.test1)

		grid6.addWidget(self.testBlock, 0, 0)
		grid6.addWidget(self.testBtn2, 0, 0)

		self.setGeometry(100, 100, 450, 250)
		self.setWindowTitle('Тесты')

		self.testWindow.setLayout(grid6)

		self.setLayout(grid6)

		#седьмое окно
		self.firstTestWindow = QWidget(self)
		grid7 = QGridLayout() 
		grid7.setSpacing(20)

		self.question1 = QLabel('''Where... you from?''')

		self.answer1 = QPushButton('''are''',self)
		self.answer1.clicked.connect(self.test1)
		grid7.addWidget(self.question1, 0, 0)
		grid7.addWidget(self.answer1, 0, 2)

		self.answer2 = QPushButton('''is''',self)
		self.answer2.clicked.connect(self.test1)
		grid7.addWidget(self.question1, 0, 0)
		grid7.addWidget(self.answer2, 0, 3)

		self.answer3 = QPushButton('''am''',self)
		self.answer3.clicked.connect(self.test1)
		grid7.addWidget(self.question1, 0, 0)
		grid7.addWidget(self.answer3, 0, 1)
		

		self.question2 = QLabel('''How old ...you?''')

		self.answer1 = QPushButton('''am''',self)
		self.answer1.clicked.connect(self.test1)
		grid7.addWidget(self.question2, 2, 0)
		grid7.addWidget(self.answer1, 2, 1)

		self.answer2 = QPushButton('''are''',self)
		self.answer2.clicked.connect(self.test1)
		grid7.addWidget(self.question2, 2,0)
		grid7.addWidget(self.answer2, 2, 2)

		self.answer3 = QPushButton('''is''',self)
		self.answer3.clicked.connect(self.test1)
		grid7.addWidget(self.question2, 2,0)
		grid7.addWidget(self.answer3, 2, 3)
	 

		self.question3 = QLabel('''What ... your name''')

		self.answer1 = QPushButton('''am''',self)
		self.answer1.clicked.connect(self.test1)
		grid7.addWidget(self.question3, 3, 0)
		grid7.addWidget(self.answer1, 3, 1)

		self.answer2 = QPushButton('''are''',self)
		self.answer2.clicked.connect(self.test1)
		grid7.addWidget(self.question3, 3,0)
		grid7.addWidget(self.answer2, 3, 2)

		self.answer3 = QPushButton('''is''',self)
		self.answer3.clicked.connect(self.test1)
		grid7.addWidget(self.question3, 3,0)
		grid7.addWidget(self.answer3, 3, 3)


		self.question4 = QLabel('''I ... glad to see you''')

		self.answer1 = QPushButton('''are''',self)
		self.answer1.clicked.connect(self.test1)
		grid7.addWidget(self.question4, 4,0)
		grid7.addWidget(self.answer1, 4, 1)

		self.answer2 = QPushButton('''am''',self)
		self.answer2.clicked.connect(self.test1)
		grid7.addWidget(self.question4, 4,0)
		grid7.addWidget(self.answer2, 4, 2)


		self.answer3 = QPushButton('''is''',self)
		self.answer3.clicked.connect(self.test1)
		grid7.addWidget(self.question4, 4,0)
		grid7.addWidget(self.answer3, 4, 3)

		
		self.question5 = QLabel('''...Igor a good chess player?''')

		self.answer1 = QPushButton('''am''',self)
		self.answer1.clicked.connect(self.test1)
		grid7.addWidget(self.question5, 5, 0)
		grid7.addWidget(self.answer1, 5, 1)

		self.answer2 = QPushButton('''are''',self)
		self.answer2.clicked.connect(self.test1)
		grid7.addWidget(self.question5, 5,0)
		grid7.addWidget(self.answer2, 5, 2)

		self.answer3 = QPushButton('''is''',self)
		self.answer3.clicked.connect(self.test1)
		grid7.addWidget(self.question5, 5,0)
		grid7.addWidget(self.answer3, 5, 3)

		self.completion1 = QPushButton('Завершить тест', self)
		self.completion1.clicked.connect(self.sendResult1)

		grid7.addWidget(self.question1, 0, 0)
		grid7.addWidget(self.answer1, 1, 0)
		grid7.addWidget(self.question2, 2, 0)
		grid7.addWidget(self.answer2, 3, 0)
		grid7.addWidget(self.question3, 4, 0)
		grid7.addWidget(self.answer3, 5, 0)
		grid7.addWidget(self.question4, 6, 0)
		grid7.addWidget(self.answer4, 7, 0)
		grid7.addWidget(self.completion1, 8, 0)

		self.firstTestWindow.setLayout(grid7)   
		self.setLayout(grid7)

		
	def Next(self):
		self.setCentralWidget(self.secondWindow)

	def Next1(self):
		self.setCentralWidget(self.thirdWindow)

	# def Next2(self):
	# 	self.setCentralWidget(self.text1Window)

	# def Next3(self):
	# 	self.setCentralWidget(self.text2Window)

	def Next2(self):
		self.setCentralWidget(self.testWindow)

	def Next3(self):
		self.setCentralWidget(self.testWindow)


	def sendForm(self):
		f = open('Список пользователей.txt','r') 
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
		self.setCentralWidget(self.text1Window)

	def sendResult1(self):
		f = open('Результаты пользователей.txt', 'a')
		f.write(self.answer1.text() + self.answer2.text() + self.answer3.text()+ self.answer4.text()+ '\n')
		f.close() 
		self.setCentralWidget(self.firstTestWindow)

	# def sendResult2(self): 
	# 	f = open('Результаты пользователей.txt', 'a')
	# 	f.write(self.answer_1.text() + self.answer_2.text() + self.answer_3.text()+ self.answer_4.text()+ '\n')
	# 	f.close() 

	def test1(self):
		self.setCentralWidget(self.firstTestWindow)


	# def test2(self):
	# 	self.setCentralWidget(self.secondTestWindow)


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
