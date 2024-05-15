pets = {}
name = input("Введите имя питомца: ")
kind =input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя хозяина питомца: ")

pets[name] = {
	'kind': kind,
	'age': age,
	'owner': owner
}

year = 'лет'
if age % 10 == 1 and age % 100 != 11:
	year = 'год'
elif 1 < age % 10 < 5 and age != 12 and age != 13 and age != 14:
	year = 'года'

print(f"Это {pets[name]['kind']} по кличке: {name}. Возраст питомца: {pets[name]['age']} {year}. Имя владельца: {pets[name]['owner']}.")
