import sqlite3

connection = sqlite3.Connection('not_telegram.db')
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
""")

#for i in range(10):
#   cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i+1}', f'example{i+1}@gmail.com', f'{(i+1)*10}', '1000'))

#for i in range(10):
#    if (i+1) % 2:
#        cursor.execute("UPDATE Users SET balance = ? WHERE id = ?", (500, f'{i+1}'))

#for i in range(10):
#    if (i*3 + 1) <= 10:
#        cursor.execute("DELETE FROM Users WHERE id = ?", (f'{i*3 + 1}',))
#    else:
#        break

#cursor.execute("SELECT * FROM Users")
#users = cursor.fetchall()
#for user in users:
#   print(user)

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')
connection.commit()
connection.close()
