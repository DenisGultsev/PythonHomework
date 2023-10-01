# Ввод значений с клавиатуры
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов: "))

# Создание и заполнение массива
progression = []
for i in range(n):
    element = a1 + (i * d)
    progression.append(element)

# Вывод массива
print("Массив арифметической прогрессии:")
for element in progression:
    print(element)
