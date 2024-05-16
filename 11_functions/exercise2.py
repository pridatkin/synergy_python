import collections

pets = {
	1:
		{
            "Мухтар": {
                "kind": "Собака",
                "age": 9,
                "owner": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "kind": "желторотый питон",
                "age": 19,
                "owner": "Саша"
            },
        },
}

def create():
	ID = collections.deque(pets, maxlen=1)[0] + 1
	pets[ID] = {}
	pets[ID] = {
		input("Введите имя питомца: "): {
			'kind': input("Введите вид питомца: "),
			'age': int(input("Введите возраст питомца: ")),
			'owner': input("Введите имя хозяина питомца: ")
		}
	}

def read():
	ID = int(input("Введите ID питомца: "))
	pet = get_pet(ID)
	if not pet:
		print("Нет питомца с таким ID")
	else:
		name = [x for x in pet.keys()][0]
		print(f"Это {pet[name]['kind']} по кличке: {name}. Возраст питомца: {pet[name]['age']} {get_suffix(pet[name]['age'])}. Имя владельца: {pet[name]['owner']}.")

def update():
	ID = int(input("Введите ID питомца: "))
	pet = get_pet(ID)
	if not pet:
		print("Нет питомца с таким ID")
	else:
		name = [x for x in pet.keys()][0]
		tmp = input("Введите вид питомца или оставьте поле пустым: ")
		if tmp:
			pet[name]['kind'] = tmp
		tmp = int(input("Введите возраст питомца или оставьте поле пустым: "))
		if tmp:
			pet[name]['age'] = tmp
		tmp = input("Введите имя хозяина питомца или оставьте поле пустым: ")
		if tmp:
			pet[name]['owner'] = tmp
						

def delete():
	ID = int(input("Введите ID питомца: "))
	pet = get_pet(ID)
	if not pet:
		print("Нет питомца с таким ID")
	else:
		pets.pop(ID)

def get_suffix(age):
	if age % 10 == 1 and age % 100 != 11:
		return 'год'
	elif 1 < age % 10 < 5 and age != 12 and age != 13 and age != 14:
		return 'года'
	else:
		return 'лет'

def get_pet(ID):
	return pets[ID] if ID in pets.keys() else False

def list_pets():
	for key, val in pets.items():
		print(f"ID:{key}", val)

def show_help():
	print("help\tвыводит эту справку")
	print("list\tвывести всех питомцев")
	print("create\tсоздать новую запись")
	print("read\tвывод информации о запрашиваемом питомце")
	print("update\tобновить информацию о питомце")
	print("delete\tудалить запись")
	print("stop\tвыйти")
	
commands = {
	'help': show_help,
	'list': list_pets,
	'create': create,
	'read': read,
	'update': update,
	'delete': delete,
	'stop': 0
}

command = ''

while command != 'stop':
	command = input("Введите команду (help для справки): ")
	if command == 'stop':
		break
	elif command not in commands.keys():
		print("Неизвестная команда, для справки введите help: ")
		continue
	commands[command]()
