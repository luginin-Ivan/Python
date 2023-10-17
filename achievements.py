import sqlite3
conn = sqlite3.connect("../chat_bot.db")
cursor = conn.cursor()

def achievements_new(achievements,user_id):
    user = cursor.execute("SELECT `achievements_user` FROM `achievements` WHERE `user_id` = ?", (user_id,)).fetchall()
    if len(user) == 0:
        cursor.execute("INSERT OR IGNORE INTO `achievements` (`achievements_user`,`user_id`) VALUES (?,?)", (achievements,user_id,))
        conn.commit()
        return "Достижение выдано"
    else:
        a = user[0][0]
        b = a + "," + achievements
        cursor.execute("UPDATE `achievements` SET `achievements_user` = ? WHERE  `user_id`= ?", (b, user_id))
        conn.commit()
        return "Достижение выдано"

def achievements_user(user_id):
    user = cursor.execute("SELECT `achievements_user` FROM `achievements` WHERE `user_id` = ?", (user_id,)).fetchall()
    if len(user) == 0:
        return "у вас нет достижений"
    else:
        a = user[0][0]
        return a


