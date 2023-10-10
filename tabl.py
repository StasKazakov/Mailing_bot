import gspread
from Functions import *
import time




def append_record(row):
    db = gspread.service_account(filename='key.json')
    sh = db.open("Offers")
    table = sh.worksheet('sent')
    table.append_row(row)
    


executed = get_data()
for number in range(len(executed)):
    row = executed[number]
    record = [row[1], row[2]]
    append_record(record)
    time.sleep(2)


