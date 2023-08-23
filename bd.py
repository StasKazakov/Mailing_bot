''''This modele criate new database.'''
import sqlite3

conn = sqlite3.connect('lids.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS lids (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shop TEXT NOT NULL,
    contact TEXT NOT NULL)''')

conn.commit()

cursor.close()
conn.close()