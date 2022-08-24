d3.json("../data/temp_data.json").then(function(data) {
    var arrayLength = data.length;
    var datearray = [];
    var temparray = [];

    for (var i = 0; i < arrayLength; i++) {
        
        datearray.push(data[i]["Date"]);
        temparray.push(data[i]["Temp"]);
    }

        var scatterData={
            y: temparray, 
            x: datearray, 
            type: 'scatter', 
            orientation: 'h'
        };

    // adds styling to chart
    var scatterLayout={
        title: 'Temperature and Butterfly Populations', 
        margin: {
            t: 30
        }
    };

    //creates bar chart
    Plotly.newPlot('scatter', [scatterData], scatterLayout);

});