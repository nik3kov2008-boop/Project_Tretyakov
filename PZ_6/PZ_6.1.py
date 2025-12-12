#Дан список размера N и целые числа K и L (1 < K ≤ L ≤ N). Найти среднее
#арифметическое всех элементов списка, кроме элементов с номерами от K до L
#включительно.
N = int(input("Введите N: "))
spisok = []

for i in range(N):
    num = int(input(f"Элемент {i+1}: "))
    spisok.append(num)
    
K = int(input(f"Введите K (1 < K ≤ {N}): "))
L = int(input(f"Введите L ({K} ≤ L ≤ {N}): "))

if not (1 < K <= L <= N):
    print("Ошибка в значениях K и L")
else:
    total = 0
    count = 0
    for i in range(N):
        if i < K-1 or i > L-1:  
            total += spisok[i]
            count += 1
    sredn1 = total / count
    print(f"Среднее арифметическое: {sredn1}")