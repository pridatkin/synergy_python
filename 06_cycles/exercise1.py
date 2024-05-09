n = int(input("Enter the number of numbers: "))
count = 0
for i in range(n):
	if int(input()) == 0:
		count += 1

print("The number of zeros is ", count)
