# 4.Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

num = int(input('Введите количество элементов: '))
idx = 0
range_number = 1
sum = 0
while idx < num:
    sum += range_number
    range_number /= -2
    idx += 1
print(f'Сумма {num} элементов = {sum}')
