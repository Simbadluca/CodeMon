var buttons = function(){
    $('#table-button').click(function(){
        $('#table-div').slideToggle(400);
    });

    $('#static-graph-button').click(function(){
        $('#static-graph').slideToggle(400);
    });

    $('#range-graph-button').click(function(){
        $('#range-graph').slideToggle(400);
    });

    $('#graph-reset').click(function(){
        $('#range-graphcontainer').highcharts().destroy();
        $(this).attr('disabled', false);

        generateRangeGraph(graphData.filename, graphData.functionName, $('#start-textbox').val(), $('#end-textbox').val());
    });
};
