class MagicPerson:
	def __init__(self,favourite_weapon,areal, damage, hp):
		self.favourite_weapon = favourite_weapon
		self.areal = areal
		self.damage = damage
		self.hp = hp

	def fight(self):
		print('Бью сильно!'*self.damage)

class Elf(MagicPerson):
	def __init__(self,favourite_weapon,areal, damage, hp):
		super().__init__()