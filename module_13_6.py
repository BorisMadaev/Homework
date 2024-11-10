from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
import asyncio

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
keyboard.add(button_1)
keyboard.insert(button_2)
kb = InlineKeyboardMarkup()
bt_1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
bt_2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
kb.add(bt_1)
kb.insert(bt_2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10×(вес в кг) + 6,25×(рост в см) – 5×(возраст в годах) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    # Для мужчин: BMR = 10×(вес в кг) + 6, 25×(рост в см) – 5×(возраст в годах) + 5
    # Для женщин: BMR = 10×(вес в кг) + 6, 25×(рост в см) – 5×(возраст в годах) – 161
    await message.answer(f'Ваша норма калорий {10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5}')
    # await message.answer(f'Ваша норма калорий {10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) -161}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
