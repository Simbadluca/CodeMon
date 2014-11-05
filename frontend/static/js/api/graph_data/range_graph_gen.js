var generateRangeGraph = function(filename, functionName, start_time, end_time){
    var apiData = getDataByRange(filename, functionName, start_time, end_time);

    apiData.success(function(data){
        setupData(data, filename, functionName);
    });

    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    $('#range-graphcontainer').highcharts({
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
                text: 'Time in seconds'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
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