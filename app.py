from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from routes import main

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foodtracker.db'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@localhost:3306/foodtracker'
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app=app) #for binding flask app

app.register_blueprint(main)

log_food = db.Table('log_food',
    db.Column('log_id', db.Integer, db.ForeignKey('log.id'), primary_key=True),
    db.Column('food_id', db.Integer, db.ForeignKey('food.id'), primary_Key=True)
)

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    proteins = db.Column(db.Integer, nullable=False)
    carbs = db.Column(db.Integer, nullable=False)
    fats = db.Column(db.Integer, nullable=False)

    @property
    def calories(self):
        return self.proteins*4 + self.carbs*4 + self.fats*9


class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    track = db.relationship('Food', secondary=log_food)

def create_app():
    return 'test'

if __name__=='__main__':
    db.create_all()  #to create table through model class
    app.run(debug=True)
