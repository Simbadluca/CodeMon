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
