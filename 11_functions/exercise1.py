def fact(n):
	res = 1
	for i in range(n):
		res *= i + 1
	return res

n = int(input("Enter the value: "))
l = []
for i in range(n, 0, -1):
	l.append(fact(i))

print(l)
