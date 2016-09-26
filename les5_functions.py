#Отже, ми можемо взяти будь-яку частину коду, дати їй ім’я і винести з основного потоку програми. 
#Наприклад, програма, яка шукає на відрізку від 0 до 99 всі числа, записані однаковими цифрами, 
#може бути записана так:

print("#1") 
n=100
for x in range(n):
	is_cool = x<10 or (int(x/10)==x%10)
	print(x,is_cool)

#Або так:

print("\n#2")
def check_if_is_cool(number):
	is_cool=number<10 or (int(number/10)==number%10)
	print(number, is_cool)

n2=100
for x in range(n2):
	check_if_is_cool(x)

#Або взагалі так. І це буде найправильніший варіант, так як виведення даних має відношення до самої 
#програми і залишається в циклі, а в окрему функцію виноситься лише перевірка, 
#яка сама по собі може знадобитися і в іншому місці:
print("\n#3")
def is_cool_3(number):
	#limited by 0 <= number <= 99
	return number<10 or int(number/10)==number%10

n3=100
for x in range(n3):
	print(x, is_cool_3(x))

#Перепишемо попередню програму так, щоб вона шукала числа на проміжку, які діляться без остачі 
#на будь-які задані числа:
print("\nnew")
































