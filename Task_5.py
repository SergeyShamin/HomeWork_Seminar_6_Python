'''Найти произведение пар чисел в списке. 
Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''

import random

list_numbers = [random.randint(1, 9) for i in range(10)]
middle = int(len(list_numbers) / 2 + len(list_numbers) % 2)
pairs = list(map(lambda i: (list_numbers[i], list_numbers[len(list_numbers) - i - 1]), range(middle)))
result = [t[0] * t[1] for t in pairs]
print(list_numbers)
print(result)