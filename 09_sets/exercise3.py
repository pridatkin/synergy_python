s = set()
for i in input().split():
	if i in s:
		print(f"{i} YES")
	else:
		print(f"{i} NO")
		s.add(i)	
