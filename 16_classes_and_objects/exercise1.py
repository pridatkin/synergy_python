class Till(object):
	money = 0
	
	def top_up(self, money):
		self.money += money

	def count_1000(self):
		print(f"There are {self.money // 1000} thousand left in the cash register")

	def take_away(self, money):
		if self.money < money:
			print("Not enough money")
		else:
			self.money -= money

#c = Till()
#c.count_1000()	
#c.top_up(5000)
#c.count_1000()
#c.take_away(8000)
#c.count_1000()
#c.take_away(3000)
#c.count_1000()
