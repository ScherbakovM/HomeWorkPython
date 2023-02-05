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
    lessonList = ['literature', 'russianlanguage' , 'mathematics','physicaltraining'] # Проверка существует ли такой предмет.
    print(12*'-')
    print('Mathematics\nRussian language\nLiterature\nPhysical training')
    print(12*'-')
    lesson = input('Пожалуйста напишите название предмета: ')
    lesson = lesson.lower().replace(' ','')
    if lesson in lessonList:
        return lesson
    else: exit('Такого предмета нет, повторите попытку.')

# Функция открытия документа и чтения

def openLesson(arg): # аргумент из lessonsChoice()
    if arg == 'Такого предмета нет, повторите попытку.':
        exit
    else:
        with open(f'Task8\lessons\{arg}.json') as f:
            global load
            load = json.load(f)
            return load

# print(openLesson('mathematics'))
# print(load['ivanov sergei'] + ' ' + '3')

# проверка есть-ли ученик в списке предмета

def checked(arg):
    check = arg in load.keys()
    if check == True:
        return True
    else: 
        return False
  
# добавить оценку 

def addGrades(arg, arg2, arg3):
        doc = openLesson(arg)
        doc[arg2] = doc[arg2] + ' ' + arg3 # Перезапись ключа с добавление новой оценки
        json.dump(doc, open(f'Task8\lessons\{arg}.json', 'w')) # Перезапись документа с учетом изменений 

# добавление нового ученика и первой оценки
      
def addStudents(predmet, addStud, grades):
        doc = openLesson(predmet)
        key, value = addStud, grades
        doc.update({key:value})
        print(doc)
        json.dump(doc, open(f'Task8\lessons\{predmet}.json', 'w'))

# listStudent.append(addStud)

    
    

