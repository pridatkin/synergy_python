value = int(input("Enter an integer: "))
if value == 0:
	print("Zero value")
elif value > 0 and value % 2 == 0:
	print("A positive even number")
elif value > 0 and value % 2 != 0:
	print("A positive odd number")
elif value < 0 and value % 2 == 0:
	print("A negative even number")
else:
	print("A negative odd number")
	
