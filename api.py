import time
import json
from flask import Flask, abort, request, Response
from flask.ext import restful
from crossdomdecorator import crossdomain

from data.database import Session
from data.models import Kodemon

from elasticsearch import Elasticsearch

"""
Flask server runs default on port: 5000
"""

# Get access to database
session = Session()

# Create an instance of Flask
app = Flask(__name__)
api = restful.Api(app)

# Set up elasticsearch connection
es = Elasticsearch()

def kodemonToList(qr):
    result = []

    for i in range(0, len(qr)):
        result.append({'id': qr[i].id,
                       'execution_time': qr[i].execution_time,
                       'timestamp': qr[i].timestamp,
                       'token': qr[i].token,
                       'key': qr[i].key,
                       'func_name': qr[i].func_name,
                       'filename': qr[i].filename})

    return result

def formatResponce(sqlResponce):

    text = '{ "result": [ '
    for elem in sqlResponce:
        text += elem.__str__()
        text += ", "

    # Remove the last comma
    text = text[:-2]
    text += " ]}"

    return text

def formatElasticResponce(responce):

    kode = []

    for hit in responce['hits']['hits']:
        kode.append( Kodemon(execution_time = hit["_source"]["execution_time"],
                    timestamp = hit["_source"]["timestamp"],
                    token = hit["_source"]["token"],
                    key = hit["_source"]["key"],
                    func_name = hit["_source"]["func_name"],
                    filename = hit["_source"]["filename"]) )

    result = '{"result": [ '


    for i in range(0, len(kode)):
        result += kode[i].__str__()
        result += ', '

    result = result[:-2]
    result += ' ]}'

    return result

# Checks if argument is epoch or datetime format and converts to
# epoch if the format is datetime.
# returns 400 if the format is wrong
def formatTime(aTimeFormat):

    try:
        int(aTimeFormat)
    except ValueError:
        try:
            timePattern = "%Y-%m-%d-%H:%M:%S"
            aTimeFormat = time.mktime(time.strptime(aTimeFormat, timePattern))
            aTimeFormat = str(int(aTimeFormat))
        except:
            return abort(400, "Error in date format. Format should be: 1337-13-37-13:37:00")

        return aTimeFormat
    else:
        return aTimeFormat

"""
RESTFUL
"""

class FileFunctionResource(restful.Resource):
    # POST
    @crossdomain(origin='*')
    def post(self):
        data = json.loads(request.data)
        func_name = data.get('func_name')
        filename = data.get('filename')
        foundKodemon = session.query(Kodemon).filter(Kodemon.func_name == func_name and Kodemon.filename == filename).all()

        if not foundKodemon:
            return abort(404)
        else:
            kodemonList = kodemonToList(foundKodemon)
            jsonResponce = json.dumps(kodemonList)

            return Response(jsonResponce, mimetype='application/json')

api.add_resource(FileFunctionResource, '/kodemon/fileandfunction')

"""
    Api calls to database
"""
# Get all Kodemon entries in database
@app.route("/kodemon/all")
def getAllEntryes():

    foundKodemon = session.query(Kodemon).all()

    if not foundKodemon:
        return abort(404)
    else:
        jsonResponce = formatResponce(foundKodemon)

        return jsonResponce


# Get all entries in data base filtered by function name
@app.route("/kodemon/function/<func_name>")
def getFuncByName(func_name):

    foundKodemon = session.query(Kodemon).filter(Kodemon.func_name == func_name).all()

    if not foundKodemon:
        return abort(404)
    else:
        jsonResponce = formatResponce(foundKodemon)

        return jsonResponce


# Get all entries in database filtered by filename
@app.route("/kodemon/file/<filename>")
def getFuncByFilename(filename):

    foundKodemon = session.query(Kodemon).filter(Kodemon.filename == filename).all()

    if not foundKodemon:
        return abort(404)
    else:
        jsonResponce = formatResponce(foundKodemon)

        return jsonResponce


# Get all entries in database filtered by file and function name
@app.route("/kodemon/<filename>/<func_name>")
@crossdomain(origin='*')
def getFuncByFileAndFuncName(filename, func_name):

    foundKodemon = session.query(Kodemon).filter(Kodemon.func_name == func_name and Kodemon.filename == filename).all()

    if not foundKodemon:
        return abort(404)
    else:
        kodemonList = kodemonToList(foundKodemon)
        jsonResponce = json.dumps(kodemonList)
        return Response(jsonResponce, mimetype='application/json')

"""
    Api calls to elastic search
"""
# Get all Kodemon entries in elasticsearch
@app.route("/kodemon/elastic/all")
def getAllEntryesElastic():

    res = es.search(index="kodemon", body={"query": {"match_all": {}}})

    if res['hits']['total'] > 0:
        responce = formatElasticResponce(res)

        return responce
    else:
        abort(404)


# Get all entries in data base filtered by function name
@app.route("/kodemon/elastic/function/<func_name>")
def getFuncByNameElastic(func_name):

    res = es.search(index="kodemon",
                body={
                    "query": {
                        "query_string": {
                            "query": func_name,
                            "default_field": "func_name"
                        }
                    }
                })

    if res['hits']['total'] > 0:
        responce = formatElasticResponce(res)

        return responce
    else:
        abort(404)

# Get all entries in database filtered by filename
# Get all entries in database filtered by file and function name

# Time format: "2011.08.29-11:05:02"
# Get all entries for a function in a given time range
@app.route("/kodemon/elastic/function/<func_name>/<time_min>_<time_max>")
def getFunctionByNameAndTimeRangeElastic(func_name, time_min, time_max):

    time_min = formatTime(time_min)
    time_max = formatTime(time_max)

    res = es.search(index="kodemon",
                body={
                    "query" : {
                        "range" : {
                            "timestamp" : {
                                "from" : time_min,
                                "to" : time_max
                            }
                        }
                    },
                    "query": {
                        "query_string": {
                            "query": func_name,
                            "default_field": "func_name"
                        }
                    }
                })

    if res['hits']['total'] > 0:
        responce = formatElasticResponce(res)

        return responce
    else:
        abort(404)


if __name__ == "__main__":
    app.run(debug=True)