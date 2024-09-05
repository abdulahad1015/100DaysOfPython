from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FloatField
from wtforms.validators import DataRequired
import requests



'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Movies.db'
Bootstrap5(app)
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE DB
class movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    description: Mapped[str] = mapped_column(String, nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer,nullable=False)
    review: Mapped[str] = mapped_column(String, nullable=False)
    img_url: Mapped[str] = mapped_column(String,nullable=False)

class RateMovieForm(FlaskForm):
    rating = FloatField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])

# CREATE TABLE
# a=movie(title="B",description="a",rating=0.9,ranking=1,review="a",img_url="apple.com")
# with app.app_context():
#     db.session.add(a)
#     db.session.commit()
#     print("Done")



@app.route("/")
def home():
    with app.app_context():
        result=db.session.execute(db.select(movie))
        movies=result.scalars().all()
    return render_template("index.html",movies=movies)

@app.route("/edit",methods=['GET','POST'])
def edit():
    form = RateMovieForm()
    if form.validate_on_submit():
        pass
    return render_template("edit.html",form=form)


if __name__ == '__main__':
    app.run(debug=True)
