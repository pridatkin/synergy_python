class Transport:
	def __init__(self, name, max_speed, mileage):
		self.name = name
		self.max_speed = max_speed
		self.mileage = mileage

t1=Transport("Renault Logan", 180, 12)
print(f"Название автомобиля: {t1.name} Скорость: {t1.max_speed} Пробег: {t1.mileage}")


