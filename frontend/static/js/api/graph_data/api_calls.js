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

var getAllData = function(filename, functionName){
    var url = 'http://localhost:5000/kodemon/sql/fileandfunction';
    var dataObject = {filename:filename, func_name:functionName};
    return getFuncData(url, dataObject);
};

var getDataByRange = function(filename, functionName, start_time, end_time){
    var url = 'localhost:5000/kodemon/es/functionandtime';
    var dataObject = {
        filename:filename,
        functionName:functionName,
        start_time:start_time,
        end_time:end_time
    };
    return getFuncData(url, dataObject);
};