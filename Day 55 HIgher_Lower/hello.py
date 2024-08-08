from flask import Flask
import requests

response=requests.get("https://docs.google.com/forms/d/e/1FAIpQLSeg15H9Ry2k1SoBLF0PW_iV-Nfh5WQDAcpzyaLXjt3b16jdpw/viewform?usp=sf_link")

app = Flask(__name__)

@app.route("/")
def hello_world():
    return response.text

@app.route("/bye")
def bye():
    return "Bye"

@app.route("/<username>")
def username(username):
    return f"Hello {username} lalala"


if __name__ == "__main__":
    app.run(debug=True)