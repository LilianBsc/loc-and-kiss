import sqlite3

connection = sqlite3.connect('../data/database/database.db')


with open('../data/database/schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO database (username, email, password) VALUES (?, ?, ?)",
            ('Username1', 'email-1@mail.com', "password123")
            )

connection.commit()
connection.close()