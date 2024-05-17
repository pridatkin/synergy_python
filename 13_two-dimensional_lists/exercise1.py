import random

m = int(input("Enter the number of lines: "))
n = int(input("Enter the number of columns: "))

size = 10
mas1 = [[random.randint(1, 100) for i in range(n)] for i in range(m)]
mas2 = [[random.randint(1, 100) for i in range(n)] for i in range(m)]
mas3 = [[mas1[i][j] + mas2[i][j] for j in range(n)] for i in range(m)]

print("array1 = ")
for i in range(m):
	print(*mas1[i])

print()

print("array2 = ")
for i in range(m):
	print(*mas2[i])

print()

print("array1 + array2 = ")
for i in range(m):
	print(*mas3[i])
