from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id : Mapped[int] = mapped_column(Integer, primary_key=True)
    title:Mapped[str] = mapped_column(String(250),unique=True)
    author:Mapped[str] = mapped_column(String(250),nullable=False)
    rating: Mapped[float]=mapped_column(Float,nullable=False)


# with app.app_context():
#     book = Book(title='Harry Potter and the Philosophers Stone', author='J.K Rowling',rating=9.5)
#     db.session.add(book)
#     db.session.commit()

# with app.app_context():
#     result=db.session.execute(db.select(Book).where(Book.rating>9))
#
#     for i in result.scalars().all():
#         print(f"{i.title}, {i.author}, {i.rating}")



@app.route('/',methods=['GET','POST'])
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book))
        all_books=result.scalars().all()
        if(len(all_books)==0):
            return render_template('index.html', books="0")
        return render_template('index.html',books=all_books)


@app.route("/add",methods=['GET','POST'])
def add():
    if(request.method=='POST'):
        with app.app_context():
            data=request.form.to_dict()
            book=Book(title=data['title'],author=data['author'],rating=data['rating'])
            print(book)
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('home'))
    return render_template('add.html')

@app.route("/delete/<int:num>",methods=['GET','POST'])
def delete(num):
    



if __name__ == "__main__":
    app.run(debug=True)

