my_list = [] 
print(list('строка'))
my_list = [1,2,3]
print(my_list[0:2])
my_list[2] = '3'
print(my_list)
my_list[1] = [1.5, 2.5]
print(my_list)
print(my_list[1][0])

worlds = ['Warhammer','the lord of the rings','ds']
worlds.append('Vampire the Mascarade')
print(worlds)
worlds.insert(0, 'мечты Навального')
print(worlds)
anti_worlds = ['Ну, погоди', 'Наруто', 'Призрак в доспехах']
worlds.append(anime_worlds)
worlds.extend(anime_worlds)
print(worlds)
worlds.append('Призрак в доспехах')
print(worlds)
worlds.remove('Призрак в доспехах') #удаляет по значению
del worlds[-2] #удаляет по индексу
bred = worlds.pop(0)

worlds_copy.append('Ведьмак')
print(worlds)
print(worlds_copy)

list_of_numbers = [3,6,1,7,4,2,2,4,10]
print(list_of_numbers.sort())
print(max(list_of_numbers))
print(min(list_of_numbers