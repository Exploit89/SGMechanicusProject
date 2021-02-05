import sqlite3

database = ('SGDatabase3.db')

connect = sqlite3.connect(database)
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE Ship(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL    
""")

names = next(zip(*cursor.description))
print(names)

rows = (cursor.fetchall())

for row in rows:
    print(row)

connect.commit()