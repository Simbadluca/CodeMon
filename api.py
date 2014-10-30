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

def createKodemonString(kodemonInstance):
    return '{"id": "', kodemonInstance.id,\
           '", "execution_time": "',  kodemonInstance.execution_time,\
           '", "timestamp": "', kodemonInstance.timestamp,\
           '", "token:" "', kodemonInstance.token, \
           '", "key": "', kodemonInstance.key, '"}'


@app.route("/kodemon/all")
def getAllEntryes():
    foundKodemon = session.query(Kodemon).all()

    text = "{ result: [ "
    if not foundKodemon:
        print "getAllEntryes() - 404"
        return "No entry found", 404
    else:
        for elem in foundKodemon:
            text += elem.__str__()
            text += ", "

        # Remove the last comma
        text = text[:-2]
        text += " ]}"

        return text


if __name__ == "__main__":
    app.run(debug=True)

"""
        jsonString = "{ 'results': ["

        for elem in foundKodemon:
            jsonString += createKodemonString(elem), ","

        jsonString = jsonString[:-1]
        jsonString += "]}"

        #print "getAllEntryes() - 200"
        """