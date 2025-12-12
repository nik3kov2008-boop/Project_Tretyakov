#Дано множество A из N точек (точки заданы своими координатами х, у). Среди всех
#точек этого множества, лежащих во второй четверти, найти точку, наиболее
#удаленную от начала координат. Если таких точек нет, то вывести точку с нулевыми
#координатами.
n = int(input("Сколько точек? "))
x_list = []
y_list = []

for i in range(n):
    print(f"Точка {i+1}:")
    x = float(input("  x = "))
    y = float(input("  y = "))
    x_list.append(x)
    y_list.append(y)

max_distance = 0
found = False
result_x = 0
result_y = 0

for i in range(n):
    x = x_list[i]
    y = y_list[i]
    
    if x < 0 and y > 0:
        distance = (x**2 + y**2) ** 0.5
        
        if not found or distance > max_distance:
            max_distance = distance
            result_x = x
            result_y = y
            found = True  
print(f"Координаты: ({result_x}, {result_y})")
print(f"Расстояние от центра: {max_distance}")