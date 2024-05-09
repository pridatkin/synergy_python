x = int(input("Enter the minimum investment amount: "))
a = int(input("How many dollars does Mike have? "))
b = int(input("How many dollars does Ivan have? "))
if a >= x and b >= x:
	print(2)
elif a >= x and b < x:
	print("Mike")
elif a < x and b >= x:
	print("Ivan")
elif (a + b) >= x:
	print(1)
else:
	print(0)
