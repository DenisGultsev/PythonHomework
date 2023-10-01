def solve_petya_and_katya():  
    S = int(input("Введите сумму чисел: "))  
    P = int(input("Введите произведение чисел: "))  
  
    for x in range(1, 1001):  
        y = S - x  
        if x * y == P:  
            return x, y  
  
x, y = solve_petya_and_katya()  
print(f"Задуманные числа: {x} и {y}")