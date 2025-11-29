#Дано число A (>1). Вывести наибольшее из целых чисел K, для которых сумма 1 +
#1/2 + ... + 1/K будет меньше A, и саму эту сумму
try:
    a = float(input("Введите число a: "))
    k = 1
    tot = 0
    while True:
       if tot + 1/k >= a: 
        break
       tot += 1/k
       k += 1

    print(f"Наибольшее K: {k-1}")
    print(f"Сумма: {tot}")
except ValueError:
    print("Что-то не так попробуй еще раз")
