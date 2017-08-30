'''
Розробити функцію counter(a, b), 
яка приймає 2 аргументи -- цілі невід'ємні числа a та b, 
та повертає число -- кількість різних цифр числа b, які містяться у числі а.

Наприклад
Виклик функції: counter(12345, 567)
Повертає: 1
Виклик функції: counter(1233211, 12128)
Повертає: 2
Виклик функції: counter(123, 45)
Повертає: 0
'''

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
