n = int(input("Enter the number of values: "))
array = []
for i in range(n):
	array.append(int(input()))
print("Source array:\t", array)
print("Inverted array\t", array[::-1])
