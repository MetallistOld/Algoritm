# Написать два алгоритма нахождения i-го по счёту простого числа. Первый - использовать алгоритм решето Эратосфена.
# Второй - без использования "решета". Проанализировать скорость и сложность алгоритмов.
import cProfile


# n = int(input('Какое по счету простое число вы хотите найти: '))
# lst = [i for i in range(n * n)]


# Вариант 1. Решето Эратосфена.

def sieve(num_list, idx):
    num_list[1] = 0
    i = 2
    s_num_list = []
    while len(s_num_list) < idx:
        if num_list[i] != 0:
            s_num_list.append(num_list[i])
            j = i * 2
            while j < len(num_list):
                num_list[j] = 0
                j += i
        i += 1
    return s_num_list[-1]

# y = 10
# x = [i for i in range(y * y)]
# cProfile.run('sieve(x, y)')
# 191 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 task_2.py:13(sieve)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 177    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вариант 2. Перебор.

def simple_num(num_list, idx):
    num_list[1] = 0
    s_nums = []
    for i in range(2, len(num_list)):
        for num in s_nums:
            if num_list[i] % num == 0:
                break
        else:
            s_nums.append(num_list[i])
        if len(s_nums) == idx:
            return s_nums[-1]


# y = 10
# x = [i for i in range(y * y)]
# cProfile.run('simple_num(x, y)')
# 43 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 task_2.py:52(simple_num)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 29    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def sieve2(num_list, idx):
    num_list[1] = 0
    i = 2
    s_num_list = []
    length = 0
    length_num_list = len(num_list)
    while length < idx:
        if num_list[i] != 0:
            s_num_list.append(num_list[i])
            length += 1
            j = i * 2
            while j < length_num_list:
                num_list[j] = 0
                j += i
        i += 1
    return s_num_list[-1]


# y = 10
# x = [i for i in range(y * y)]
# cProfile.run('sieve2(x, y)')
# 15 function calls in 0.000 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 task_2.py:99(sieve2)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
# 10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

