# -*- coding: utf-8 -*-
class Person:
	def __init__(self, name, job=None, pay=0, age = 0):
		self.name = name
		self.job = job
		self.pay = pay
		self.age = age
	def lastName(self):
		return self.name.split()[-1]
	def __str__(self):
	 	return '[Person: %s, %s]' % (self.name, self.pay)
 
ivan = Person('Иван Petrov')
john = Person('John Sidorov', job='ФСБ', pay=1000000)
print(ivan)
print(john)
print(ivan.lastName(), john.lastName())




