from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt
 
On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random")
def random_cafe():
    result = None
    with app.app_context():
        result = db.session.execute(db.select(Cafe))
        result = result.scalars().all()
        result = random.choice(result)
    if result:
        cafe_data = {
            "id":result.id,
            "name":result.name,
            "map_url":result.map_url,
            "img_url":result.img_url,
            "location": result.location,
            "seats":result.seats,
            "has_toilet":result.has_toilet,
            "has_wifi":result.has_wifi,
            "has_sockets":result.has_sockets,
            "can_take_calls":result.can_take_calls,
            "coffee_price":result.coffee_price
        }
        return jsonify(cafe_data)
    else:
        return jsonify({"error": "No cafes found"}), 404

@app.route("/all")
def all_cafes():
    result = None
    with app.app_context():
        result = db.session.execute(db.select(Cafe))
        result = result.scalars().all()

    if result:
        for i in result:
            cafe_data = {
                {
                "id":i.id,
                "name":i.name,
                "map_url":i.map_url,
                "img_url":i.img_url,
                "location": i.location,
                "seats": i.seats,
                "has_toilet": i.has_toilet,
                "has_wifi": i.has_wifi,
                "has_sockets": i.has_sockets,
                "can_take_calls": i.can_take_calls,
                "coffee_price":result.coffee_price}
            }
        return jsonify(cafe_data)

# HTTP GET - Read Record

# HTTP POST - Create Record

# HTTP PUT/PATCH - Update Record

# HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)
