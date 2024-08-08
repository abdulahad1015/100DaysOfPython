from flask import Flask
from random import randint

app = Flask(__name__)

number=randint(0,9)
print(number)

@app.route("/")
def hello_world():
    return '<h1>Guess a number between 1 and 9</h1>'\
    '<img src="https://media.giphy.com/media/HMbI4Bub3yPwgAa1wU/giphy.gif?cid=790b7611lng3v8ikjrlz1r8j02dfaktxwd6b2sgv3fc1wmq9&ep=v1_gifs_search&rid=giphy.gif&ct=g">'\

@app.route("/<int:guess_number>")
def guess(guess_number):
    global number
    if guess_number==number:
        return '<h1>Correct !</h1>' \
               '<img src="https://media.giphy.com/media/5dwzMo3lwPW8BY0u54/giphy.gif?cid=790b7611lng3v8ikjrlz1r8j02dfaktxwd6b2sgv3fc1wmq9&ep=v1_gifs_search&rid=giphy.gif&ct=g">' \

    elif guess_number>number:
        return '<h1>Too high</h1>' \
               '<img src="https://media.giphy.com/media/vPA5ZfXBapiAnxQIWs/giphy.gif?cid=790b7611lng3v8ikjrlz1r8j02dfaktxwd6b2sgv3fc1wmq9&ep=v1_gifs_search&rid=giphy.gif&ct=g">' \

    elif guess_number<number:
        return '<h1>Too Low</h1>' \
               '<img src="https://media.giphy.com/media/AFbmWvJKKpEcuU4Pvl/giphy.gif?cid=ecf05e47jmukptga7erozmvzmfmkm0di0d67ukqtap5ceyqz&ep=v1_gifs_search&rid=giphy.gif&ct=g">' \

if __name__ == "__main__":
    app.run(debug=True)



