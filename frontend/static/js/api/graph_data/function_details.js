var graphData = {
    count:         0,//length of the data array
    index:         0,//the index of the first item displayed on graph
    maxIndex:      0,//the index of the item displayed last plus one
    values:       [],//the values displayed on the graph
    categories:   [],//the categories displayed on the x-axis
    filename:     "",
    functionName: ""
};

var incrementIndex = function(){
    //check if it is possible to increase the index
    if(graphData.maxIndex < graphData.count - 1){
        graphData.index    += 1;
        graphData.maxIndex += 1;
    }
};

var decrementIndex = function(){
    //check if index is at the first possible position
    if(graphData.index > 0){
        graphData.index    -= 1;
        graphData.maxIndex -= 1;
    }
};

var setData = function(inputData, filename, functionName){
    graphData.filename = filename;
    graphData.functionName = functionName;
    graphData.count = inputData.length;

    for(var i = 0; i < inputData.length; i++){
        var datetime = new Date(inputData[i].timestamp * 1000);
        graphData.categories.push(datetime);
        graphData.values.push(inputData[i].execution_time / 1000);
    }

    if(graphData.count > 9){
        graphData.maxIndex = 10;
    }
    else{
        graphData.maxIndex = graphData.count - 1;
    }
};

var run = function(){
    //get the filename and function name
    var domData      = $('#js').data();
    var filename     = domData.file;
    var functionName = domData.function;

    //query the api for the function details
    //var ajax = getFuncData(filename, functionName);
    var ajax = getAllData(filename, functionName);

    ajax.success(function(apiData){
        setData(apiData);
    });

    var graph = generateGraph();
    var buttonsfunction = buttons();
};

$(document).ready(run());