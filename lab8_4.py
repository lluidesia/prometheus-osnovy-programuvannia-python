'''
Розробити функцію make_sudoku(size), 
яка приймає 1 аргумент -- додатнє ціле число (1 <= size <= 42), 
та повертає список списків -- квадратну матрицю, що представляє судоку розмірності size.

Судоку розмірності X являє собою квадратну матрицю розмірністю X**2 на X**2, розбиту на X**2 квадратів розмірністю X на X, 
заповнену цілими числами таким чином, щоб кожна вертикаль, кожна горизонталь та кожний квадрат містили всі числа від 1 до X**2 
включно без повторів.

-- квадрат 9х9 (3**2 = 9), який складається з 9 квадратів 3х3. В кожній вертикалі розміщені різні числа від 1 до 9. Те саме стосується кожної горизонталі та кожного внутрішнього квадрату.

Дане завдання не має єдиного вірного розв'язку -- ваша функція повинна повертати результат, який задовольняє умові, за відведений час.

Тести із некоректними даними не проводяться

Приклад вхідних і вихідних даних:
print make_sudoku(1) # [[1]]
print make_sudoku(2) # [[1,2,3,4],[3,4,1,2],[2,1,4,3],[4,3,2,1]]
print make_sudoku(3) # [[3,5,8,1,2,7,6,4,9],[6,7,4,5,8,9,3,2,1],[2,1,9,3,4,6,5,7,8],[9,8,6,7,1,4,2,5,3],[4,3,1,2,6,5,8,9,7],[7,2,5,9,3,8,1,6,4],[1,6,3,4,7,2,9,8,5],[8,9,7,6,5,1,4,3,2],[5,4,2,8,9,3,7,1,6]]
(0.5/2.5 бали)
'''

from random import shuffle, choice
def make_sudoku(size):
	if type(size) == int and size>=1 and size<=42:
		s = size**2
		rang = list(range(1, s+1))

		summ = 0
		for i in rang:
			summ = summ + i

		e = list(range(1, s+1))
		shuffle(e)

		res = list(range(s))
		res[0] = e

		for i in range(1,s):
			res[i] = []
			ee = res[i-1]

			for j in range(0,s):
				a = (ee[j]+1)
				if a == s+1:
					a=1
				res[i].append(a)

		
		return res
