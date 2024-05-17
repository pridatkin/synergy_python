class Turtle(object):
	x = 0
	y = 0
	s = 1

	def	__init__(self, x, y, s):
		self.x = x
		self.y = y
		self.s = s

	def go_up(self):
		self.y += self.s

	def go_down(self):
		self.y -= self.s

	def go_left(self):
		self.x -= self.s

	def go_right(self):
		self.x += self.s

	def evolve(self):
		self.s += 1

	def degrade(self):
		if self.s == 1:
			print("The minimum value has been reached")
		else:
			self.s -= 1

	def count_moves(self, x2, y2):
		return abs(self.x - x2) + abs(self.y - y2)
