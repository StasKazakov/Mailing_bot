''''This modele criate new database.'''
import sqlite3

conn = sqlite3.connect('lids.db')
cursor = conn.cursor()

# Code for clear database
# cursor.execute("DELETE FROM lids")

# Code for deleting rows.
# value_to_delete = 'Stas'
# cursor.execute("DELETE FROM lids WHERE shop = ?", (value_to_delete,))

cursor.execute('''CREATE TABLE IF NOT EXISTS lids (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shop TEXT NOT NULL,
    contact TEXT NOT NULL)''')

conn.commit()
cursor.close()
conn.close()