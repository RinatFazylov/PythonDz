"""
Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена
прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
"""
a1 = int(input('Введите число a1: '))
d = int(input('Введите число d: '))
n = int(input('Введите число n: '))
my_list=[]
for i in range(n):
    my_list.append(a1 + i * d)
print(my_list)