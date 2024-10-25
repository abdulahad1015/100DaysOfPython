from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,EmailField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap5
'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
app.secret_key = "danish786"
bootstrap =  Bootstrap5(app)

class MyForm(FlaskForm):
    email = EmailField(label='email', validators=[DataRequired()])
    password = PasswordField(label='password', validators=[DataRequired()])
    submit = SubmitField(label='login')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET','POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.email.data)
        if form.email.data=="abdulahad1015@gmail.com" and form.password.data=="12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html',form=form,bootstrap=bootstrap)

if __name__ == '__main__':
    app.run(debug=True)
