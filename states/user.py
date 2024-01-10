from aiogram.dispatcher.filters.state import State, StatesGroup

class RegisterState(StatesGroup):
    phone_number = State()
    login = State()
    password = State()