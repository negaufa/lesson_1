a = int(input('Введите целое число А: '))
b = int(input('Введите целое число B: '))
c = input('Введите арифметическое действие, поддерживаются + - * / ')
if c == '+':
    print('Ваш результат ' + str(a + b))
elif c == '-':
    print('Ваш результат ' + str(a - b))
elif c == '*':
    print('Ваш результат ' + str(a * b))
elif c == '/':
    print('Ваш результат ' + str(a / b))
