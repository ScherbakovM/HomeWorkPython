from views import *
import json

# Функция выбора кто использует программу. 

def InitialChoice():
    user = warningChoice
    print(f'\n{startMessage}\n{startChoice}')
    choice = input(f'\n{youTeacher}') 
    choice = choice.lower().replace(' ','')
    if choice == 'да' or choice == "yes":
        user = 'Преподаватель'
        return user
    if choice != 'да' or choice != "yes":
        choice = input(f'{youStudent}')
        choice = choice.lower().replace(' ','')
        if choice =='да' or choice == "yes":
            user = 'Ученик'
        return user
    return user

# Функция выбора предмета 

def lessonsChoice():
    lessonList = ['литература', 'русскийязык' , 'математика' ,'физкультура']
    print(12*'-')
    print('Литература\nРусский язык\nМатематика\nФизкультура')
    print(12*'-')
    lesson = input('Пожалуйста напишите название предмета: ')
    lesson = lesson.lower().replace(' ','')
    if lesson in lessonList:
        return lesson
    else: return'Такого предмета нет, повторите попытку.'

# Функция открытия документа 

def openLesson(arg): # аргумент из lessonsChoice()
    if arg == 'Такого предмета нет, повторите попытку.':
        exit
    else:
        with open(f'Task8\lessons\{arg}.txt', encoding = 'utf-8') as entered:
            document = entered.read()
            return document
document = openLesson('математика')  



with open('Task8\lessons\математика.txt', encoding='utf-8') as file: #Читаем файл
  lines = file.read().splitlines() # read().splitlines() - чтобы небыло пустых строк

dic = {} # Создаем пустой словарь
for line in lines: # Проходимся по каждой строчке
  key,value = line.split(': ') # Разделяем каждую строку по двоеточии(в key будет - пицца, в value - 01)
  dic.update({key:value})	 # Добавляем в словарь

print(dic['Иванов Сергей']) 