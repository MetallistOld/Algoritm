# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.
from collections import Counter
import heapq


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def walk(self, code_dict, path):
        self.left.walk(code_dict, path + "0")
        self.right.walk(code_dict, path + "1")


class Leaf:
    def __init__(self, value):
        self.value = value

    def walk(self, code_dict, path):
        code_dict[self.value] = path
        return path


def huffman(s):
    lst = []

    for i, item in Counter(s).items():
        lst.append((item, len(lst), Leaf(i)))

    iteration = len(lst)
    heapq.heapify(lst)
    while len(lst) > 1:
        first = heapq.heappop(lst)
        second = heapq.heappop(lst)
        heapq.heappush(lst, (first[0] + second[0], iteration, MyNode(first[2], second[2])))
        iteration += 1

    code_dict = {}
    if lst:
        lst[0][2].walk(code_dict, "")
    return code_dict


input_string = input('Введите строку: ')
print(f'Строка: \n{input_string}')
counter_char = Counter(input_string)
print(f'Символы в строке и их количество: {counter_char}')
code_string = huffman(counter_char)
# print(code_string)
for key, value in code_string.items():
    print(f'Код для символа {key}: {value}')
