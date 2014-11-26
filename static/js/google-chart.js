var aController = true;
var ChartLeftIndent = 50;
var ChartWidth = "85%";
function checkWindowWidth(){
    if($(window).width() <= (BREAK.MN)){
        ChartLeftIndent = 30;
        ChartWidth = "85%";
    }else if($(window).width() <= (BREAK.VS)){
        ChartLeftIndent = 35;
        ChartWidth = "85%";
    }else{
        ChartLeftIndent = 50;
        ChartWidth = "85%";
    }
}checkWindowWidth();
function drawChart() {
    var data = google.visualization.arrayToDataTable([
        ['Year', 'Sales'],
        [1,  20],
        [2,  30],
        [3,  24],
        [4,  40],
        [5,  28],
        [6,  34],
        [7,  29],
        [8,  20],
        [9,  30],
        [10,  25],
        [11,  40],
        [12,  27]
    ]);



    var options = {
        titleTextStyle: {color: '#fff', fontName: "<global-font-name>", fontSize: "16"},
        axisTitlesPosition: 'out',
        backgroundColor: {fill: "#ef743d" },
        chartArea:{left:ChartLeftIndent,top:20,width:ChartWidth,height:'83%'},
        hAxis:{
            textStyle: {
                color: '#fff',
                fontName: "<global-font-name>"
            },
            baselineColor: "#f5a581",
            gridlines: {
                color: '#f5a581',
                count: '12'
            }
        },
        vAxis:{
            textStyle: {
                color: '#fff',
                fontName: "<global-font-name>"
            },
            maxValue: "50",
            baselineColor: "#f5a581",
            gridlines: {
                color: '#f5a581'
            }
        },
        legend: "none",
        pointSize: 7,
        series: {
            0: { color: '#fff', pointShape: 'circle' }
        }
    }

    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, options);
    $( window ).on('resize', function(){
        if (aController){
            resizeController();
        }
    });
}
if($('.b-chart').size() > 0){
    google.load("visualization", "1.1", {packages:["corechart"]});

    google.setOnLoadCallback(drawChart());

}
var timeout;
var controllerCounter = 0;
function resizeController(){
    if(controllerCounter < 1){
        aController = false;
        clearTimeout(timeout);
        timeout = setTimeout(function(){
            if (aController){
                controllerCounter++;
            }else{
                controllerCounter = 0;
            }
            resizeController();
            aController = true;
        }, 100);
    }else{
        aController = true;
        controllerCounter = 0;
        checkWindowWidth();
        drawChart();
    }
}