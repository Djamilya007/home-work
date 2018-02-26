# count_wheel = 4
# engine  = True
# fuel = "oil"

# def ride():
# 	print("врум врум")

# name = "чайка"

class Car:
	count_wheel = 4
	engine = True
	fuel = "oil"

	def ride(self, speed):
		print(" врум врум " * speed)

seagull = Car()
print(seagull.count_wheel,seagull.fuel)
seagull.ride(3)

raphic = Car()
raphic.fuel = " молитвы пассажиров"
print("Рафики в качестве топлива использовали" + raphic.fuel)
raphic.ride(5)













