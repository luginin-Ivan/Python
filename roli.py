import sqlite3

conn = sqlite3.connect("../chat_bot.db")
cursor = conn.cursor()

def new_roli(user_id):
    user = cursor.execute("SELECT `roli` FROM `roli` WHERE `user_id` = ?", (user_id,)).fetchall()
    if len(user) == 0:
        cursor.execute("INSERT OR IGNORE INTO `roli` (`user_id`,`roli`) VALUES (?,?)", (user_id, "младший модератор"))
        conn.commit()
        return "Пользователь повышен до младшего модератора"
    else:
        amount = user[0][0]
        if amount == "младший модератор":
            cursor.execute("UPDATE `roli` SET `roli` = ? WHERE  `user_id`= ?", ("старший модератор", user_id))
            conn.commit()
            return "Пользователь повышен до старшего модератора"


def prof_admin():
    def_admin = []
    print("омтоав"  in def_admin)
    user = cursor.execute("SELECT `user_id` FROM `roli` WHERE `roli` = ?", ("старший модератор",)).fetchall()
    if len(user) == 0:
        return def_admin
    else:

        for i in user[0]:
            def_admin.append(i)
        return def_admin

