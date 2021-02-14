import sqlite3

database = ('SGDatabase3.db')

connect = sqlite3.connect(database)
cursor = connect.cursor()

cursor.execute("""
SELECT infovalue FROM shiptest
WHERE shipname = 'mist'
""")

shipname = next(zip(*cursor.description))
print(shipname)

rows = (cursor.fetchone())

print(rows)

connect.commit()

misttier = int(rows[0])
print(misttier)
