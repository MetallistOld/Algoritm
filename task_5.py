# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random

num_list = [random.randint(-15, 15) for _ in range(15)]
min_idx = 0
for i, item in enumerate(num_list):
    if num_list[min_idx] < item < 0:
        min_idx = i

if num_list[min_idx] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве: \n{num_list} \nмаксимальный отрицательный элемент = {num_list[min_idx]} \nего индекс = {min_idx}')
