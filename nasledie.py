class Hero:
	def __init__(self, strength, vulnerability, team, side):
		self.strength = strength
		self.vulnerability = vulnerability
		self.team = team
		self.side = side

	def punch(self):
		return self.strength

	def save(self):
		print("Боже,храни Америку!")

class X_men(Hero):
	def fly(self):
		print("Палундра!!!")
class New_x_men(X_men):
	def __init__(self, strength, vulnerability, team, side, teacher):
		# self.strength = strength
		# self.vulnerability = vulnerability
		# self.team = team
		# self.side = side
		# self.teacher = teacher
		super().__init__(strength, vulnerability, team, side)
		self.teacher = teacher
	def fly(self):
		print("Свистать всех наверх")

superman = Hero(500, 'криптонит', 'лига справедливости', True)
fenix = New_x_men(1000, None, None, None, "Профессор К")
logan = X_men(100, "алкоголизм", 'люди икс', True)
print(logan.team)
logan.save()
print(fenix.strength)
fenix.fly()
# superman.fly()
print(fenix.teacher)