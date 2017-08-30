'''
Розробити класс SuperStr, який наслідує функціональність стандартного типу str і містить 2 нових методи:

метод is_repeatance(s), який приймає 1 аргумент s та повертає True або False в залежності від того, 
чи може бути поточний рядок бути отриманий цілою кількістю повторів рядка s. Повернути False, якщо s не є рядком. 
Вважати, що порожній рядок не містить повторів.
метод is_palindrom(), який повертає True або False в залежності від того, чи є рядок паліндромом. 
Регістрами символів нехтувати. Порожній рядок вважати паліндромом.
Приклад послідовності дій для тестування класу:
s = SuperStr('123123123123')
print s.is_repeatance('123') # True
print s.is_repeatance('123123') # True
print s.is_repeatance('123123123123') # True
print s.is_repeatance('12312') # False
print s.is_repeatance(123) # False
print s.is_palindrom() # False
print s # 123123123123 (рядок)
print int(s) # 123123123123 (ціле число)
print s + 'qwe' # 123123123123qwe
p = SuperStr('123_321')
print p.is_palindrom() # True
'''

class SuperStr(str):

	def __init__(self, st):
		self.st = st

	def is_repeatance(self, s):
		is_per = False
		if type(s) == str and s != '' and self.st != '':
			stt = self.st
			n = int(len(stt)/len(s))
			if stt == s * n:
				is_per = True
		
		return is_per

	def is_palindrom(self):
		text = self.st.lower()
		text=text.replace(" ", "")

		text_reverse=text[::-1]

		n=len(text)
		is_pal = True

		for i in range(n):
			if text[i] != text_reverse[i]:
				is_pal =False

		return is_pal
