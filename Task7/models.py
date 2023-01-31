# Логика
from views import choice

# Запись ******************

def userEntered():
    global userData
    userData = ''

    userSurname = input("Введите вашу фамилию: ")
    
    with open('Task7/phonebook.txt','a', encoding='utf-8') as phonebook:
        phonebook.write(f'{userSurname}\n') #Спросили и записали фамилию 
        userData += (userSurname) + ','

    userName = input("Введите ваше имя: ")
    with open('Task7/phonebook.txt','a', encoding='utf-8') as phonebook:
        phonebook.write(f'{userName}\n') #Спросили и записали имя
        userData += (userName) + ','

    userPhone = input(f"{userName}, введите ваш телефон: ")
    with open('Task7/phonebook.txt','a', encoding='utf-8') as phonebook:
        phonebook.write(f'{userPhone}\n') #Спросили и записали телефон
        userData += (userPhone) + ','

    decriptionPhone = input("Введите описание (рабочий, личный): ")
    with open('Task7/phonebook.txt','a', encoding='utf-8') as phonebook:
        phonebook.write(f'{decriptionPhone}\n') #Спросили и записали описание
        userData += (decriptionPhone) 
    with open('Task7/phonebook.txt','a', encoding='utf-8') as phonebook:
            phonebook.write(f'***********\n') # Разделитель 
    with open('Task7/phoneBookString.txt','a', encoding='utf-8') as phoneBookString:
            phoneBookString.write(f'{userData}\n') # Разделитель 

# Чтение **********************
   
def read():
    with open('Task7/phonebook.txt','r', encoding='utf-8') as phonebook:
        print(phonebook.read())
    with open('Task7/phoneBookString.txt','r', encoding='utf-8') as phoneBookString:
        phoneBookString = phoneBookString.read()
        print(phoneBookString)





