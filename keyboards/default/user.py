from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mars Bozor"),
            KeyboardButton(text="Mahsulot q'shish")
        ],
        [
            KeyboardButton(text="Mening mahsulotlarim"),
            KeyboardButton(text="Profile")
        ]
    ], resize_keyboard=True
)