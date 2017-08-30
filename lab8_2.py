'''
Розробити функцію find_fraction(summ), 
яка приймає 1 аргумент -- невід'ємне ціле число summ, 
та повертає тьюпл, що містить 2 цілих числа -- чисельник та знаменник найбільшого правильного нескорочуваного дробу, для якого сума чисельника та знаменника дорівнює summ. Повернути False, якщо утворити такий дріб неможливо.

Тести із некоректними даними не проводяться.

Приклад послідовності дій для тестування:
print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)
'''

def find_fraction(summ):
    if type(summ) == int and summ > 0:
        ser1 = int(summ / 2)

        def nsd(a, b):
            while a * b != 0:
                if a >= b:
                    a = a % b
                else:
                    b = b % a
            return a + b

        for i in range(0, ser1):
            ser1 = int(summ / 2) - i
            ser2 = summ - ser1
            ncdd = nsd(ser1, ser2)
            if ser1 != ser2 and ncdd == 1:
                return (ser1, ser2)

    return False
