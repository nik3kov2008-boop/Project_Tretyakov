# Даны два числа. Ввести большее из них
try:
    a, b = int(input(" Введите первое число: ")), int(input(" Введите второе число: "))
    if a > b:
      print(a)
    elif a < b:
      print(b)
    else:
      print("Числа равны")
except ValueError:
    print("Неправильно ввели")
    
    
