'''
Розробити функцію find_most_frequent(text), 
яка приймає 1 аргумент -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
та повертає список слів (у нижньому регістрі), які зустрічаються в тексті найчастіше.

Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Якщо слів, які зустрічаються найчастіше, декілька -- вивести їх в алфавітному порядку.

Наприклад
Виклик функції: find_most_frequent('Hello,Hello, my dear!')
Повертає: ['hello']
Виклик функції: find_most_frequent('to understand recursion you need first to understand recursion...')
Повертає: ['recursion', 'to', 'understand']
Виклик функції: find_most_frequent('Mom! Mom! Are you sleeping?!!!')
Повертає: ['mom']
'''

def find_most_frequent(text):
	text = text.lower()
	textlist = []
	maxwordslist = [] 
	for i in text:
		if i in ",.:;!?-" :
			text = text.replace(i, " ")

	textlist = text.split(" ")
	textlist = [i for i in textlist if i != ""]
	textlist.sort()
	numb = []

	for item in textlist:
		numb.append(textlist.count(item))

	for item in textlist:
		if textlist.count(item) >= max(numb) and item not in maxwordslist:
			maxwordslist.append(item)

	return maxwordslist
