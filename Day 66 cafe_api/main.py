from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Query
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
    map_url: Mapped[str] = mapped_column(String(500), nullable=True)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=True)
    seats: Mapped[str] = mapped_column(String(250), nullable=True)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=True)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=True)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=True)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    result = None
    with app.app_context():
        result = db.session.execute(db.select(Cafe))
        result = result.scalars().all()
        result = random.choice(result)
    if result:
        cafe_data = {
            "id": result.id,
            "name": result.name,
            "map_url": result.map_url,
            "img_url": result.img_url,
            "location": result.location,
            "seats": result.seats,
            "has_toilet": result.has_toilet,
            "has_wifi": result.has_wifi,
            "has_sockets": result.has_sockets,
            "can_take_calls": result.can_take_calls,
            "coffee_price": result.coffee_price
        }
        return jsonify(cafe_data)
    else:
        return jsonify({"error": "No cafes found"}), 404


@app.route("/search", methods=['GET'])
def seacrh_cafe():
    location = request.args.get("loc")
    print(location)
    result = None
    with app.app_context():
        result = db.session.execute(db.select(Cafe).where(Cafe.location == location))
        result = result.scalars().all()
    cafeList = []
    print(result)
    for i in result:
        cafe_data = {
            "id": i.id,
            "name": i.name,
            "map_url": i.map_url,
            "img_url": i.img_url,
            "location": i.location,
            "seats": i.seats,
            "has_toilet": i.has_toilet,
            "has_wifi": i.has_wifi,
            "has_sockets": i.has_sockets,
            "can_take_calls": i.can_take_calls,
            "coffee_price": i.coffee_price
        }
        cafeList.append(cafe_data)

    if not cafeList:
        return jsonify({"error": "No cafes found"}), 404
    else:
        return jsonify(cafeList)


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
                    "id": i.id,
                    "name": i.name,
                    "map_url": i.map_url,
                    "img_url": i.img_url,
                    "location": i.location,
                    "seats": i.seats,
                    "has_toilet": i.has_toilet,
                    "has_wifi": i.has_wifi,
                    "has_sockets": i.has_sockets,
                    "can_take_calls": i.can_take_calls,
                    "coffee_price": result.coffee_price}
            }
        return jsonify(cafe_data)


# HTTP POST - Create Record
@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    print(db.session.add(new_cafe, _warn=True))
    db.session.commit()
    return jsonify({"response": {"success": "Sucessfully added a new cafe"}})


# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    price = request.args.get("new-price")
    cafe = db.get_or_404(Cafe, cafe_id)
    if cafe:
        cafe.coffee_price = price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=['DELETE'])
def report_closed(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id)
    api_key=request.args.get("api-key")
    if api_key=="TopSecret":
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the record."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})
    else:
        return jsonify(error={"Not Authorized": "Please enter a valid Key."})

if __name__ == '__main__':
    app.run(debug=True)
