import sqlite3
conn = sqlite3.connect("../chat_bot.db")
cursor = conn.cursor()

def new_varn(user_id):
    user = cursor.execute("SELECT `amount_varn` FROM `varn` WHERE `user_id` = ?", (user_id,)).fetchall()
    if len(user) == 0:
        cursor.execute("INSERT OR IGNORE INTO `varn` (`user_id`,`amount_varn`) VALUES (?,?)", (user_id, 1))
        conn.commit()
        return "Количество варнов: 1"
    else:
        amount = user[0][0]
        if amount == 0:
            cursor.execute("UPDATE `varn` SET `amount_varn` = ? WHERE  `user_id`= ?", (1, user_id))
            conn.commit()
            return "Количество варнов: 1"
        elif amount == 1:
            cursor.execute("UPDATE `varn` SET `amount_varn` = ? WHERE  `user_id`= ?", (2, user_id))
            conn.commit()
            return "Количество варнов: 2"
        elif amount == 2:
            cursor.execute("UPDATE `varn` SET `amount_varn` = ? WHERE  `user_id`= ?", (3, user_id))
            cursor.execute("DELETE FROM `varn` WHERE `user_id` = ?", (user_id,))
            conn.commit()
            return "бан"

def minus_varn(user_id):
    user = cursor.execute("SELECT `amount_varn` FROM `varn` WHERE `user_id` = ?", (user_id,)).fetchall()
    if len(user) == 0:
        return "у данного пользователя нет варнов"
    else:
        amount = user[0][0]
        if amount == 0:
            return "у данного пользователя нет варнов"
        elif amount == 1:
            cursor.execute("UPDATE `varn` SET `amount_varn` = ? WHERE  `user_id`= ?", (0, user_id))
            conn.commit()
            return "У пользователя был снят варн"
        elif amount == 2:
            cursor.execute("UPDATE `varn` SET `amount_varn` = ? WHERE  `user_id`= ?", (1, user_id))
            conn.commit()
            return "У пользователя был снят варн"

def my_namber_of_varn(my_id):
    user = cursor.execute("SELECT `amount_varn` FROM `varn` WHERE `user_id` = ?", (my_id,)).fetchall()
    if len(user) == 0:
        return 0
        # await bot.send_message(message.chat.id, f"Количесвто ваших варнов: {0}")
    else:
        my_varn = user[0][0]
        return my_varn
        # await bot.send_message(message.chat.id, f"Количесвто ваших варнов: {my_varn}")

