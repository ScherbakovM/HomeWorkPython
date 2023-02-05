from models import InitialChoice, lessonsChoice, openLesson, checked, addGrades,addStudents
from views import *

user = InitialChoice() # Выбор преподаватель или ученик

def action(arg): # Проверка и запуск фукнции  выбор урока для ученика и преподователя 
    if arg =='Преподаватель':
        print('-'  * 12)
        print('Чтобы проставить оценки выберите предмет из списка ниже:')
        return lessonsChoice()
    if arg == 'Ученик':
        surName,name = input('Enter you surname: '), input('Enter you name: ')
        global student
        student = f'{surName} {name}'
        student = student.lower()
        print(student)
        print('-'  * 12)
        print('Чтобы посмотреть свои оценки выберите предмет из списка ниже:')
        return lessonsChoice()
    if arg == warningChoice: exit(f'{sep}\n{warningChoice}')
    else: exit

lesson = action(user) # Выбранный предмет
doc = openLesson(lesson)


# Вывод оценок для ученика, добавление для преподавателя.
def printGrades():
    if user == 'Ученик':
        check = checked(student)
        if check == True:
            print(f'Ваши оценки по предмету - {lesson} : {doc[student]}')
        else: exit('У вас еще нет оценок по этому предмету!')
    if user == 'Преподаватель':
        global checkName, checkSurName
        checkSurName = input('Enter surname student : ').lower().replace(' ','')
        checkName = input('Enter name student: ').lower().replace(' ','')
        studentLog = f'{checkSurName} {checkName}'
        check = checked(studentLog)
        if check == True: # Если ученик есть
            print(f'{studentLog} : {doc[studentLog]}')
            answer = input(f'Add new grades? (yes) / Exit enter (no): ')
            if answer == 'yes':
                grades = input('Введите оценку :').replace(' ','')
                addGrades(lesson, studentLog, grades)                           
        else: 
            grades = input('Введите оценку :').replace(' ','')
            answerChek = input(f'{studentLog} dont have grades, add a student ? (yes) / (no)').lower().replace(' ','') # Если ученика нет
            if answerChek == 'yes':
                addStudents(lesson, studentLog, grades)
            else: exit("Bye!")
    else: exit("Bye!")
                                    
printGrades()
