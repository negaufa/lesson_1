proceed = float(input('Введите значение выручки:'))
cost = float(input('Введите значение издержек:'))
fin_result = round(proceed - cost, 2)
if fin_result > 0:
    print(
        f'Фирма работает с прибылью. Прибль составляет {fin_result} у.е. \nРентабельность выручки составляет {round(fin_result / proceed * 100, 2)} %')
elif fin_result < 0:
    print(f'Фирма работает в убыток. Убыток составляет {abs(fin_result)} у.е.\nНужно больше золота, милорд')
else:
    print('Фирма работает в ноль.')
worker = int(input('Введите количество сотрудников:'))
print(f'Прибль фирмы на одного сотрудника {round(proceed / worker, 2)} у.е.')
