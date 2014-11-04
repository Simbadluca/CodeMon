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

    graphData.filename = filename;
    graphData.functionName = functionName;
};
var getFuncData = function(filename, functionName){
    var url = 'http://localhost:5000/kodemon/es/fileandfunction';

    return $.ajax({
        type: 'POST',
        url: url,
        contentType: 'application/json',
        datatype: 'json',
        async: false,
        data: JSON.stringify({filename:filename, func_name:functionName})
    });
};

var generateGraph = function(){
    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    $('#static-graphcontainer').highcharts({
        title: {
            text: graphData.filename,
            x: -20 //center
        },
        subtitle: {
            text: graphData.functionName,
            x: -20
        },
        chart: {
            type: 'spline',
            animation: Highcharts.svg, // don't animate in old IE
            marginRight: 10,
            events: {
                load: function () {

                    var series = this.series[0];
                    var xAxis = this.xAxis;
                    $('#right-button').click(function(){
                        incrementIndex();

                        var x = graphData.categories[graphData.maxIndex],
                            y = graphData.values[graphData.maxIndex];
                        xAxis.categories = graphData.categories.slice(graphData.index, graphData.maxIndex);
                        console.log('x: ' + x);
                        console.log('y: ' + y);

                        series.addPoint([x, y], true, true);
                    });

                    $('#left-button').click(function () {
                        if (series.data.length) {
                            series.data[series.data.length - 1].remove();
                        }
                    });
                }
            }
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            categories: graphData.categories.slice(graphData.index, graphData.maxIndex)
        },
        yAxis: {
            title: {
                text: 'Value'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            formatter: function () {
                return '<b>' + this.series.name + '</b><br/>' +
                    Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                    Highcharts.numberFormat(this.y, 2);
            }
        },
        legend: {
            enabled: false
        },
        exporting: {
            enabled: false
        },
        series: [{
            data: graphData.values.slice(graphData.index, graphData.maxIndex),
            name: ' '
        }]
    });
};

var buttons = function(){
    $('#table-button').click(function(){
        $('#table-div').slideToggle(400);
    });

    $('#graph-button').click(function(){
        $('#static-graph').slideToggle(400);
    });
};

var run = function(){
    //get the filename and function name
    var domData      = $('#js').data();
    var filename     = domData.file;
    var functionName = domData.function;

    //query the api for the function details
    var ajax = getFuncData(filename, functionName);

    ajax.success(function(apiData){
        setData(apiData);
    });

    var graph = generateGraph();
    var buttonsfunction = buttons();
};

$(document).ready(run());