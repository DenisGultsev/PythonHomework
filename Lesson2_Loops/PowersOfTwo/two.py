def print_powers_of_two():  
    N = int(input("Введите число N: "))  
    power = 0  
    while 2 ** power <= N:  
        print(2 ** power)  
        power += 1  
  
print_powers_of_two()