#Описать функцию Mean(X, Y, AMean, GMean), вычисляющую среднее
#арифметическое AMean = (X+Y)/2 и среднее геометрическое GMean = y/X Y двух
#положительных чисел X и Y (X и Y — входные, AMean и GMean — выходные
#параметры вещественного типа). С помощью этой функции найти среднее
#арифметическое и среднее геометрическое для пар (A, B), (A, C), (A, D), если даны
#A, B, C, D.
def Mean(x, y):
    am = (x + y) / 2
    gm = (x * y) ** 0.5
    return am, gm

try:
    a = int(input("A: "))
    b = int(input("B: "))
    c = int(input("C: "))
    d = int(input("D: "))
    am1, gm1 = Mean(a, b)
    am2, gm2 = Mean(a, c)
    am3, gm3 = Mean(a, d)

    print(f"(A,B): ср.арифм. = {am1}, ср.геом. = {gm1}")
    print(f"(A,C): ср.арифм. = {am2}, ср.геом. = {gm2}")
    print(f"(A,D): ср.арифм. = {am3}, ср.геом. = {gm3}")
except ValueError:
    print('Неправильно ввели')