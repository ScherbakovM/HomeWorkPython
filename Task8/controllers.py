from models import InitialChoice, lessonsChoice, openLesson
from views import actionStudent, actionTeacher

user = InitialChoice()

print(user)

def action(arg):
    if arg =='Преподаватель':
        print(f'\n{actionTeacher}')
        return lessonsChoice()
    if arg == 'Ученик':
        print(f'\n{actionStudent}')
        return lessonsChoice()
    else: exit

lesson = action(user)

document = openLesson(lesson)
