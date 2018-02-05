list_of_visits = input('Введите список гостей:').split(',')
# list_of_visits = list_of_visits.split(', ')
# print(list_of_visits)

# man_list = ['Малик','Магомедамин','Рашид']
# print(' '.join(man_list))
# name = input('Представьтесь пожалуйста.:')
# if name in list_of_visits:
    # print("Добро пожаловать")
# else:
	# print("вон отсюда")
# k = 1
for i in list_of_visits:
    # print(str(k) + ')',i)
	# k +=1
	if i == 'Джамиля':
		print("Рады видеть вас, наша Королева")
		break
else:
	print("Не дыши тут")
		
# for i in range(1,10000000000000000000000000000):
# 	print(i)
# 	pass


dict_of_prog_lang = {
	'Java': 'Android, Desktop',
	'C': 'Hardware , Desktop',
	'Pascal':None,
	'C#':'Desktop, Unity'
}
lang = input("Введи название языка:")
work = input("Где нужен:")
# for i in dict_of_prog_lang.items():
print(lang, work in zip('Java','Android, Desktop',))