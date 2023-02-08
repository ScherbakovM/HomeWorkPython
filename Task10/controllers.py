import time
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from State import Test 
from aiogram.dispatcher import FSMContext
from views import tg_Token
from models import get_steps_lst, process_step, CheckR, logger

def run(arg):
    StepOne = get_steps_lst(arg) # Переводим строку в лист с разделение по операндам
    StepTwo = process_step(StepOne) # Для рассчетов 
    StepThre = CheckR(StepTwo) #Зацикливаем пока длина не равна 1
    return StepThre

# Для бота 

TOKEN = tg_Token
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot, storage=MemoryStorage()) 
# storage=MemoryStorage  (from aiogram.contrib.fsm_storage.memory import MemoryStorage) нужно для смены статусов state в хендлере

@dp.message_handler(commands=['calc'], state=None)
async def answer_user(message: types.Message):
    await message.reply(f'<i>Введие пример для расчета: </i>')
    await Test.Q1.set() # Установка состояния для перехода к след хандлеру

@dp.message_handler(state=Test.Q1)
async def answer_user(message: types.Message, state:FSMContext):
    textMessage = message.text # Ввод задания для расчета
    answer = run(textMessage) # Прогоняем через ран
    answer = "".join(map(str, answer)) # перевод в строку
    user_log = f'username : {message.from_user.username} id: {message.from_user.id} ввод: {message.text} вывод: {answer}\n' # лог
    logger(user_log)
    await message.reply(f'{textMessage} = {answer}')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp)
    
    
