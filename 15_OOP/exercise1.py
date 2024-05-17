class Transport:
	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

class Bus(Transport):
	def __inint__(self, name, max_speed, mileage):
		super().__init__(name, max_speed, mileage)
	
	def __str__(self):
		return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"

b1=Bus("Renault Logan", 180, 12)
print(b1)
