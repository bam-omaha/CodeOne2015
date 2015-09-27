import json
import os
import server
from server import db, create_user, create_transaction, model
import csv

db.drop_all()
db.create_all()

admin_user = create_user('admin', 'admin@example.com', 'password', is_admin=True)

# Read in checking data
with open('checkingData.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for description, category_name, amount, date in readCSV:
        category = model.Category.query.filter_by(title=category_name).first()
        if category is None:
            category = model.Category(category_name)
            db.session.add(category)
            db.session.commit()

        print("Adding entry for {} at {}".format(category_name, date))
        create_transaction(admin_user, description, amount, category, date)

# Read in questions
with open("knowledgebase.json") as f:
    for topic_name, answer in json.load(f).items():
        print("Inserting knowledgebase item for", topic_name)
        knowledge = model.Knowledge(topic_name, answer)
        db.session.add(knowledge)
        db.session.commit()
