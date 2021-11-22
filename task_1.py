# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках
# первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
#
import random
import sys


# '64bit', 'Windows10
# Python 3.9.5

# Lesson 03_5 Найти максимальный элемент среди минимальных элементов столбцов матрицы.

matrix = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)]

for i, line in enumerate(matrix):

    if i == 0:
        min_line = line.copy()
        for item in line:
            print(f'{item:>5}', end='')
        print()
        continue

    for idx, item in enumerate(line):
        if item < min_line[idx]:
            min_line[idx] = item
        print(f'{item:>5}', end='')
    print()

print('-' * len(min_line) * 5)

max_min = min_line[0]
for item in min_line:
    print(f'{item:>5}', end='')
    if item > max_min:
        max_min = item

print()
print(f'Максимальный элемент среди минимальных элементов столбцов матрицы = {max_min}')
sum_size = 0
sum_size += sys.getsizeof(matrix)
sum_size += sys.getsizeof(max_min)
sum_size += sys.getsizeof(i)
sum_size += sys.getsizeof(min_line)
sum_size += sys.getsizeof(item)

print('Переменные занимают', sum_size)
