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
        title: 'Temperature', 
        margin: {
            t: 30
        }
    };

    //creates bar chart
    Plotly.newPlot('scatter', [scatterData], scatterLayout);

});

d3.json("../data/butterfly_data.json").then(function(buttfly_data) {
    var arrayLength = buttfly_data.length;
    var datearray = [];
    var countarray = [];


    for (var i = 0; i < arrayLength; i++) {
        
       console.log(buttfly_data[i]);
       for (var x in buttfly_data[i]){
        console.log(x);
        datearray.push(x);
        console.log(buttfly_data[i][x])
        countarray.push(buttfly_data[i][x]);
       }
    }
    

        var barData={
            y: countarray, 
            x: datearray, 
            type: 'bar'
        };

    // adds styling to chart
    var barLayout={
        title: 'Butterfly Count', 
        xaxis: {
            range: ['2020-11-01', '2022-02-01'],
            type: 'date'
          },
     
    };

    //creates bar chart
    Plotly.newPlot('bar', [barData], barLayout);

});