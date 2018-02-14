import random

def create():
	person = {
'hp':100,
'damage':30
}
	person['name'] = input('Введите имя персонажа:')
	cho = int(input("""Выберите бонус
		1- прибавка к здоровью,
		2- прибавка к урону:"""))
	if cho == 1:
		person['hp'] +=30
	else:
		person['damage'] += 9
	return person

player_1 = create()
player_2 = create()

def fight(damager, defender):
	real_damage = damage['damage'] + random.randint(-3,3)
	print(damager['name'],' наносит',real_damage, 'урона',defender['name'])
	defender['hp'] -= real_damage
def health_info(person):
	print('У', person[name], 'осталось', person['hp'],'здоровья')
player_1 = create()
player_2 = create()

while True:
	fight(player_1, player_2)
	fight(player_2, player_1)

# player_1 = {
# 'hp':100,
# 'damage':30
# }
# player_2 = {
# 'hp':100,
# 'damage':30
# }
# player_3 = {
# 'hp':100,
# 'damage':30
# }
# player_4 = {
# 'hp':100,
# 'damage':30
# }
# player_1['name'] = input("Введите имя первого персонажа")
# player_2['name'] = input("Введите имя второго персонажа")
# player_3['name'] = input("Введите имя третьего персонажа")
# player_4['name'] = input("Введите имя четвертого персонажа")

# while True:
# 	print(player_1['name'] ,'атакует', player_2['name'] )
# 	player_2['hp'] -= player_1['damage'] + random.randint(-3,3)
# 	print(player_2['name'], 'атакует', player_1)
# 	player_1['hp'] -= player_2['damage'] + random.randint(-3,3)
# 	print(player_4,'атакует', player_3['name'])
# 	player_4['hp'] -= player_3['damage'] + random.randint(-3,3)
# 	print(player_3, 'атакует', player_4)
# 	player_3['hp'] -= player_4['damage'] + random.randint(-3,3)