import sqlite3

database = ('SGDatabase3.db')

connect = sqlite3.connect(database)
cursor = connect.cursor()

cursor.execute("""
INSERT INTO shiptest (info, infovalue, shipname)
VALUES ('tier', '1', 'mist')
""")

connect.commit()
