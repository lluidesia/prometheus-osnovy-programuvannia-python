'''
Розробити функцію convert_n_to_m(x, n, m), 
яка приймає 3 аргументи -- ціле число (в системі числення з основою n) або рядок x, що представляє таке число, та цілі числа n та m (1 <= n, m <= 36), 
та повертає рядок -- представлення числа х у системі числення m.

У випадку, якщо аргумент х не є числом або рядком, або не може бути представленням цілого невід'ємного числа в системі числення з основою n, повернути логічну константу False.

В системах числення з основою більше десяти для позначення розрядів із значенням більше 9 використовувати літери латинського алфавіту у верхньому регістрі від A до Z. У вхідному x можуть використовуватися обидва регістри.

Вважати, що в одиничній системі числення число записується відповідною кількістю нулів.

Наприклад
Виклик функції: convert_n_to_m([123], 4, 3)
Повертає: False
Виклик функції: convert_n_to_m("0123", 5, 6)
Повертає: 102
Виклик функції: convert_n_to_m("123", 3, 5)
Повертає: False
Виклик функції: convert_n_to_m(123, 4, 1)
Повертає: 000000000000000000000000000
Виклик функції: convert_n_to_m(-123.0, 11, 16)
Повертає: False
Виклик функції: convert_n_to_m("A1Z", 36, 16)
Повертає: 32E7
'''

def convert_n_to_m(x, n, m):
	if n>=1 and n<=36 and m>=1 and m<=36:
		if type(x)== int:
			if x<0:
				return False
			x = str(x)
			if x == '0'*len(x):
				return '0'
		if type(x) == str:
			try:
				int(x) < 0
				if int(x)<0:
					return False
			except:
				pass


		if type(x) != int and type(x) != str:
			return False
		if m!= 1:
			try:
				int(x, n) % n 
			except:
				return False


		if n == m:
			return str(int(x))

		valall = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		valdict = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, 
		'6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 
		'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 
		'J':19, 'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 
		'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30, 
		'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
		valdictreverse = {0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 
		6:'6', 7:'7', 8:'8', 9:'9', 10:'A', 11:'B', 12:'C', 
		13:'D', 14:'E', 15:'F', 16:'G', 17:'H', 18:'I', 
		19:'J', 20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 
		25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 30:'U', 
		31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}

		if n != 10:
			#x = str(x)
			x = x.upper()
			kplus = len(x) - 1
			s = 0
			for i in range(kplus+1):
				xkp = valdict[x[kplus - i]]
				s = s + (n**i)* int(xkp)

			if m == 10:
				return s
		if m == 1:
			return "0"*int(s)
		if m > 1 and m <=36:
			xval = int(s)
			ostachi = []
			while xval > 0:
				ostacha = xval%m
				ostachi.append(valdictreverse[xval%m])
				xval = (xval//m)
			a = ''.join(str(e) for e in ostachi[::-1])
			return a
	else:
		return False

'''
print(convert_n_to_m(100, 2, 1))
print(convert_n_to_m('bnh34521', 11, 14))
print(convert_n_to_m('ZZZZ', 35, 13))
print(convert_n_to_m('-123.0', 5, 6))
#Повертає: 102

print(convert_n_to_m('0254', 8, 2))
#print(type(convert_n_to_m('0254', 8, 2)))
#10101100

print(convert_n_to_m([123], 4, 3))
#Повертає: False

print(convert_n_to_m("0123", 5, 6))
#Повертає: 102

print(convert_n_to_m("123", 3, 5))
#Повертає: False

print(convert_n_to_m(123, 4, 1))
#Повертає: 000000000000000000000000000

print(convert_n_to_m(-123.0, 11, 16))
#Повертає: False

print(convert_n_to_m("A1z", 36, 16))
#Повертає: 32E7

print()
print()


print(convert_n_to_m(True, 1, 2) == False)
print()

print(convert_n_to_m('', 12, 5)) #False is ok? 

print(convert_n_to_m(123123123123123123123, 10, 10)== '123123123123123123123') #true 

print(convert_n_to_m('123123123123123123123', 11, 16))
print(convert_n_to_m('123123123123123123123', 11, 16)== '2C09BC518E8048D23A')
print(convert_n_to_m(123123123123123123123, 11, 16))
print(convert_n_to_m(123123123123123123123, 11, 16)== '2C09BC518E8048D23A')

#print(convert_n_to_m(0, 10, 2)== '0') #string index out of range)
#print(convert_n_to_m(000, 10, 2)== '0') #string index out of range

#print(convert_n_to_m('000', 10, 2)== '0')
print()
print(convert_n_to_m('bnh34521', 31, 14)== '119337DC2BC')
print(convert_n_to_m('000ZZZZ', 36, 13)== '46A672')
print(convert_n_to_m('bnh34521', 11, 14)== False)

print(convert_n_to_m('qweasd', 33, 36)== 'HGPEYJ')
print(convert_n_to_m([123], 4, 3)== False)
print(convert_n_to_m("0123", 5, 6)== '102')
print(convert_n_to_m("123", 3, 5)== False)
print(convert_n_to_m(123, 4, 1)=='000000000000000000000000000', '000000000000000000000000000')
print(convert_n_to_m(-123.0, 11, 16)== False)
print(convert_n_to_m("A1Z", 36, 16)== '32E7')
'''
'''
#з прометеуса
print(1)
#Виклик:
print(convert_n_to_m([1], 2, 2))
#Відповідь:
print(False)

print(2)
#Виклик:
print(convert_n_to_m(True, 1, 2))
#Відповідь:
print(False)

print(3)
#Виклик:
print(convert_n_to_m({1: 0}, 2, 2))
#Відповідь:
print(False)

print(4)
#Виклик:
print(convert_n_to_m(-777, 10, 2))
#Відповідь:
print(False)

print(5)
#Виклик:
print(convert_n_to_m(123123123123123123123.0, 11, 16))
#Відповідь:
print(False)

print(6)
#Виклик:
print(convert_n_to_m(100, 2, 1))
#Відповідь:
print(0000)

print(7)
#Виклик#:
print(convert_n_to_m(0, 10, 2))
#Відповідь:
print(0)

print(8)
#Виклик:
print(convert_n_to_m(000, 10, 2))
#Відповідь:
print(0)

print(9)
#Виклик:
print(convert_n_to_m(777, 10, 2))
#Відповідь:
print(1100001001)

print(10)
#Виклик:
#print(convert_n_to_m(777L, 10, 2))
#Відповідь:
print(1100001001)

print(11)
#Виклик:
print(convert_n_to_m('000', 10, 2))
#Відповідь:
print(0)

print(12)
#Виклик:
print(convert_n_to_m('ZZZZ', 36, 13))
#Відповідь:
print('46A672')

print(13)
#Виклик:
print(convert_n_to_m('000ZZZZ', 36, 13))
#Відповідь:
print('46A672')

print(14)
#Виклик:
print(convert_n_to_m('ZZZZ', 35, 13))
#Відповідь:
print(False)

print(15)
#Виклик:
print(convert_n_to_m('qweasd', 33, 36))
#Відповідь:
print(HGPEYJ)

print(16)
#Виклик:
print(convert_n_to_m('123123123123123123123', 11, 16))
#Відповідь:
print('2C09BC518E8048D23A')

print(17)
#Виклик:
print(convert_n_to_m(123123123123123123123, 11, 16))
#Відповідь:
print('2C09BC518E8048D23A')

print(18)
#Виклик:
print(convert_n_to_m(123123123123123123123, 10, 10))
#Відповідь:
print(123123123123123123123)

print(19)
#Виклик:
print(convert_n_to_m('bnh34521', 31, 14))
#Відповідь:
print('119337DC2BC')

print(20)
#Виклик:
print(convert_n_to_m('bnh34521', 11, 14))
#Відповідь:
print(False)
'''
