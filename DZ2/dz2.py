"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих
чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
*Пример:
4 4 -> 2 2
S P    X Y
5 6 -> 2 3
"""
from random import randint

s=int(input('Введите число s: '))
p=int(input('Введите число p: '))

for x in range(0,1000,1):
    for y in range (0,1000,1):
        if x+y==s and x*y==p:
            print(f'{x} {y}')













