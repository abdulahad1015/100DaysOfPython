from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)
articles=Post()

@app.route("/")
def home():
    return render_template("index.html", posts=articles.posts)


@app.route("/post/<int:num>")
def get_post(num):
    if(num==1):
        return render_template("post.html", posts=articles.posts[0])
    if(num==2):
        return render_template("post.html", posts=articles.posts[1])
    if(num==3):
        return render_template("post.html", posts=articles.posts[2])
    else:
        return "Page not found"

if __name__ == "__main__":
    app.run(debug=True)
