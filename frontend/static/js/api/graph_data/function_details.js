var run = function(){
    //get the filename and function name
    var domData      = $('#js').data();
    var filename     = domData.file;
    var functionName = domData.function;

    //query the api for the function details
    //var ajax = getFuncData(filename, functionName);
    //var ajax = getAllData(filename, functionName);

    /*ajax.success(function(apiData){
        setData(apiData);
    });*/

    var graph = generateStaticGraph(filename, functionName);
    var buttonsfunction = buttons();
};

$(document).ready(run());