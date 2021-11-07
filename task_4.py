# Определить, какое число в массиве встречается чаще всего.
import random

num_list = [random.randint(1, 5) for _ in range(10)]
digital_dict = dict.fromkeys(num_list, 0)          # словарь, ключами которого являются уникальные элементы списка

for num in num_list:
    digital_dict[num] += 1

max_num = 0
for key in digital_dict:
    if digital_dict[key] > max_num:
        max_key = key
        max_num = digital_dict[key]

print(f'В массиве \n{num_list} \nчаще всего встречается число: {max_key} ({max_num} раз)')
