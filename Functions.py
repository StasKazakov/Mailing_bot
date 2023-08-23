import sqlite3

# Function to entry new row in table.
def add_entry(shop, contact):
    try:
        conn = sqlite3.connect('lids.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO lids (shop, contact) VALUES (?, ?)", (shop, contact))
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# Function to get all information from database.
def get_data():
    try:
        conn = sqlite3.connect('lids.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lids")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

