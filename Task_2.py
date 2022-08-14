#Найти сумму чисел списка стоящих на нечетной позиции
import random 

list_numbers = [random.randint(1, 9) for value in range(0, 10)]

print(list_numbers)
print(sum([c for i, c in enumerate(list_numbers) if i % 2 != 0]))