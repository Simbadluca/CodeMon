// The base ajax function, at this point it always assumes POST and json
// Input: api URL and the dataobject to be sent via POST
var getFuncData = function(url, dataObject){
    return $.ajax({
        type: 'POST',
        url: url,
        contentType: 'application/json',
        datatype: 'json',
        async: false,
        data: JSON.stringify(dataObject)
    });
};

// Get all data related to a function based on the function name and its file
var getAllData = function(filename, functionName){
    var url = 'http://localhost:5000/kodemon/sql/fileandfunction';
    var dataObject = {filename:filename, func_name:functionName};
    return getFuncData(url, dataObject);
};

// Get all data related to a function based on the function name, its file, and the supplied range of timestamps
var getDataByRange = function(filename, functionName, start_time, end_time){
    var url = 'http://localhost:5000/kodemon/sql/functionandtime';
    var dataObject = {
        filename:filename,
        func_name:functionName,
        start_time:start_time,
        end_time:end_time
    };
    return getFuncData(url, dataObject);
};