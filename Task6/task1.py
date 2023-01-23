

# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

# def twoDigit(arg):
#     if(arg < 99 and arg > 9):
#         return True
#     else: return False

twoDigit = lambda arg: True if arg < 99 and arg > 9 else False

a = list(input('Введите список чисел через пробел: ').split(' '))
a = list(map(int, a))
b = list(filter(twoDigit, a))
print(*b)
