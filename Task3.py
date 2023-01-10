import random
import math

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# elem = int(input('Введите кол-во элементов списка : '))
# randomNum = list(range(10)) # Создаём список от 0 до 10
# random.shuffle(randomNum) # Перемешиваем числа в списке.
# userList = (randomNum[0:elem]) # заполняем новый список от 0-ой до позиции которую вводит юзер.
# print('ваш список из', elem, 'элементов:', userList)

# def SumElemList(arg):
#         print('нечётные( по позиции ) элементы списка: ')
#         sum = 0
#         for index in range(len(arg)):
#                 if(index % 2 != 0):
#                         print(arg[index], end = ' ')
#                         sum += arg[index]
#         print()                
#         print('сумма нечётных элементов списка = ',sum)

# SumElemList(userList)

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# elem = int(input('Введите кол-во элементов списка : '))
# randomNum = list(range(10)) # Создаём список от 0 до 10
# random.shuffle(randomNum) # Перемешиваем числа в списке.
# userList = (randomNum[0:elem]) # заполняем новый список от 0-ой до позиции которую вводит юзер.
# print('ваш список из', elem, 'элементов:', userList)
# newList = []

# def prodNumbers(arg):
        
#         for i in range(len(arg)):
        
#                 halfList = int(len(arg) / 2)
#                 halfList = math.ceil(halfList)

#                 if(i > halfList):
#                         break

#                 if(i == 0):

#                         newList.append(arg[i] * arg[i-1])
                
#                 else:
#                         newList.append(arg[i] * arg[-i-1])
        
#         return newList

# prodNumbers(userList)
# print(newList)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# elem = int(input('Введите кол-во элементов списка : '))
# floatList = []

# for i in range(0, elem, + 1):
#         num = float((input(f'введите вещественное число {i+1}: ')))
#         floatNum = round(num - int(num),3)
#         floatList.append(floatNum)

# maxNumber = floatList[0]
# minNumber = floatList[0]

# for i in floatList:
#         if(maxNumber < i):
#                         maxNumber = i
                        
#         if(i < minNumber):
#                         minNumber = i
# print('максимальная дробная часть', maxNumber)                       
# print('минимальная  дробная часть', minNumber)                       
# print(f'разница между максимальной и минимальной дробной часть = {maxNumber - minNumber}')


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Введите число в десятичной системе которое вы хотите преобразовать в двоичную: '))
print(f'Вы ввели число : {number}')

def binarySys(number):
        remainder = '' 
        if(number > 0): 
                remainder = number % 2             
                binarySys(int(number / 2))
        print(remainder, end = '')
binarySys(number)


#   # Остаток
#                 res =  res +  remainder 
#                 number = (math.floor(number / 2)) # неполное частное 