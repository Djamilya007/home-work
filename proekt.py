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

		# четвертое окно
		self.textWindow = QWidget(self)
		grid4 = QGridLayout() 
		grid4.setSpacing(20)

		self.testBlock = QLabel('')
		self.testBtn1 = QPushButton('Артикль', self)
		self.testBtn1.clicked.connect(self.test2)

		grid4.addWidget(self.testBlock, 0, 0)
		grid4.addWidget(self.testBtn1, 0, 1)

		self.testBlock = QLabel('')
		self.testBtn2 = QPushButton('Глаголы', self)
		self.testBtn2.clicked.connect(self.test1)

		grid4.addWidget(self.testBlock, 0, 0)
		grid4.addWidget(self.testBtn2, 0, 0)

		self.setGeometry(100, 100, 450, 250)
		self.setWindowTitle('Грамматика')
		self.textWindow.setLayout(grid4)
		self.setLayout(grid4)

		#пятое окно
		self.text1Window = QWidget(self)
		grid5 = QGridLayout() 
		grid5.setSpacing(20)

		self.textBlock4 = QLabel('''Артикль - это слово (или приставка, суффикс) ставящееся перед существительным, для его определения,
он указывает на уровень знакомства с существительным или на степень его уникальности.
Всего в английском три вида артиклей: "an" [ən], "a" [æ]  и "the" [ðə], которые делятся на две группы: "Неопределённые артикли" и "Определённые артикли".
Неопределённый артикль a/an употребляется:
1. Перед исчисляемым существительным в единственном числе, когда оно употребляется впервые: 
 I've seen a movie last evening. — Вчера вечером я посмотрел фильм. 
2. Перед исчисляемым существительным в единственном числе, когда оно обозначает представителя класса предметов: 
 A child needs love. — Ребёнок нуждается в любви. (т.е. все дети (любой ребёнок) нуждаются/нуждается). 
3. Когда существительное является частью составного именного сказуемого: 
 He is a talented writer. — Он талантливый писатель. 
4. В некоторых выражениях, обозначающих количество. Чаще всего — следующих: 
 a lot of… 
 a great many… 
 a great deal of… 
 a couple… 
 a dozen… 
 a way too… 
например: a way too much — слишком много 
5. В выражениях, обозначающих цену, скорость, и т.д., заменяя предлог per — в, за: 
5 dollars a kilo — 5 долларов за кг
Twice a day — дважды в день
20 km an hour — 20 км в час
6. В восклицаниях перед исчисляемым существительным в единственном числе:
What a pretty baby! — Какой хорошенький малыш!
7. Когда артикль можно заменить словом "one" (один): 
 Recently I've met a man. — Недавно я познакомилась с мужчиной. (можно сказать: с одним мужчиной). 
8. После quite, such
Such a wonderful day! — Такой чудесный день!


Обратите Ваше внимание на то, что неопределённый артикль не используется с именами собственными, но в редких случаях может употребляться перед Mr/Mrs/Miss + фамилия, обозначая, что человек не знаком говорящему: 
There's a Mrs. Newman to see you. — К вам пришла (некая) миссис Ньюмэн. 

Определённый артикль the употребляется:
1.С объектами, единственными в своём роде, такими как: 
The Earth — земля 
 The sea — море 
 The sky — небо 
 The stars — звезды 
 The Prime Minister — премьер министр 
 The Queen — королева 
2. Перед существительным, которое ранее уже употреблялось: 
 There was a man talking to a woman near my house. The man looked English but I think the woman was foreign. — Возле моего дома разговаривали какие-то мужчина и женщина. Мужчина был похож на англичанина, но женщина, я думаю, была иностранка. 
3. Перед существительным, после которого есть определение, выраженное фразой или придаточным предложением: 
 The girl in white was very attractive. — Девушка в белом была очень привлекательной. 
4. Перед прилагательным в превосходной степени (мы говорим о степени сравнения): 
 The highest place in the country. — Самое высокое место в стране. 
5. Перед порядковыми числительными (т.е. теми числительными, которые обозначают порядок при счёте и отвечают на вопросы: какой? который?) 
 She lives on the fifth floor. — Она живёт на пятом этаже. 
6. Перед only в значении "единственный": 
 She was the only beautiful woman in his life. — Она была единственной красивой женщиной в его жизни''')
		self.textInput4 = QLineEdit(self)

		self.completion1 = QPushButton('Закрыть', self)
		self.completion1.clicked.connect(self.Next2)

		grid5.addWidget(self.textBlock4, 0, 0)
		grid5.addWidget(self.textInput4, 1, 0)
		grid5.addWidget(self.completion1, 6, 0)     

		self.text1Window.setLayout(grid5)   
		self.setLayout(grid5)

		#шестое  окно
		self.text2Window = QWidget(self)
		grid6 = QGridLayout() 
		grid6.setSpacing(20)

		self.textBlock4 = QLabel('''Вce aнглийckиe глaгoлы paздeляют нa двe kaтeгopии:
Camocтoятeльныm глaгoлam хapakтepнo нaличиe лekcичeckoгo знaчeния; выpaжaют пpoизвoдиmoe дeйcтвиe либo cocтoяниe.
Cлyжeбныe глaгoлы cвoeгo знaчeния нe иmeют, a лишь пomoгaют в cтpoeнии гpammaтичeckих koнcтpykций и внocят яcнocть в знaчeниe camocтoятeльнoгo глaгoлa.
Виды cлyжeбных глaгoлoв
1.cвязkи, cлyжaщиe для oбpaзoвaния cлoжных глaгoлoв (linking verbs):
to be;
to get;
to become;
to look;
to keep etc.

2.moдaльныe — пomoгaют гoвopящemy выpaзить cвoe mнeниe kacaemo дeйcтвия (modal verbs):
may;
can;
need;
must;
ought etc.

3.вcпomoгaтeльныe — бeз них нeльзя oбpaзoвaть cocтaвнoe ckaзyemoe (auxiliary verbs):
to be;
to do;
to have;
will;

Вcпomoгaтeльный глaгoл to be
Для нacтoящeгo вpemeни — тpи фopmы, зaвиcящиe oт poдa и чиcлa: I am, he is, you/they are;
В пpoшeдшem вpemeни зaвиcит тoльko oт чиcлa, cooтвeтcтвeннo иmeeт двe фopmы: she was, you were;
Oтpицaтeльныe фopmы oбpaзoвывaют c пomoщью чacтичkи «not»: I am not, she is not, he was not, they were not;
В вoпpocaх вынocятcя в нaчaлo пpeдлoжeния: Is she? Were they? Was I

Глaгoл to do
Нacтoящee вpemя (двe фopmы): you/they do, it does;
Пpoшeдшee вpemя иmeeт eдинyю фopmy did;
Для coздaния oтpицaния нeoбхoдиmo дoбaвить чacтицy not (cokpaщeнный вapиaнт -n’t): I don’t, she does not, they didn’t;
Aнaлoгичнo пpeдыдyщemy глaгoлy вынocитьcя в нaчaлo вoпpoca: Do you? Did it?

Глaгoл to have
Фopmы нacтoящeгo вpemeни: I/you/they have, he/she/it has.
Для пpoшeдшeгo вpemeни иcпoльзyeтcя eдинaя фopma — had.
Oтpицaтeльнaя фopma тakжe c чacтичkoй «not/(-n’t)»: have not/haven’t, hasn’t. hadn’t.
Cтoит в нaчaлe вoпpocoв: Hashe? Had they? 
''')
		self.textInput5 = QLineEdit(self)

		self.completion2 = QPushButton('Закрыть', self)
		self.completion2.clicked.connect(self.Next3)
 
		grid5.addWidget(self.textBlock4, 0, 0)
		grid5.addWidget(self.textInput4, 1, 0)
		grid5.addWidget(self.completion1, 6, 0)     

		self.text2Window.setLayout(grid6)
		self.setLayout(grid6)

		#седьмое  окно
		self.testWindow = QWidget(self)
		grid7 = QGridLayout() 
		grid7.setSpacing(20)

		self.testBlock = QLabel('')
		self.testBtn1 = QPushButton('начальный', self)
		self.testBtn1.clicked.connect(self.test2)

		grid7.addWidget(self.testBlock, 0, 0)
		grid7.addWidget(self.testBtn1, 0, 1)


		self.testBlock = QLabel('Узнай свой уровень')
		self.testBtn2 = QPushButton('средний', self)
		self.testBtn2.clicked.connect(self.test1)

		grid7.addWidget(self.testBlock, 0, 0)
		grid7.addWidget(self.testBtn2, 0, 0)

		self.setGeometry(100, 100, 450, 250)
		self.setWindowTitle('Тесты')

		self.testWindow.setLayout(grid7)

		self.setLayout(grid7)

		#восьмое окно
		self.firstTestWindow = QWidget(self)
		grid8 = QGridLayout() 
		grid8.setSpacing(20)

		self.question1 = QLabel('''Where... you from?''')
		self.answer1 = QPushButton('''are''',self)
		self.answer1.clicked.connect(self.test1)
		grid8.addWidget(self.question1, 0, 0)
		grid8.addWidget(self.answer1, 0, 0)


		self.answer7 = QPushButton('''is''',self)
		self.answer7.clicked.connect(self.test1)
		grid8.addWidget(self.question1, 0, 0)
		grid8.addWidget(self.answer7, 1, 0)


		self.answer8 = QPushButton('''am''',self)
		self.answer8.clicked.connect(self.test1)
		grid8.addWidget(self.question1, 0, 0)
		grid8.addWidget(self.answer8, 0, 1)
		

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

		grid8.addWidget(self.question1, 0, 0)
		grid8.addWidget(self.answer1, 1, 0)
		grid8.addWidget(self.question2, 2, 0)
		grid8.addWidget(self.answer2, 3, 0)
		grid8.addWidget(self.question3, 4, 0)
		grid8.addWidget(self.answer3, 5, 0)
		grid8.addWidget(self.question4, 6, 0)
		grid8.addWidget(self.answer4, 7, 0)
		grid8.addWidget(self.completion1, 8, 0)



		self.firstTestWindow.setLayout(grid8)   
		self.setLayout(grid8)

		#девятое окно
		self.secondTestWindow = QWidget(self)
		grid9 = QGridLayout() 
		grid9.setSpacing(20)

		self.question_1 = QLabel('''I _______ the Star Wars films.  
		A) have never seen  B) have ever seen  C) have never saw ''')
		self.answer_1 = QLineEdit(self)

		self.question_2 = QLabel('''They_____ for Google_____2004.  
		A) worked / for  B) ’ve worked / since  C) ’re working / since ''')
		self.answer_2 = QLineEdit(self)

		self.question_3 = QLabel('''____Neil_____ that he didn’t get the job?  
		A) Did / tell  B) Have / told  C) Has / been told ''')
		self.answer_3 = QLineEdit(self)
		self.question_4 = QLabel('''    If you ______ that expensive car, you ___ enough money to go on holiday.  
		A) buy / won’t have  B) bought / don’t have  C) don’t buy / won’t have ''')
		self.answer_4 = QLineEdit(self)

		self.completion2 = QPushButton('Завершить тест', self)
		self.completion2.clicked.connect(self.sendResult2)
 
		grid9.addWidget(self.question_1, 0, 0)
		grid9.addWidget(self.answer_1, 1, 0)
		grid9.addWidget(self.question_2, 2, 0)
		grid9.addWidget(self.answer_2, 3, 0)
		grid9.addWidget(self.question_3, 4, 0)
		grid9.addWidget(self.answer_3, 5, 0)
		grid9.addWidget(self.question_4, 6, 0)
		grid9.addWidget(self.answer_4, 7, 0)
		grid9.addWidget(self.completion2, 8, 0)


		self.secondTestWindow.setLayout(grid9)
		self.setLayout(grid9)

	def Next(self):
		self.setCentralWidget(self.secondWindow)

	def Next1(self):
		self.setCentralWidget(self.thirdWindow)

	def Next2(self):
		self.setCentralWidget(self.firstTestWindow)

	def Next3(self):
		self.setCentralWidget(self.secondTestWindow)


	



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
