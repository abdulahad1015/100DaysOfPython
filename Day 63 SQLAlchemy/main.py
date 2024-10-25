#Was designed to use SqlLite but now modified to use MySql

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


class Base(DeclarativeBase):
    pass


app = Flask(__name__)

# MySQL database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/books_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Define the Book model (table schema)
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


# Ensure the tables are created when the app starts
with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book))
        all_books = result.scalars().all()
        if len(all_books) == 0:
            return render_template('index.html', books="0")
        return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        with app.app_context():
            data = request.form.to_dict()
            book = Book(title=data['title'], author=data['author'], rating=data['rating'])
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/delete/<num>", methods=['GET', 'POST'])
def delete(num):
    with app.app_context():
        result = db.session.execute(db.select(Book).where(Book.id == num))
        book = result.scalar()
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for('home'))


@app.route("/update/<num>", methods=['GET', 'POST'])
def update(num):
    if request.method == 'POST':
        data = request.form.to_dict()
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == num)).scalar()
            book_to_update.rating = data['rating']
            db.session.commit()
        return redirect(url_for('home'))
    else:
        with app.app_context():
            result = db.session.execute(db.select(Book).where(Book.id == num))
            book = result.scalar()
        return render_template('update.html', book=book)


if __name__ == "__main__":
    app.run(debug=True)
