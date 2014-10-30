from flask import Flask

from data.database import Session
from data.models import Kodemon

"""
Flask server runs default on port: 5000
"""

# Get access to database
session = Session()

# Create an instance of Flask
app = Flask(__name__)

def formatResponce(sqlResponce):

    text = "{ result: [ "
    for elem in sqlResponce:
        text += elem.__str__()
        text += ", "

    # Remove the last comma
    text = text[:-2]
    text += " ]}"

    return text

# Get all Kodemon entries in database
@app.route("/kodemon/all")
def getAllEntryes():

    foundKodemon = session.query(Kodemon).all()

    if not foundKodemon:
        return "No entry found", 404
    else:
        jsonResponce = formatResponce(foundKodemon)

        return jsonResponce


# Get all entries in data base filtered by function name
@app.route("/kodemon/function/<func_name>")
def getFuncByName(func_name):

    foundKodemon = session.query(Kodemon).filter(Kodemon.func_name == func_name).all()

    if not foundKodemon:
        return "No entry found", 404
    else:
        jsonResponce = formatResponce(foundKodemon)

        return jsonResponce


# Get all entries in database filtered by filename
@app.route("/kodemon/file/<filename>")
def getFuncByFilename(filename):

    foundKodemon = session.query(Kodemon).filter(Kodemon.filename == filename).all()

    if not foundKodemon:
        return "No entry found", 404
    else:
        jsonResponce = formatResponce(foundKodemon)

        return jsonResponce


# Get all entries in database filtered by file and function name
@app.route("/kodemon/<filename>/<func_name>")
def getFuncByFileAndFuncName(filename, func_name):

    foundKodemon = session.query(Kodemon).filter(Kodemon.func_name == func_name and Kodemon.filename == filename).all()

    if not foundKodemon:
        return "No entry found", 404
    else:
        jsonResponce = formatResponce(foundKodemon)

        return jsonResponce


if __name__ == "__main__":
    app.run(debug=True)