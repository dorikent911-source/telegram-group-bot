import os
from aiogram import Bot, Dispatcher, executor, types

BOT_TOKEN = os.getenv(8426814098:AAHcy888nwH6P7cf3tS_7sxI9LYX8jz4n_w)
ADMIN_ID = int(os.getenv(7541414412))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(chat_type=[types.ChatType.GROUP, types.ChatType.SUPERGROUP])
async def group_message(message: types.Message):
    user = message.from_user

    await message.reply(
        "Xabaringiz qabul qilindi. "
        "Tez orada siz bilan shaxsiy chat orqali bog‘lanamiz."
    )

    username = f"@{user.username}" if user.username else "Username yo‘q"

    text = (
        "📩 Guruhdan yangi xabar\n\n"
        f"👤 Ism: {user.full_name}\n"
        f"🔗 Username: {username}\n"
        f"🆔 User ID: {user.id}\n"
        f"💬 Xabar:\n{message.text}"
    )

    await bot.send_message(ADMIN_ID, text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
