import json
import urllib
import urllib2
from flask import Flask, render_template

# Create the flask app
app = Flask(__name__)

# Index directory
@app.route('/')
def functions():
    # Set the url for the api
    url = 'http://localhost:5000/kodemon/sql/all'
    # Get the json data from the url
    data = json.load(urllib.urlopen(url))

    # a dictionary that hold all information about the functions run
    # format: {filename: {function_name: [{}, {}]}}
    func_dict = {}

    for i in range(0, len(data)):
        # Store the function file location
        filename = data[i]['filename']
        # Store the functions name
        func_name = data[i]['func_name']

        # All other function details are stored in a dictionary
        run_details = {'id': data[i]['id'],
                       'execution': data[i]['execution_time'],
                       'timestamp': data[i]['timestamp'],
                       'token': data[i]['token'],
                       'key': data[i]['key']}

        # If filename has not already added to dictionary
        if not filename in func_dict:
            func_dict[filename] = {func_name: []}
        else:
            # If this function has not already been added as value to the file key
            if not func_name in func_dict[filename]:
                # All relevant run details are stored as a list of dictionaries
                func_dict[filename][func_name] = []

        # add the run instance details to the dictionary
        func_dict[filename][func_name].append(run_details)

    return render_template('functions.html', list=func_dict)


@app.route('/functions/<filename>-<func_name>')
def function(filename, func_name):
    # Set the url for the api
    url = 'http://localhost:5000/kodemon/sql/fileandfunction'
    # Setup the data values to be sent to the api
    values = json.dumps({'filename': filename, 'func_name': func_name})

    # Get the json data from the url
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    response = json.load(urllib2.urlopen(req, values))

    return render_template('function.html', list=response)

if __name__ == '__main__':
    app.run(port=4500, debug=True)