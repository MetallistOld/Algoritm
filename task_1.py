# Проанализировать скорость и сложность одного - трёх любых алгоритмов,
# разработанных в рамках домашнего задания первых трех уроков.
#
# Задание 5 урок 3
# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
from timeit import timeit
import random
import cProfile


def my_func(num_list):
    min_el = float('-inf')
    for i, item in enumerate(num_list):
        if min_el < item < 0:
            min_el = item
            min_idx = i


random.seed(42)
num_list = [random.randint(-100, 0) for _ in range(100000)]
time1 = timeit(f'my_func({num_list})', setup='from __main__ import my_func', number=1000)
print(time1)
# 8.6344859

def func_2(num_list):
    new_list = [i for i in num_list if i < 0]
    maximum = max(new_list)
    idx = new_list.index(maximum)


num_list = [random.randint(-100, 0) for _ in range(100000)]
time2 = timeit(f'my_func({num_list})', setup='from __main__ import my_func', number=1000)
print(time2)
# 7.963149499999998

cProfile.run('my_func(num_list)')
# 4 function calls in 0.005 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.005    0.005 <string>:1(<module>)
# 1    0.005    0.005    0.005    0.005 task_1.py:12(my_func)
# 1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('func_2(num_list)')
# 7 function calls in 0.007 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.007    0.007 <string>:1(<module>)
# 1    0.000    0.000    0.006    0.006 task_1.py:26(func_2)
# 1    0.005    0.005    0.005    0.005 task_1.py:27(<listcomp>)
# 1    0.000    0.000    0.007    0.007 {built-in method builtins.exec}
# 1    0.001    0.001    0.001    0.001 {built-in method builtins.max}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}