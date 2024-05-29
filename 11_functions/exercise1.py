def fact(n):
	res = 1
	for i in range(n):
		res *= i + 1
	return res

n = int(input("Enter the value: "))
l = []
f = fact(n)
for i in range(f, 0, -1):
	l.append(fact(i))

print(f)
print(l)
