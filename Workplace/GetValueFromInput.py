import sqlite3

database = ('SGDatabase.db')

connect = sqlite3.connect(database)
cursor = connect.cursor()

inputname = input("Input name: ")

sql = ("""
    SELECT Nation FROM Ship
    WHERE Name = ?
""")

cursor.execute(sql, (inputname,))

names = next(zip(*cursor.description))
print(names)

rows = (cursor.fetchall())

for row in rows:
    print(row)

connect.commit()
