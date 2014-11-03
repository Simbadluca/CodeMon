var getFuncData = function(filename, functionName){
    var url = 'http://localhost:5000/kodemon/' + filename + '/' + functionName;

    $.ajax({
        async: false,
        type: 'GET',
        url: url,
        success: function(data) {
            var categories = [];
            var values = [];

            for(var key in data){
                var datetime = new Date(data[key].timestamp * 1000);
                categories.push(datetime);
                values.push(data[key].execution_time / 1000);
            }

            $('#container').highcharts({
                title: {
                    text: filename,
                    x: -20 //center
                },
                subtitle: {
                    text: functionName,
                    x: -20
                },
                xAxis: {
                    categories: categories
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
                    valueSuffix: 's'
                },
                legend: {
                    layout: 'vertical',
                    align: 'right',
                    verticalAlign: 'middle',
                    borderWidth: 0
                },
                series: [{
                    name: functionName,
                    data: values//[7.0, 6.9, 9.5, 14.5, 18.2, 14.5, 15.2, 1.5, 1.3, 18.3, 13.9, 9.6]
                }]
            });
        }
    });
};

var testFunc = function(){
    var data = $('#js').data();
    var filename = data.file;
    var functionName = data.function;

    getFuncData(filename, functionName);
};

$(document).ready(testFunc());