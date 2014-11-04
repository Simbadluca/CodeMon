var graphData = {
    count:         0,//length of the data array
    index:         0,//the index of the first item displayed on graph
    maxIndex:      0,//the index of the item displayed last plus one
    values:       [],//the values displayed on the graph
    categories:   [],//the categories displayed on the x-axis
    filename:     "",
    functionName: ""
};

var setupData = function(inputData, filename, functionName){
    graphData.filename = filename;
    graphData.functionName = functionName;
    graphData.count = inputData.length;

    for(var i = 0; i < inputData.length; i++){
        var datetime = new Date(inputData[i].timestamp * 1000);
        graphData.categories.push(datetime);
        graphData.values.push(inputData[i].execution_time / 1000);
    }

    if(graphData.count > 15){
        graphData.maxIndex = 14;
    }
    else{
        graphData.maxIndex = graphData.count - 1;
    }
};