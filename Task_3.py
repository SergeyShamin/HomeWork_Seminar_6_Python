#Найти расстояние между двумя точками пространства(числа вводятся через пробел)

import math

x1, y1, x2, y2 = [float(i) for i in input('Введите числа: ').split()]
print(math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)))