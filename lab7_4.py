'''
Розробити функцію create_calendar_page(month,year), 
яка приймає 2 аргументи -- цілі числа -- місяць (нумерація починається з 1) і рік, 
та повертає оператором return 1 рядок, який містить сторінку календаря на цей місяць.

Якщо місяць та рік не задані, використати сьогоднішні значення.

Це значення є одним рядком із переносами рядка \n, пробіли після числа 28 відсутні. 
Зайві пробіли в кінці під-рядків або всього рядка, як і зайві порожні рядки недопустимі.
Тести із некорестними даними не проводяться.

Приклад викликів для тестування функції:
print create_calendar_page(1)
print create_calendar_page()
print create_calendar_page(3)
print create_calendar_page(04, 1992)
'''

import datetime

month = datetime.datetime.today().month
year = datetime.datetime.today().year

def create_calendar_page(month=month,year=year):
	if type(month) != int or type(year) != int:
		return None
	#month and year are int
	#how many days
	if month in (4,6,9,11):
		daysinmonth = 30
	elif month in (1,3,5,7,8,10,12):
		daysinmonth = 31
	elif month == 2:
		if year%4 == 0:
			daysinmonth = 29
		else: daysinmonth = 28
	print(daysinmonth)

	#from what day of week month was started
	dt = datetime.datetime(year, month, 1)
	day = dt.weekday()
	print(day)

	monthcalendar = ' '*day*3 
	days = daysinmonth

	dayincalendar = 1
	for i in range(1,days+1):
		if i < 10:
			monthcalendar = monthcalendar+"0"

		monthcalendar = monthcalendar+str(dayincalendar)
		
		if i != 7-day and i!= 14-day and i!= 21-day and i != 28-day and i != 35 - day and i != days:
			monthcalendar = monthcalendar + " "
		
		

		if i == 7-day or i == 14-day or i == 21-day or i == 28-day or i == 35 - day:
			monthcalendar = monthcalendar + "\n"

		dayincalendar = dayincalendar + 1

	header = "-"*20+"\n" +"MO TU WE TH FR SA SU\n"+"-"*20+"\n"
	calendar = header + monthcalendar
	return calendar
