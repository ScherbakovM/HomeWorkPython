# 1) Создайте программу для игры с конфетами человек против бота.
# Условие задачи: На столе лежит 120 конфета. Играют два игрока делая ход друг после друга.
# Первый ход делает человек. За один ход можно забрать не более чем 28 конфет.
# Победитель - тот, кто оставил на столе 0 конфет.

# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф

# a) Добавьте игру против бота

# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)


import math
import random

# Game Sweets
# sweets = int(120)  # Кол-во конфет
# maxStep = 28 # Ограничение по максимальному шагу
# description = ('\nНа столе лежит 120 конфет. Сначала ходит пользователь, потом бот. За один ход можно забрать не более чем 28 конфет.'
# '\nПобедитель - тот, кто оставит на столе 0 конфет.\n') # Описание игры

# print(description)
# def logicsSweets(sweets): 
#     if(sweets > 28):
#         userStep = int(input('Введите кол-во конфет которое вы хотите взять: ')) # Игрок вводит своё кол-во конфет
#         if(userStep > maxStep or userStep < 0): exit(' Error404! Нельзя брать больше 28 конфет!')  # Проверка шага !> 28  
#         print('шаг пользователя: ', userStep)
#         sweets = sweets - userStep
#         print('Конфет осталось:', sweets)
#         if(sweets <= 0):
#             print('Победил:', 'Пользователь')
#         if(sweets > 0):
#             if(sweets < 28): # Проверка шага. Если перед шагом бота остаток меньше 28, он заберёт всё
#                 botStep = int(sweets)
#                 print('шаг бота: ', botStep)
#                 sweets = sweets - botStep
#                 print('Конфет осталось:', sweets)
#                 if(sweets <= 0):exit('Победил бот')
#             else:
#                 botStep = int(random.randint(0, 28))
#                 print('шаг бота: ', botStep)
#                 sweets = sweets - botStep
#                 print('Конфет осталось:', sweets)
#                 if(sweets <= 0):exit('Победил бот')
#     if(sweets <= 28):
#         userStep = int(input('Введите кол-во конфет которое вы хотите взять: ')) # Игрок вводит своё кол-во конфет
#         if(userStep > sweets): exit(F' Error404! Нельзя брать больше {sweets} конфет!')  # Проверка шага не больше остатка.
#         print('шаг пользователя: ', userStep)
#         sweets = sweets - userStep
#         print('Конфет осталось:', sweets)
#         if(sweets <=0):exit('Победил пользователь')
#         botStep = int(sweets) # Ограничение бота по шагу возьмёт всё если меньше 28
#         print('шаг бота: ', botStep)
#         sweets = sweets - botStep
#         print('Конфет осталось:', sweets)
#         if(sweets <=0):exit('Победил бот')   
#     logicsSweets(sweets)
#     return sweets

# logicsSweets(sweets)





# 3) Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"

# Вывод: stroka = "aaabbbbccbbb"

with open('rle_pack.txt', 'r') as entered:
    stroka = entered.read() # читаем фаил
print(stroka)

def rle_package(arg):
    newStroka = ''
    i = 0
    while(i < len(arg)):
        count = 1 # Подсчитываем кол-во одинаковых элементов
        while(i + 1 < len(arg) and arg[i] == arg[i+1]): #Выполняется пока арг + 1 меньше длины арг
            count = count + 1
            i = i + 1
        newStroka += str(count) + arg[i] # записываем кол-во повторений и значение индекса
        i = i + 1
    return newStroka
newStroka = rle_package(stroka)

with open('rle_pack.txt','a') as entered:
    entered.write(newStroka)