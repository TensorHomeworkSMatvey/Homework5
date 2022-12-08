def summing(*numbers):
    try: return "Сумма чисел равна: " + str(sum(numbers))
    except: return "Введите числа через запятую"

print(summing(1, 2, 3, 4, 5))