import time
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.dispatcher.filters import Command
from State import Test 
from aiogram.dispatcher import FSMContext
from views import tg_Token

TOKEN = tg_Token
bot = Bot(token=TOKEN, parse_mode='html')
dp = Dispatcher(bot=bot, storage=MemoryStorage()) 
# storage=MemoryStorage  (from aiogram.contrib.fsm_storage.memory import MemoryStorage) нужно для смены статусов state в хендлере

@dp.message_handler(commands=['Del'], state=None)
async def answer_user(message: types.Message):
    await message.reply(f'<i>Введите текст в котором нужно удалить "абв"</i>')
    await Test.Q1.set() # Установка состояния для перехода к след хандлеру

@dp.message_handler(state=Test.Q1)
async def answer_user(message: types.Message, state:FSMContext):
    textMessage = message.text.lower()
    myList = textMessage.split(' ') # переводим в лист
    answer = list(filter(Del, myList)) # фильтруем без "абв"
    answer = " ".join(answer) # возвращаем в строку 
    await message.reply(answer)
    await state.update_data(answer1 = answer)
    await state.finish()
       
#Функция удалени 'абв'

def Del(x):
    for i in x:
        if 'абв' not in x:
            return True
        else: return False

if __name__ == '__main__':
    executor.start_polling(dp)


#  pip install aiogram
#  команда /Del для удаления абв
# Ссылка на боты для проверки t.me/deleteabcBot

