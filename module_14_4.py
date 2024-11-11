from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import get_all_products

products = get_all_products()

api = "7745156903:AAGuJ6Sa9-vW3i7B-vJyx3vZLdhxLMQ3yPM"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
keyboard.add(button_1)
keyboard.insert(button_2)
keyboard.add(button_3)
kb = InlineKeyboardMarkup()
bt_1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
bt_2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
kb.add(bt_1)
kb.insert(bt_2)
kb_new = InlineKeyboardMarkup(row_width=450)
bt_new_1 = InlineKeyboardButton('Product1', callback_data='product_buying')
bt_new_2 = InlineKeyboardButton('Product2', callback_data='product_buying')
bt_new_3 = InlineKeyboardButton('Product3', callback_data='product_buying')
bt_new_4 = InlineKeyboardButton('Product4', callback_data='product_buying')
kb_new.insert(bt_new_1)
kb_new.insert(bt_new_2)
kb_new.insert(bt_new_3)
kb_new.insert(bt_new_4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(len(products)):
        await message.answer(f'Название: {products[i][1]} | Описание: {products[i][2]} | Цена: {products[i][3]}')
        with open(f'files/{1+i}.jpg', 'rb') as jpg:
            await message.answer_photo(jpg)
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_new)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10×(вес в кг) + 6,25×(рост в см) – 5×(возраст в годах) + 5')
    await call.answer()


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
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
#    await message.answer(f'Ваша норма калорий {10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) -161}')
    await state.finish()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=keyboard)


@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
