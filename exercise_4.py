a = int(input('Введите целое положительное число: '))
max = 0
min = 0
sum = 0
while a > 0:
    min = a % 10
    sum = sum + min
    if min > max:
        max = min
    a = a // 10
print(f'Самая большая цифра в числе: {max}')
print(f'Сумма цифр в числе: {sum}')
