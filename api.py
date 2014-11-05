import time
import json
from flask import Flask, abort, request, Response
from flask.ext import restful

from data.database import Session
from data.models import Kodemon

from elasticsearch import Elasticsearch
from flask.ext.restful.utils import cors

"""
Flask server runs default on port: 5000
"""

# Get access to database
session = Session()

# Create an instance of Flask
app = Flask(__name__)
api = restful.Api(app)
api.decorators = [cors.crossdomain(origin='*', headers=['accept', 'Content-Type'])]

# Set up elasticsearch connection
es = Elasticsearch()


# Format SQL query to list
def kodemonToList(qr):
    result = []

    #for every row found in the query we construct a dictionary and add to the result list
    for i in range(0, len(qr)):
        result.append({'id': qr[i].id,
                       'execution_time': qr[i].execution_time,
                       'timestamp': qr[i].timestamp,
                       'token': qr[i].token,
                       'key': qr[i].key,
                       'func_name': qr[i].func_name,
                       'filename': qr[i].filename})

    return result


# Format ElasticSearch query to list
def ElasticSearchToList(responce):
    result = []

    print responce['hits']['total']

    for hit in responce['hits']['hits']:
        result.append({'id': hit["_source"]["id"],
                       'execution_time': hit["_source"]["execution_time"],
                       'timestamp': hit["_source"]["timestamp"],
                       'token': hit["_source"]["token"],
                       'key': hit["_source"]["key"],
                       'func_name': hit["_source"]["func_name"],
                       'filename': hit["_source"]["filename"]})

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
RESTFUL SQL Lite
"""

# Get all Kodemon entries in database
class AllSQL(restful.Resource):
    # GET
    def get(self):
        foundKodemon = session.query(Kodemon).all()

        if not foundKodemon:
            return abort(404)
        else:
            kodemonList = kodemonToList(foundKodemon)
            jsonResponce = json.dumps(kodemonList)

            return Response(jsonResponce, mimetype='application/json')

# Find all data about a function given its name and file location
class FileFunctionResource(restful.Resource):
    # POST
    def post(self):
        # Retrieve the json data from client
        data = json.loads(request.data)
        func_name = data.get('func_name')
        filename = data.get('filename')

        # Query the database
        foundKodemon = session.query(Kodemon).filter(
            Kodemon.func_name == func_name and Kodemon.filename == filename).all()

        # If query returns nothing
        if not foundKodemon:
            return abort(404)
        else:
            # Convert the query to a list of dictionaries
            kodemonList = kodemonToList(foundKodemon)
            # And create a json object
            jsonResponce = json.dumps(kodemonList)

            return Response(jsonResponce, mimetype='application/json')

    def options(self):
        pass


class GetFunctionByNameFileAndTimeRange(restful.Resource):
    # POST
    def post(self):
        # Retrieve the json data from client
        data = json.loads(request.data)
        func_name = data.get('func_name')
        filename = data.get('filename')
        startTime = data.get('start_time')
        endTime = data.get('end_time')

        # Query the database
        sql = session.query(Kodemon) \
            .filter(
            Kodemon.func_name == func_name and
            Kodemon.filename == filename) \
            .filter(
            Kodemon.timestamp.between(startTime, endTime)
        ).all()

        # If query returns nothing
        if not sql:
            return abort(404)
        else:
            # Convert the query to a list of dictionaries
            kodemonList = kodemonToList(sql)
            # And create a json object
            jsonResponse = json.dumps(kodemonList)
            return Response(jsonResponse, mimetype='application/json')

    def options(self):
        pass

# Add the sql functions to the api
api.add_resource(AllSQL, '/kodemon/sql/all')
api.add_resource(FileFunctionResource, '/kodemon/sql/fileandfunction')
api.add_resource(GetFunctionByNameFileAndTimeRange, '/kodemon/sql/functionandtime')

"""
RESTFUL Elastic Search
"""

# Get all Kodemon in elastic search
class AllElasticSearch(restful.Resource):
    # GET
    def get(self):
        res = es.search(index="kodemon", body={"query": {"match_all": {}}})

        if res['hits']['total'] > 0:
            kodemonList = ElasticSearchToList(res)
            jsonResponce = json.dumps(kodemonList)

            return Response(jsonResponce, mimetype='application/json')
        else:
            abort(404)

    def options(self):
        pass


# Get all Kodemon in elastic search filtered by function name
class GetFunctionByNameElasticSearch(restful.Resource):
    support_cors = True
    cors_origin = '*'
    cors_headers = 'origin, content-type, x-request-with'

    # POST
    def post(self):
        # Retrieve the json data from client
        data = json.loads(request.data)
        func_name = data.get('func_name')

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
            kodemonList = ElasticSearchToList(res)
            jsonResponce = json.dumps(kodemonList)

            return Response(jsonResponce, mimetype='application/json')
        else:
            abort(404)

    def options(self):
        return {'Allow': 'PUT'}, 200, \
               {'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'PUT,GET,POST'}


class GetFunctionsByFunctionNameAndFilenameElasticSearch(restful.Resource):
    # POST
    def post(self):
        # Retrieve the json data from client
        data = json.loads(request.data)
        func_name = data.get('func_name')
        filename = data.get('filename')

        res = es.search(index="kodemon",
                        body={
                            "query": {
                                "query_string": {
                                    "query": func_name,
                                    "default_field": "func_name"
                                }
                            },
                            "query": {
                                "query_string": {
                                    "query": filename,
                                    "default_field": "filename"
                                }
                            }
                        })
        if res['hits']['total'] > 0:
            kodemonList = ElasticSearchToList(res)
            jsonResponce = json.dumps(kodemonList)

            return Response(jsonResponce, mimetype='application/json')
        else:
            abort(404)

    def options(self):
        pass


class GetFunctionByNameFileAndTimeRangeElasticSearch(restful.Resource):
    # POST
    def post(self):
        # Retrieve the json data from client
        data = json.loads(request.data)
        func_name = data.get('func_name')
        filename = data.get('filename')
        startTime = data.get('start_time')
        endTime = data.get('end_time')

        res = es.search(index="kodemon",
                        body={
                            "query": {
                                "query_string": {
                                    "query": func_name,
                                    "default_field": "func_name"
                                }
                            },
                            "query": {
                                "query_string": {
                                    "query": filename,
                                    "default_field": "filename"
                                }
                            },
                            "query": {
                                "range": {
                                    "timestamp": {
                                        "from": startTime,
                                        "to": endTime
                                    }
                                }
                            }
                        })
        if res['hits']['total'] > 0:
            kodemonList = ElasticSearchToList(res)
            jsonResponce = json.dumps(kodemonList)

            return Response(jsonResponce, mimetype='application/json')
        else:
            abort(404)

    def options(self):
        pass


api.add_resource(AllElasticSearch, '/kodemon/es/all')
api.add_resource(GetFunctionByNameElasticSearch, '/kodemon/es/function')
api.add_resource(GetFunctionsByFunctionNameAndFilenameElasticSearch, '/kodemon/es/fileandfunction')
api.add_resource(GetFunctionByNameFileAndTimeRangeElasticSearch, '/kodemon/es/functionandtime')

if __name__ == "__main__":
    app.run(debug=True)