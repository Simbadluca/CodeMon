var run = function(){
    //get the filename and function name
    var domData      = $('#js').data();
    var filename     = domData.file;
    var functionName = domData.function;
    var minTimestamp = domData.min;
    var maxTimestamp = domData.max;

    var buttonfunctions = buttons();

    var staticGraph = generateStaticGraph(filename, functionName);
    var rangeGraph = generateRangeGraph(filename, functionName, minTimestamp, maxTimestamp);

};

$(document).ready(run());