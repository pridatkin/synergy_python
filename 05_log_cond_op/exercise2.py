word = input("Enter the word: ")

a = 0
e = 0
i = 0
o = 0
u = 0
y = 0
cons = 0
vow = 0

for lit in word:
	if lit == 'a':
		a += 1
	elif lit == 'e':
		e += 1
	elif lit == 'i':
		i += 1
	elif lit == 'o':
		o += 1
	elif lit == 'u':
		u += 1
	elif lit == 'y':
		y += 1
	else:
		cons += 1

vow = a + e + i + o + u + y

print(f"Word \"{word}\" contains \n\
		{cons} consonant letters \n\
		{vow} vowel letters \n\
		{a} a letters \n\
		{e} e letters \n\
		{i} i letters \n\
		{o} o letters \n\
		{u} u letters \n\
		{y} y letters ")
