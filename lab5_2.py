def counter(a, b):
	b_str=str(b)
	a_str=str(a)
	b_str_one=[]
	a_str_one=[]
	for item in b_str:
		if item not in b_str_one:
			b_str_one.append(item)

	for item in a_str:
		if item not in a_str_one:
			a_str_one.append(item)

	i=0
	for item in a_str_one:
		if item in b_str_one:
			i=i+1

	return i


print(counter(123, 45))


