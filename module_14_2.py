import sqlite3

connection = sqlite3.Connection('not_telegram.db')
cursor = connection.cursor()

# Код из предыдущего задания

#
#cursor.execute("""
#CREATE TABLE IF NOT EXISTS Users(
#id INTEGER PRIMARY KEY,
#sername TEXT NOT NULL,
#mail TEXT NOT NULL,
#ge INTEGER,
#balance INTEGER NOT NULL
#
#"")
#
#for i in range(10):
#   cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i+1}', f'example{i+1}@gmail.com', f'{(i+1)*10}', '1000'))
#
#for i in range(10):
#    if (i+1) % 2:
#        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, f'{i+1}'))
#
#for i in range(10):
#    if (i*3 + 1) <= 10:
#        cursor.execute("DELETE FROM Users WHERE id = ?", (f'{i*3 + 1}',))
#    else:
#        break
#
#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
#users = cursor.fetchall()
#for user in users:
#    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

# Удаление пользователя с id=6
cursor.execute("DELETE FROM Users WHERE id = 6")

#cursor.execute("SELECT * FROM Users")
#users = cursor.fetchall()
#for user in users:
#    print(user)

# Подсчёт кол-ва всех пользователей
cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances/total_users)

connection.commit()
connection.close()
