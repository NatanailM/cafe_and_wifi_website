import os

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/natan/Documents/Python/Portfolio/Cafe and Wifi Website/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    coffee_price = db.Column(db.String(250), nullable=False)


@app.route("/")
def home():
    all_cafes = db.session.query(Cafe).all()
    return render_template("index.html", all_cafes=all_cafes)


@app.route("/cafe/<int:cafe_id>")
def cafe(cafe_id):
    current_cafe = Cafe.query.get(cafe_id)

    return render_template("cafe.html", cafe=current_cafe)


if __name__ == '__main__':
    app.run(debug=True)
