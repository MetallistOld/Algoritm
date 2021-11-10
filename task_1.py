# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный
# массив, заданный случайными числами на промежутке [-100; 100). Выведите на
# экран исходный и отсортированный массивы. Сортировка должна быть реализована в
# виде функции. По возможности доработайте алгоритм (сделайте его умнее).

from random import randint
from timeit import timeit

MAX_SIZE = 100
NUMBER_EXECUTIONS = 1000


def bubble_sort(array):
    for i in range(len(array) - 1, 0, -1):
        flag = True
        for n in range(i):
            if array[n] < array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]
                flag = False
        if flag:
            break  # Выходим из цикла, если замен больше не происходит, тем самым оптимизируем алгоритм сортировки
    return array


def bubble_sort_no_smart(array):  # Не оптимизированный вариант сортировки
    for i in range(len(array) - 1, 0, -1):
        for n in range(i):
            if array[n] < array[n + 1]:
                array[n], array[n + 1] = array[n + 1], array[n]

    return array


numbers = [randint(-100, 100) for _ in range(MAX_SIZE)]

print(f'Исходный массив:\n{numbers}')

print(f'Отсортированный массив:\n{bubble_sort(numbers)}')

time1 = timeit(f'bubble_sort({numbers})',
               setup='from __main__ import bubble_sort',
               number=NUMBER_EXECUTIONS)
time2 = timeit(f'bubble_sort_no_smart({numbers})',
               setup='from __main__ import bubble_sort_no_smart',
               number=NUMBER_EXECUTIONS)

print(f'Производительность умной сортировки: {time1}')
print(f'Производительность сортировки: {time2}')
