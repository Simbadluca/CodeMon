import json
#import util
import urllib
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    welcome = "Hello World"
    return render_template("home.html", welcome=welcome)

@app.route('/functions/')
@app.route('/functions')
def functions():
    url = 'http://localhost:5000/kodemon/all'
    data = json.load(urllib.urlopen(url))["result"]
    return render_template('functions.html', list=data)

@app.route('/functions/<name>')
def function(name):
    url = 'http://localhost:5000/kodemon/function/' + name
    data = json.load(urllib.urlopen(url))['result'][0]
    return render_template('function.html', data=data)


if __name__ == '__main__':
    app.run(port=4500, debug=True)