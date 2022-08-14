'''Сформировать список из  N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.'''

list_numbers = [(3**value)*((-1)**value) for value in range(0, 10)]
print(list_numbers)
