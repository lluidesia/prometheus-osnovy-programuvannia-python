
def clean_list(list_to_clean):
	list_result=[]
	list_str=[]

	for item in list_to_clean:
		
		for i in list_result:
			
			if item not in list_result or str(item) != str(i):
				list_result.append(item)
				list_str.append(str(item))

	return list_result

'''
def clean_list(list_to_clean):
	list_result=[]
	list_str=[]

	for item in list_to_clean:
		if item not in list_result or str(item) not in list_str:
			list_result.append(item)
			list_str.append(str(item))

	return list_result

'''


#l_to=[1, 1.0, '1', -1, 1,1.0]
l_to=['asd', 'dsa', 1, '1', 1.0]
#l_to=[]
#l_to=['qwe', 'reg', 'qwe', 'REG']

print(clean_list(l_to))







