my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def rec_print(l):
	if l:
		print(l.pop(0))
		rec_print(l)
	else:
		print("End of list")

rec_print(my_list)
