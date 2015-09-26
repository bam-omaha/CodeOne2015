import os
import server
from server import db, create_user, model

db.drop_all()
db.create_all()

create_user('admin', 'admin@example.com', 'password', is_admin=True)
