# 1) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# Number = int(input('введите ваше число : '))
# pr = 1

# for i in range(1, Number + 1):
#    if(i <= Number):
#       pr *= i
#       print(pr) 
      
# 2) Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Пример:

# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5
      
# Number = int(input('введите ваше число : '))

# for i in range(1, Number):
#     if(Number % i == 0 and i != 1):
#         print(f'наименьший натуральный делитель  = {i}')
#         break

# 3) Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.

# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]

# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

# 4)Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.
# summ = 0
# Number = int(input('введите ваше число : '))
# for i in range(0, Number + 1, 2):
#     if(i!= 0):
#      summ += i
# print(f'Сумма всех четных элементов от 1 до числа {Number} = {summ}')   