#Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения ...Полученное число является приближенным
#значением функции arctg в точке X.
try:
    x = float(input("Введите число x: "))
    n = int(input("Введите число n: "))
    min = 1
    i = 1
    tot1 = 0
    while i <= n:  
        nnn = 2 * i - 1
        tot = min * (x ** nnn) / nnn
        tot1 += tot
        min *= -1
        i += 1
    print(tot1)
except ValueError:
    print("Что-то не так попробуй еще раз")
    
