def find_indexes(lst, min_val, max_val):
    indexes = []
    for i in range(len(lst)):
        if min_val <= lst[i] <= max_val:
            indexes.append(i)
    return indexes


# Пример использования
lst = [1, 5, 3, 8, 2, 7, 4, 6]
min_val = 3
max_val = 6
result = find_indexes(lst, min_val, max_val)
print(result)  # [2, 3, 6, 7]
