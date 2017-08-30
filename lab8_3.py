'''
Розробити функцію bouquets(narcissus_price, tulip_price, rose_price, summ), 
яка приймає 4 аргументи -- додатні дійсні числа (ціни за один нарцис, тюльпан та троянду, і суму грошей у кишені головного героя), 
та повертає ціле число -- кількість варіантів букетів, які можна скласти з цих видів квітів, таких щоб вартість кожного букету 
не перевищувала summ.

Не забути, що букети з парною (загальною) кількістю квітів живим дівчатам не дарують. Тести із некоректними даними не проводяться.

Приклад послідовності дій для тестування:
print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(200,300,400,100000) # 3524556
'''

def bouquets(narcissus_price, tulip_price, rose_price, summ):
	nar = type(narcissus_price) == int or type(narcissus_price)== float and narcissus_price>0
	tul = type(tulip_price) == int or type(tulip_price)== float and tulip_price>0
	ros = type(rose_price) == int or type(rose_price)== float and rose_price>0
	summm = type(summ) == int or type(summ)== float and summ>0
	
	if nar and tul and ros and summm:
		narcissus_amount = int(summ/narcissus_price)
		tulip_amount = int(summ/tulip_price)
		rose_amount = int(summ/rose_price)
		sumoffbouquets = 0
		for i in range(0,narcissus_amount+1):
			nari = i
			for j in range(0, tulip_amount+1):
				tulj = j
				if (nari*narcissus_price+tulj*tulip_price)>summ:
					continue
				for k in range(0, rose_amount+1):
					rosk = k
					if (nari+tulj+rosk)%2 != 0 and (nari*narcissus_price+tulj*tulip_price+rosk*rose_price)<=summ:
						sumoffbouquets = sumoffbouquets + 1

		return sumoffbouquets

