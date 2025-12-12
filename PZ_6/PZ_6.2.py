#Даны списки A и B одинакового размера N. Поменять местами их содержимое и
#вывести вначале элементы преобразованного списка A, а затем — элементы
#преобразованного списка B.
N = int(input("Введите N: "))

A = []
for i in range(N):
    num = int(input(f"Элемент списка А {i+1}: "))
    A.append(num)
    
B = []
for i in range(N):
    num = int(input(f"Элемент списка B {i+1}: "))
    B.append(num)    
    
for i in range(N):
    A[i], B[i] = B[i], A[i]
print(f"Элементы списка А: {A}")    
print(f"Элементы списка B: {B}") 