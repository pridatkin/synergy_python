n = int(input("Enter the number of numbers: "))
array = list(map(int, input().split()))[:n]
s = set(array)
print(s)
