from flask import Flask, render_template
import geocoder

app = Flask(__name__)

@app.route('/')
def index():
    g = geocoder.ip('me')
    lat, lng = g.latlng
    return render_template('index.html', lat=lat, lng=lng)

if __name__ == "__main__":
    app.run(debug=True)