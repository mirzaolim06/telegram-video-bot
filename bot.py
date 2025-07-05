import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.environ.get("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("Bot muvaffaqiyatli ishga tushdi!")

if __name__ == "__main__":
    from aiogram import executor
    executor.start_polling(dp)



