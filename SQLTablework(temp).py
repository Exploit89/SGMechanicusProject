import sqlite3

database = ('SGDatabase.db')

connect = sqlite3.connect(database)
cursor = connect.cursor()

cursor.execute("""
    Enter your SQL code here
""")

names = next(zip(*cursor.description))
print(names)

rows = (cursor.fetchall())

for row in rows:
    print(row)

connect.commit()