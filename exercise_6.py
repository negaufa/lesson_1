intermediate_result = float(input('Введите начальное количество километров: '))
desired_result = float(input('Введите нужное количество километров: '))
day = 1
while intermediate_result < desired_result:
    intermediate_result = round(intermediate_result + intermediate_result / 100 * 10, 2)
    day += 1
print(f'На {day} день спортсмен достиг результата - не менее {desired_result} км.')
