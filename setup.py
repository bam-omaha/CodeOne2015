import os
import server
from server import db, create_user, create_transaction, model
import csv

db.drop_all()
db.create_all()

admin_user = create_user('admin', 'admin@example.com', 'password', is_admin=True)

with open('checkingData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for description, category_name, amount, date in readCSV:
        category = model.Category.query.filter_by(title=category_name).first()
        if category is None:
            category = model.Category(category_name)
            db.session.add(category)
            db.session.commit()

        create_transaction(admin_user, description, amount, category, date)
