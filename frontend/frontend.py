from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    welcome = "Hello World"
    return render_template("home.html", welcome=welcome)


if __name__ == '__main__':
    app.run(port=4500, debug=True)