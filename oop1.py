# -*- coding: utf-8 -*-
class Person:
	def __init__(self, name, age, job, pay):
		self.name = name
		self.age = age
		self.job = job
		self.pay = pay
	def lastName(self):
	 	return self.name.split()[-1]
	def __str__(self):
	 	return '[Person: %s, %s]' % (self.name, self.pay)
 
ivan = Person('Иван Petrov', 22, 'Apple', 2500000)
john = Person('John Sidorov', 24, 'ФСБ', 1000000)
print(ivan.age)
print(john.name)
print(ivan.lastName(), john.lastName())




