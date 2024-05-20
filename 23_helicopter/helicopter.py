from utils import randcell
import os

class Helicopter:
	def __init__(self, w, h):
		rc = randcell(w, h)
		rx, ry = rc[0], rc[1]
		self.x = rx
		self.y = ry
		self.h = h
		self.w = w
		self.tank = 0
		self.mxtank = 1
		self.score = 0
		self.lives = 20

	def move(self, dx, dy):
		nx, ny = self.x + dx, self.y + dy
		if nx >= 0 and ny >= 0 and nx < self.h and ny < self.w:
			self.x, self.y = nx, ny

	def print_stats(self):
		print(f"🪣💧 {self.tank}/{self.mxtank}", end = ' | ')
		print(f"🏆 {self.score}", end = ' | ')
		print(f"❤️ {self.lives}")

	def game_over(self):
		os.system("clear")
		print("*********************************")
		print("*                               *")
		print(f"* GAME OVER, YOUR SCORE IS {self.score}!\t*")
		print("*                               *")
		print("*********************************")
		exit(0)
	
	def export_data(self):
		return {'score': self.score,
				'lives': self.lives,
				'x': self.x,
				'y': self.y,
				'tank': self.tank,
				'mxtank': self.mxtank}

	def import_data(self, data):
		self.score = data['score'] or 0
		self.lives = data['lives'] or 20
		self.x = data['x'] or 0
		self.y = data['y'] or o
		self.tank = data['tank'] or 0
		self.mxtank = data['mxtank'] or 1
