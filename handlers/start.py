from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.user import user_main_menu

from keyboards.default.user import user_main_menu
from loader import dp, db_manager
from states.user import RegisterState
# from utils.misc.checker import login_def


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    check_user = await check(user_id=message.chat.id, channel=-1002035223730)
    if check_user is True:    
        user = db_manager.get
        if user:
            text = "Botimizaga xush kelibsiz"
            await message.answer(text=text, reply_markup=user_main_menu)
        else:
            text = "Iltimos telefon raqamingizni kiriting"  
            await message.answer(text=text)
            await RegisterState.phone_number.set()
    else: 
        text = f"Sen kanalga a'zo bo'lmagansan.\n{channels[2]}"
        await message.answer(text=text, reply_markup=ReplyKeyboardRemove())
         
   
