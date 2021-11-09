# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найти в массиве медиану.
from random import randint, choice
import statistics  # Взял не для основного решения задачи


def median(array, k):
    if len(array) == 1:
        return array[0]

    pivot = choice(array)

    left_el = [el for el in array if el < pivot]
    right_el = [el for el in array if el > pivot]
    pivots = [el for el in array if el == pivot]

    if k < len(left_el):
        return median(left_el, k)
    elif k < len(left_el) + len(pivots):
        return pivots[0]
    else:
        return median(right_el, k - len(left_el) - len(pivots))


M = 20  # Размер массива
random_array = [randint(0, 200) for _ in range(2 * M + 1)]
print(f'Медианой массива является:\n{median(random_array, len(random_array) / 2)}')
random_array.sort()
print(f'Массив после сортировки методом sort:\n{random_array}')
print(f'Медианой массива является:\n{random_array[len(random_array) // 2]}')

# Если не изобретать велосипед, то модуль статистики позволяет сильно сократить код
print(f'Медиана массива через модуль "statistics": {statistics.median(random_array)}')

