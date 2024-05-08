#a = 46275
a = int(input("Enter the five-digit value: "))
res = (a % 100 // 10) ** (a % 10) * (a % 1000 // 100) / (a // 10000 - a % 10000 // 1000)
print(res)
