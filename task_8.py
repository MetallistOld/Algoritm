# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в ее последнюю ячейку.
# В конце следует вывести полученную матрицу.

matrix = []

for n in range(4):
    matrix.append([])
    line_sum = 0
    for i in range(4):
        num = int(input(f'Введите значение {n + 1} строки и {i +1} столбца: '))
        matrix[n].append(num)
        line_sum += num
    matrix[n].append(line_sum)

for line in matrix:
    for num in line:
        print(f'\t{num:>5}', end='')
    print()
