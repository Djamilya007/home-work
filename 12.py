class Student:
	def __init__(self,name, surname, stud_id, score, omissions):
		self.name = name
		self.surname = surname
		self.stud_id = stud_id
		self.score = score
		self.omissions = omissions

	def check_in(self):
		self.name = input('Введите имя:')
		self.surname = input('Введите фамилию:')
		self.stud_id = int(input('Введите номер студ.билета:'))
		return self.name, self.surname, self.stud_id

	def log_in(self):
		self.stud_id = int(input('Введите номер студ.билета:'))
		return self.stud_id

	def getter(self):
		return 'Информация о среднем балле недоступна'

	def setter(self, value):
		print('Информация недоступна')
		score = property(getter, setter)

	def getter(self):
		return 'Информация о пропусках недоступна'

	def setter(self, value):
		print('Информация недоступна')
		omissions = property(getter, setter)


class Math(Student):
	def __init__(self, name, surname, stud_id, score, omissions, course, group):
		super().__init__(name, surname, stud_id, score, omissions)
		self.course = course
		self.group = group

	def schdule(self):
		print('Расписание мат.фак')

class Programming(Student):
	def __init__(self, name, surname, stud_id, score, omissions, course, group):
		super().__init__(name, surname, stud_id, score, omissions)
		self.сours = course
		self.group = group

	def schdule(self):
		print('Расписание инф.фак')

human = Student('Dzhamilya', 'Magomedova', '30405', '87', '5')
human_1 = Math('Dzhamilya', 'Magomedova', '30405', '87', '5', '1course', '4group')
human_2 = Programming('Dzhamilya', 'Magomedova', '30405', '87', '5', '1course', '4group')
human.check_in()
human.log_in()
human.schdule()
human_1.schdule()
human_2.schdule()
		



