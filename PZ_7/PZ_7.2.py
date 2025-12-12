#Дана строка, состоящая из русских слов, разделенных пробелами (одним или
#несколькими). Найти длину самого длинного слова
text = input("Введите строку: ")
words = text.split()
if not words: 
    print("Строка не содержит слов!")
else:
    max_length = max(len(word) for word in words)
    print(f"Длина самого длинного слова: {max_length}")