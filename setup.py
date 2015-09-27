import os
import server
from server import db, create_user, create_transaction, model
import csv

db.drop_all()
db.create_all()

create_user('admin', 'admin@example.com', 'password', is_admin=True)

with open('checkingData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    # 1 is description ,2 is category, 3 is amount, date
    for row in readCSV:
        create_transaction('admin',row[0],row[2],row[1],row[3])

