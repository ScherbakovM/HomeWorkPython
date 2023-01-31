# Связываем пользователя и логику ( views & models )

from models import userEntered, read
from views import choice

userChoice = choice().lower() # Что хочет пользователь ?

def run():
    if(userChoice == "записать"):
         return userEntered() # Запись
        
    if(userChoice == "вывести справочник" or userChoice == "вывести"):
        return read() # Вывод справочника
        
    else: 
        exit('ERROR 404, повторите попытку! Необходимо вводить: "записать" или "вывести справочник"')
run()


