def show_em_all(func):

	def wrapper(*args, **kwargs):

		print("Название функции:", func.__name__)
		print("Позиционные аргументы:", args)
		print("Именнованные аргументы:", kwargs)
		result = func(*args, ** kwargs)
		print("Результат", result)
		return result

	return wrapper

# def summ6(a,b):
# 	return( a + b) * 6

# def loh_you(name):
# 	print(name +", поздравляю, ты лох")

# nice_summ6 = show_em_all(summ6)
# print(summ6(5,5))
# print(nice_summ6(6,6))

def no(func):

	def wrapper(*args, **kwargs):
		return str(func(*args, **kwargs)) + "(НЕТ)"
	return wrapper

@show_em_all
@no

def you_pretty(name):
	return name + " красавчик"
print(you_pretty("Камал"))

  
super_funce = lambda a, b: a + " " + b + "Амин"

print(super_funce("Мир", "Труд"))
good_boys = ["Аслан", "Арслан", "Джаливито", "Саид-постигнувший"]

good_boys.sort(key = lambda e: e.lower())
print(good_boys)