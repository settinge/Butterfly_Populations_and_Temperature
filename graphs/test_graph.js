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
            name: 'Temperature',
            orientation: 'h'
        };

    // adds styling to chart
    var scatterLayout={
        xaxis: {
            range: ['1997-11-15', '2022-02-15'],
            type: 'date'
        },
        title: 'Temperature', 
        margin: {
            t: 30
        }
    };

    //creates bar chart
    // Plotly.newPlot('scatter', [scatterData], scatterLayout);


d3.json("../data/total_butterfly_data.json").then(function(buttfly_data) {
    var arrayLength = buttfly_data.length;
    var datearray = [];
    var countarray = [];


    for (var i = 0; i < arrayLength; i++) {
        
       console.log(buttfly_data[i]);
       for (var x in buttfly_data[i]){
        console.log(x);
        datearray.push(x);
        console.log(buttfly_data[i][x]/300)
        countarray.push(buttfly_data[i][x]/300);
       }
    }
    

        var barData={
            y: countarray, 
            x: datearray, 
            type: 'scatter',
            name: 'Butterfly Count' // text: ['Thanksgiving Count 2020', 'New Years Count 2021', 'Thanksgiving Count 2021', 'New Years Count 2022'],
        };

    // adds styling to chart
    var layout = {
        xaxis: {
            range: ['1997-11-01', '2022-02-01'],
            type: 'date'
        },
        yaxis: {
          range: [0, 90]
        },
        title:'Butterfly Count in Monterey County 1997-2022'
     
    };

    //creates bar chart
    // Plotly.newPlot('bar', [barData], layout);
    var plotData = [scatterData, barData];

    var layout = {
        title: 'Temperature vs Butterfly Counts in Monterey: 1997 - 2022',
        yaxis: {title: 'Simple Contour Plot Axis', range: [0, 100]},
        yaxis2: {title: 'Line and Scatter Plot Axis', range: [0, 90]}
    };

    Plotly.newPlot('plotDiv', plotData, layout);

});
});
