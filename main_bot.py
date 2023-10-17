import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, Message
from achievements import *
from config import TOKEN
from varn import *
from roli import *

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"], commands_prefix="!/")
async def cmd_ban(message: types.Message):
    a = ["a","b"]
    b = ["Kur0WasMi2take","Kur0WasMi2take"]
    c = "https://t.me/"
    name = ''
    for i in range(len(a)):
        name += f"<a href='{c+b[i]}'>{a[i]}</a>"+ "\n"

    await bot.send_message(message.chat.id, name, parse_mode="html")

#команда бана пользователя, через ответ на сообщение
@dp.message_handler(commands=["ban"], commands_prefix="!/")
async def cmd_ban(message: types.Message):
    prof = prof_admin()
    a = []
    chat_admins = await bot.get_chat_administrators(message.chat.id)
    for admins in chat_admins:
        userId = admins.user.id
        a.append(userId)
    if message.from_user.id in a or message.from_user.id in prof:
        if not message.reply_to_message:
            await message.reply("это должен быть ответ на сообщение")
            return
        # await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
        await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)
        #в команде message.reply_to_message.from_user хранятся данные аккаунта, на который мы отвечаем
        await message.delete()
        a1 = "https://t.me/" + message.reply_to_message.from_user.username
        b1 = message.reply_to_message.from_user.full_name
        await bot.send_message(message.chat.id, f" пользователь <a href='{a1}'>{b1}</a>" + "\n" + "забанен", parse_mode="HTML",disable_web_page_preview = True)

    else:
        await bot.send_message(message.chat.id, "У тебя нет прав банить!")

#команда выдачи варна
@dp.message_handler(commands=["varn"], commands_prefix="!/")
async def cmd_ban(message: types.Message):
    global a
    a = []
    chat_admins = await bot.get_chat_administrators(message.chat.id)
    for admins in chat_admins:
        userId = admins.user.id
        a.append(userId)

    if message.from_user.id in a:
        if not message.reply_to_message:
            await message.reply("это должен быть ответ на сообщение")

        else:
            user_id = message.reply_to_message.from_user.id
            varn = new_varn(user_id)
            if varn == "бан":
                await bot.kick_chat_member(chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id)

                await message.reply_to_message.reply("Пользователь исключен ")
            else:
                await bot.send_message(message.chat.id, varn)
    else:
        await bot.send_message(message.chat.id, "У тебя нет прав использовать эту команду")

#команда снятия варна
@dp.message_handler(commands=["unvarn"], commands_prefix="!/")
async def cmd_ban(message: types.Message):
    global a
    a = []
    chat_admins = await bot.get_chat_administrators(message.chat.id)
    for admins in chat_admins:
        userId = admins.user.id
        a.append(userId)

    if message.from_user.id in a:
        if not message.reply_to_message:
            await message.reply("это должен быть ответ на сообщение")
            return

        user_id = message.reply_to_message.from_user.id
        varn = minus_varn(user_id)
        await bot.send_message(message.chat.id, varn)

    else:
        await bot.send_message(message.chat.id, "У тебя нет прав отчислять студента!")

@dp.message_handler(commands=["new_message"])
async def cmd_ban(message: types.Message):
    global b
    b = []
    chat_admins = await bot.get_chat_administrators(message.chat.id)
    for admins in chat_admins:
        userId = admins.user.id
        b.append(userId)

    if message.from_user.id in b:
        new_message = message.text[13:]
        open_file = open("./new_message.txt", "w", encoding="UTF-8")
        global a
        a = []
        chat_admins = await bot.get_chat_administrators(message.chat.id)
        for admins in chat_admins:
            userId = admins.user.id
            a.append(userId)

        if message.from_user.id in a:
            if not message.reply_to_message:
                await message.reply("это должен быть ответ на сообщение")
                return
        open_file.write(new_message)
        await bot.send_message(message.chat.id, "приветсвенное сообщение обновленно")



@dp.message_handler(commands=["повысить"], commands_prefix="!/")
async def cmd_ban(message: types.Message):

        user_id = message.reply_to_message.from_user.id
        ab = new_roli(user_id)
        await bot.send_message(message.chat.id, ab)


@dp.message_handler(content_types=[ContentType.NEW_CHAT_MEMBERS])
async def new_members_handler(message: Message):
    new_member = message.new_chat_members[0]
    n = "https://t.me/" + new_member.username
    b = new_member.full_name
    open_file = open("./new_message.txt", "r", encoding="UTF-8")
    read_file = open_file.read()
    await bot.send_message(message.chat.id, f"<a href='{n}'>{b}</a>" + "\n" + read_file, parse_mode="HTML",disable_web_page_preview = True)

@dp.message_handler(content_types=[ContentType.LEFT_CHAT_MEMBER])
async def new_members_handler(message: Message):
    await bot.send_message(message.chat.id, "пользоватлеь вышел")

@dp.message_handler(content_types=["text"])
async def cmd_ban(message: types.Message):
    if message.text == "мои варны" or message.text == "Мои варны":
        my_id = message.from_user.id
        my_varn = my_namber_of_varn(my_id)
        if my_varn == 0:
            await bot.send_message(message.chat.id,f"Количесвто ваших варнов: {0}")
        else:
            await bot.send_message(message.chat.id,f"Количесвто ваших варнов: {my_varn}")
    elif "выдать достижение" in message.text:
        achievements = message.text[12:]
        user_id = message.reply_to_message.from_user.id
        def_achievements = achievements_new(achievements,user_id)
        await bot.send_message(message.chat.id,def_achievements)
    elif message.text == "мои достижения":
        user_id = message.from_user.id
        user_username = "https://t.me/" + message.from_user.username
        user_name = message.from_user.full_name
        def_achievements_user = achievements_user(user_id)
        await bot.send_message(message.chat.id, f"У пользваотеля <a href = '{user_username}'>{user_name}</a> получены достижения:" +"\n"+ def_achievements_user, parse_mode="html", disable_web_page_preview=True)
    #фильтр сообщений
    else:
        open_varn_list = open("./varn_list.txt", "r",encoding="UTF-8")
        read_varn_list = open_varn_list.readlines()
        for i in read_varn_list:
            new = i.replace("\n","")
            if new == '':
                continue
            else:
                if new in message.text.lower():
                    await bot.delete_message(message.chat.id, message.message_id)
                    break


        # for i in read_varn_list:
        #     new = i.replace("\n","")
        #     if new == '':
        #         continue
        #     else:
        #         a.append(new)
        #     if message.text.lower() in a:
        #         await bot.delete_message(message.chat.id, message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp)