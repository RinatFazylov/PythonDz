"""
Найдите сумму цифр трехзначного числа.
Пример:
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)
"""
number = int(input('Введите 3х значное число: '))
if number>1000 or number<100:
    print("Неверное число")
else:
    sum =number/100
    sum=sum+((number%100)%10)
    sum=sum+((number%100)/10)
    print (int(sum))




