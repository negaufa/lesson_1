second_count = int(input('Введите время в секундах: '))
hour = second_count // 3600
minute = (second_count - hour * 3600) // 60
second = (second_count - (hour * 3600 + minute * 60))
print(f'{hour:02}:{minute:02}:{second:02}')
