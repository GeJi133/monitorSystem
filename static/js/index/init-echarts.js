$(document).ready(function() {




    <!--Rainfall and Evaporation echarts init-->

    var dom = document.getElementById("rainfall");
    var rainChart = echarts.init(dom);

    var app = {};
    option = null;
    option = {
        color: ['#A768F3','#36a2f5'],
        tooltip : {
            trigger: 'axis'
        },
        legend: {
            data:['Sale','Market']
        },
        calculable : true,
        xAxis : [
            {
                type : 'category',
                data : ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
            }
        ],
        yAxis : [
            {
                type : 'value'
            }
        ],
        series : [
            {
                name:'Sale',
                type:'bar',
                data:[2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                markPoint : {
                    data : [
                        {type : 'max', name: 'Max'},
                        {type : 'min', name: 'Min'}
                    ]
                },
                markLine : {
                    data : [
                        {type : 'average', name: 'Average'}
                    ]
                }
            },
            {
                name:'Market',
                type:'bar',
                data:[2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
                markPoint : {
                    data : [
                        {name : 'Max', value : 182.2, xAxis: 7, yAxis: 183, symbolSize:18},
                        {name : 'Min', value : 2.3, xAxis: 11, yAxis: 3}
                    ]
                },
                markLine : {
                    data : [
                        {type : 'average', name : 'Average'}
                    ]
                }
            }
        ]
    };

    if (option && typeof option === "object") {
        rainChart.setOption(option, false);
    }


    /**
     * Resize chart on window resize
     * @return {void}
     */
    $(window).on('resize',function() {
        setTimeout(function(){
			 rainChart.resize();
		})
        
    });


});