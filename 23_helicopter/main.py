from pynput import keyboard
from map import Map
from clouds import Clouds
from helicopter import Helicopter
import time
import json
import os

TICK_SLEEP = 0.1
TREE_UPDATE = 50
CLOUDS_UPDATE = 100
FIRE_UPDATE = 50
MAP_W, MAP_H = 20, 10

field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helicopter(MAP_W, MAP_H)
tick = 1
exit_game = False

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
# f - сохранение, g - восстановление

def process_key(key):
	global helico, clouds, field, tick, exit_game
	try:
		c = key.char.lower()
		if c in MOVES.keys():
			dx, dy = MOVES[c][0], MOVES[c][1]
			helico.move(dx, dy)	
		elif c == 'f':
			print('save')
			data = {'helicopter': helico.export_data(),
					'clouds': clouds.export_data(),
					'field': field.export_data(),
					'tick': tick}
			with open('level.json', 'w') as lvl:
				json.dump(data, lvl)
		elif c == 'g':
			try:
				lvl = open('level.json', 'r')
				data = json.load(lvl)
				tick = data['tick'] or 1
				helico.import_data(data['helicopter'])
				clouds.import_data(data['clouds'])
				field.import_data(data['field'])
			except Exception:
				pass

	except AttributeError:
		if key == keyboard.Key.esc:
			exit_game = True
    #print('{0} released'.format(
    #    key))
    #if key == keyboard.Key.esc:
    #    return False

listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()

while exit_game == False:
	os.system("clear") #cls for Windows
	print("TICK", tick)
	field.process_helicopter(helico, clouds)
	helico.print_stats()
	field.print_map(helico, clouds)
	tick += 1
	time.sleep(TICK_SLEEP)
	if tick % TREE_UPDATE == 0:
		field.generate_tree()
	if tick % FIRE_UPDATE == 0:
		field.update_fires()
	if tick % CLOUDS_UPDATE == 0:
		clouds.update()

