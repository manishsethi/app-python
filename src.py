import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

class User(db.Model):
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(80), unique=True)
   email = db.Column(db.String(120), unique=True)

   def __init__(self, username, email):
       self.username = username
       self.email = email

   def __repr__(self):
       return '<User %r>' % self.username

@app.route("/users")
def users_index():
   to_json = lambda user: {"id": user.id, "name": user.username, "email": user.email}
   return json.dumps([to_json(user) for user in User.query.all()])
