import json
import urllib
import urllib2
from flask import Flask, render_template
from datetime import date


app = Flask(__name__)

@app.route('/')
def functions():
    url = 'http://localhost:5000/kodemon/sql/all'
    data = json.load(urllib.urlopen(url))

    # a dictionary that hold all information about the functions run
    # format: {filename: {function_name: [{}, {}]}}
    func_dict = {}

    for i in range(0, len(data)):
        filename = data[i]['filename']
        func_name = data[i]['func_name']

        run_details = {'id': data[i]['id'],
                       'execution': data[i]['execution_time'],
                       'timestamp': data[i]['timestamp'],
                       'token': data[i]['token'],
                       'key': data[i]['key']}

        # check if filename and function have already been added to dictionary
        if not filename in func_dict:
            func_dict[filename] = {func_name: []}
        else:
            if not func_name in func_dict[filename]:
                func_dict[filename][func_name] = []

        # add the run instance details to the dictionary
        func_dict[filename][func_name].append(run_details)

    return render_template('functions.html', list=func_dict)


@app.route('/functions/<filename>-<func_name>')
def function(filename, func_name):
    url = 'http://localhost:5000/kodemon/sql/fileandfunction'
    values = json.dumps({'filename': filename, 'func_name': func_name})

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    response = json.load(urllib2.urlopen(req, values))

    return render_template('function.html', list=response)

@app.route('/test')
def test():
    url = 'http://localhost:5000/kodemon/es/all'
    data = json.load(urllib.urlopen(url))["result"]

    # a dictionary that hold all information about the functions run
    # format: {filename: {function_name: [{}, {}]}}
    func_dict = {}

    for i in range(0, len(data)):
        filename = data[i]['filename']
        func_name = data[i]['func_name']

        func_details = {'id': data[i]['id'],
                        'execution': data[i]['execution_time'],
                        'timestamp': data[i]['timestamp'],
                        'token': data[i]['token'],
                        'key': data[i]['key']}

        # check if filename and function have already been added to dictionary
        if not filename in func_dict:
            func_dict[filename] = {func_name: []}
        else:
            if not func_name in func_dict[filename]:
                func_dict[filename][func_name] = []

        func_dict[filename][func_name].append(func_details)

    return render_template('test.html', list=func_dict)

if __name__ == '__main__':
    app.run(port=4500, debug=True)