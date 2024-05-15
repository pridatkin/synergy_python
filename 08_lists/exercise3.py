m = int(input("Enter the tonnage of the boat: "))
n = int(input("enter the number of fishermen: "))
counter = 0
weight = []

for i in range(n):
	weight.append(int(input(f"Enter the weight of the fisherman {i + 1} :")))	

	if weight[-1] > m:
		print("The weight of the fisherman is greater than the tonnage of the boat!")
		exit(0)

weight.sort()

while len(weight) != 0:
	if len(weight) > 1 and (weight[0] + weight[-1]) <= m:
		weight.pop(0)
	counter += 1
	weight.pop()

print(f"{counter} boats are needed to transport all fishermen")
		
