n = int(input("Enter the number of values: "))
array = list(map(int, input().split()))[:n]
print("Source array:\t", array)
array.insert(0, array.pop())
print("Modified array\t", array)
