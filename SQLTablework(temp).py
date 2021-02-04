import sqlite3

database = ('SGDatabase2.db')

connect = sqlite3.connect(database)
cursor = connect.cursor()

cursor.execute("""
    SELECT * FROM Ship 
""")

names = next(zip(*cursor.description))
print(names)

rows = (cursor.fetchall())

for row in rows:
    print(row)

connect.commit()