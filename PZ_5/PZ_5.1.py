#Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
#Использовать локальные переменные.
def sum_of_series(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
result = sum_of_series(60)
print(f"Сумма чисел от 1 до 60: {result}")