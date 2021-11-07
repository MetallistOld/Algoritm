# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке
# и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
    try:
        num1, operation, num2 = [
            i for i in
            input(
                'Введите математическое выражение (число операнд число) или в качестве операнда введите 0 для выхода: '
            ).split()
        ]
    except ValueError:
        print('Неправильный ввод.')
        continue
    num1 = int(num1)
    num2 = int(num2)

    if operation == '0':
        print('До свидания')
        break
    elif operation == '+':
        print(f'{num1} {operation} {num2} = {num1 + num2}')
    elif operation == '-':
        print(f'{num1} {operation} {num2} = {num1 - num2}')
    elif operation == '*':
        print(f'{num1} {operation} {num2} = {num1 * num2}')
    elif operation == '/':
        try:
            print(f'{num1} {operation} {num2} = {num1 / num2}')
        except ZeroDivisionError:
            print('Ошибка. На ноль делить нельзя')
