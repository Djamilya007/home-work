# class Mail:
# 	name = 'Джамиля'
# 	surname = "Магомедова"
# 	number = "89640037791"
# 	age = 18
# 	cart = False 
# 	def send(self):
# 		print("Хватит спамить!")
# human = Mail()
# print(human.age)
# human.send() #сокрощенная конструкция
# Mail.send(human)


class Mail:
	def __init__(self, name, surname):
		self.name = name
		self.surname = surname
	def send(self):
 		print("Хватит спамить!")

human = Mail("Джамиля", "Магомедова")
print(human.name)
human.send()

