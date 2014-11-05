var graphData = {};

var setupData = function(inputData, filename, functionName){
    graphData = {
        count:         0,//length of the data array
        index:         0,//the index of the first item displayed on graph
        maxIndex:      0,//the index of the item displayed last plus one
        values:       [],//the values displayed on the graph
        categories:   [],//the categories displayed on the x-axis
        filename:     "",
        functionName: ""
    };


    graphData.filename = filename;
    graphData.functionName = functionName;
    graphData.count = inputData.length;

    for(var i = 0; i < inputData.length; i++){
        //setup the displayed time
        var datetime = new Date(inputData[i].timestamp * 1000);
        var time = datetime.getHours() + ':' + datetime.getMinutes() + ':' + datetime.getSeconds();

        graphData.categories.push(time);
        graphData.values.push(inputData[i].execution_time / 1000);
    }

    graphData.maxIndex = graphData.count;
};