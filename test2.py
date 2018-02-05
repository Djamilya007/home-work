name = input("Введите свое имя:")
math = int(input("Какая у вас оценка:"))
physics = int(input("Какая у вас оценка:"))
chemistry = int(input("Какая у вас оценка:"))
biology = int(input("Какая у вас оценка:"))
geography = int(input("Какая у вас оценка:"))
if int(input((math + physics + chemistry + biology + geography)/5) == 4,8):
    print("Вы нам подходите")
else:
	print("Работайте над собой")