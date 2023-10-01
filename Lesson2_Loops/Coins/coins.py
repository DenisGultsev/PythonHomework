def flip_coins(coins):
    heads = 0
    tails = 0
    for coin in coins:
        if coin == 0:
            tails += 1
        else:
            heads += 1
    return min(heads, tails)

n = int(input("Введите количество монеток: "))
coins = []
for i in range(n):
    coin = int(input(f"Введите значение монетки {i+1} (0 - герб, 1 - решка): "))
    coins.append(coin)

min_flips = flip_coins(coins)
print(f"Минимальное количество монеток, которые нужно перевернуть: {min_flips}")