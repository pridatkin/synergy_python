n = int(input("Enter the number: "))
temp = n
counter0 = 1
counter1 = 0

for i in range(2, int(n ** 0.5) + 2):
	while temp % i == 0:
		counter1 += 1
		temp /= i
	if counter1 != 0:
		print(f"{i}\t{counter1}")
	counter0 *= counter1 + 1	
	counter1 = 0

#for i in range(n // 2 + 1):
#	if n % (i + 1) == 0:
#		count += 1
#		#print(i + 1)

print(f"The number of integer divisors of the number {n} is {counter0}")
