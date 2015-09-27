from flask.ext.sqlalchemy import SQLAlchemy
from flask import Markup

import calendar

from datetime import datetime, timedelta

class Model():
    def __init__(self, app):
        self.db = SQLAlchemy(app)
        db = self.db

        class Transaction(self.db.Model):
            __tablename__ = 'transactions'

            id = db.Column(db.Integer, primary_key=True)
            title = db.Column(db.String)
            amount = db.Column(db.Float)
            time = db.Column(db.DateTime)

            user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
            user = db.relationship('User', backref=db.backref('Transactions', lazy='dynamic'))

            category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
            category = db.relationship('Category', backref=db.backref('Transaction', lazy='dynamic'))

            def __init__(self, user, title, amount, category, time):
                self.user = user
                self.title = title
                self.amount = float(amount)
                self.category = category
                self.time = datetime.strptime(time, '%m/%d/%Y')
        self.Transaction = Transaction

        class Category(self.db.Model):
            __tablename__ = 'categories'

            id = db.Column(db.Integer, primary_key=True)
            title = db.Column(db.String)

            def __init__(self, title):
                self.title = title
        self.Category = Category

        class Knowledge(self.db.Model):
            __tablename__ = 'knowledges'

            id = db.Column(db.Integer, primary_key=True)
            topic_name = db.Column(db.String)
            answer = db.Column(db.String)

            def __init__(self, topic_name, answer):
                self.topic_name = topic_name
                self.answer = answer
        self.Knowledge = Knowledge

        class Budget(self.db.Model):
            __tablename__ = 'budget'

            id = db.Column(db.Integer, primary_key=True)
            limit= db.Column(db.Float)
            used = db.Column(db.Float)
            category = db.Column(db.String)

            user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
            user = db.relationship('User', backref=db.backref('Budget', lazy='dynamic'))


            def __init__(self, text, rating, category):
                self.text = text
                self.rating = rating
                self.category = category
        self.Budget = Budget

        class User(self.db.Model):
            __tablename__ = 'users'

            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(80))
            email = db.Column(db.String(120), unique=True)
            password = db.Column(db.String)
            authenticated = db.Column(db.Boolean())
            is_admin = db.Column(db.Boolean())
            is_anonymous = False

            def __init__(self, name, email, is_admin=False):
                self.name = name
                self.email = email
                self.authenticated = False
                self.is_admin = is_admin

            def __str__(self):
                return "User: {}".format((self.id, self.name, self.email, self.password, self.authenticated, self.is_admin))

            def is_authenticated(self) :
                return self.authenticated

            def is_active(self) :
                return self.is_authenticated()

            def get_id(self) :
                return self.email

            def get_id_num(self):
                return self.id
        self.User = User
