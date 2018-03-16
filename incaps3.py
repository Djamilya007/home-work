class Trump:
	def __init__(self, love_to_mexican, hair, money):
		self.love_to_mexican = love_to_mexican
		self.hair = hair
		self.__money = money

	def get_money(self):
		print('Ха-ха, обойдешься без новой шубы')
		return 'Вызвался getter'

	def set_money(self, value):
		print('Хватит тырить бабки')

	money = property(get_money, set_money)

little_Trump = Trump(False, 'Best', 40000000000)

# print(little_Trump.money)
# print(little_Trump.__money)
little_Trump.money = 200000000000
# Джамиля - королева всея Руси, а также лучший программист во Вселенной