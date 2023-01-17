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



# with open('rle_pack.txt', 'r') as entered:
#     stroka = entered.read() # читаем фаил
# print(stroka)

# def rle_package(arg): #Запаковка 
#     newStroka1 = ''
#     i = 0
#     while(i < len(arg)):
#         count = 1 # Подсчитываем кол-во одинаковых элементов
#         while(i + 1 < len(arg) and arg[i] == arg[i+1]): #Выполняется пока арг + 1 меньше длины арг
#             count = count + 1
#             i = i + 1
#         newStroka1 += str(count) + arg[i] # записываем кол-во повторений и значение индекса
#         i = i + 1
#     return newStroka1
# newStroka1 = rle_package(stroka)

# with open('rle_pack.txt','a') as entered:
#     entered.write(f'\nPackage text : {newStroka1}')



# with open('rle_unpack.txt', 'r') as enter: 
#     rle_pack = enter.read() # читаем фаил
#     print(rle_pack)

# def rle_unpackage(arg):# распаковка
#     if len(arg) < 1:
#         return ''
#     newStroka2 = ''
#     repeat = ''
#     for elem in arg:
#         if elem.isdigit():
#                 repeat += elem
#         else:
#             for i in range(int(repeat)):
#                 newStroka2 += elem # Записываем i repeat раз
#             else:
#                  repeat = ''
#     return newStroka2
# newStroka2 = rle_unpackage(rle_pack)

# with open('rle_unpack.txt','a') as entered: # Распаковываем. записываем в тот же фаил
#     entered.write(f'\nunpackage text : {newStroka2}')








# 2) Создайте программу для игры в ""Крестики-нолики"" человек vs человек.
# 1 | 2 | X
# 4 | X | O
# X | 8 | O

# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

# board = list(range(1,10))

# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)

# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")

# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "выиграл!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)

# input("Нажмите Enter для выхода!")