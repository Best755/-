 $(function () {
     Chart1();
     Chart2();
     Chart3();
     Chart4();
     function Chart1(){
        const chart = echarts.init(document.getElementById("chart_1"));
        let x_data=[];
        let s_data= [];
        const option = {
            color:['#B22222'],
            grid: {
                left: '1%',
                right: '0',
                bottom: '10%',
                containLabel: true
            },

            xAxis: {
                type: 'category',
                data: x_data,
                splitLine:{
                    show:false
                },
                axisLabel: {
                    show:true,
                    textStyle:{
                        color:'#c3dbff',
                        fontSize:12
                    }
                },
                axisLine:{
                    lineStyle:{
                        color:'#c3dbff'
                    }
                }

            },
            yAxis: {
                // splitLine:{
                //     show:false
                // },
                type: 'log',
                 axisLabel: {
                    show:true,
                    textStyle:{
                        color:'#c3dbff',
                        fontSize:8
                    }
                },
                 axisLine:{
                    lineStyle:{
                        color:'#c3dbff'
                    }
                }
            },
            series: [{
                data: s_data,
                type: 'bar',
                showBackground: true,
                backgroundStyle: {
                    color: 'rgba(220, 220, 220, 0.8)'
                }
            }]
        };
        $.get("http://121.41.228.236:8000/app/word_data_5/",function(data){
             console.log(data);
            $.each(data.data,function (k,v) {
                x_data.push(v.word_name);
                s_data.push(parseInt(v.sum_definite));

            });
            chart.hideLoading();
            chart.setOption({
                xAxis:{
                    data:x_data
                },
                series:[{
                    data:s_data
                }]
            });


        });
        chart.setOption(option);

    }
    function Chart2() {
      const chart1 = echarts.init(document.getElementById("chart_2"));
      let y_data=[];
      let s_data1=[];
      let s_data2=[];
      const option = {
          color:['#FF4500','#00FFFF'],
            // title: {
            //     text: '世界人口总量',
            //     subtext: '数据来自网络'

            // },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'shadow'
                }
            },
            legend: {
                data: ['确诊人数', '治愈人数'],
                top:"10%",
                textStyle:{
                    color:	'#87CEEB'
                }
            },

            // grid: {
            //     left: '3%',
            //     right: '4%',
            //     bottom: '3%',
            //     containLabel: true
            // },
            xAxis: {
                type: 'log',
          boundaryGap: false,
                splitLine:{
                    show:false
                },
                axisLabel: {
                    show:true,
                    textStyle:{
                        color:'#c3dbff',
                        fontSize:10
                    }
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }

            },
            yAxis: {
                type: 'category',

                data:y_data,
                axisLabel: {
                    show:true,
                    textStyle:{
                        color:'#c3dbff',
                        fontSize:10
                    }
                },
                   axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            series: [
                {
                    name: '确诊人数',
                    type: 'bar',
                    data: s_data1,
                },
                {
                    name: '治愈人数',
                    type: 'bar',
                    data: s_data2,
                }
            ]
        };
      $.get("http://121.41.228.236:8000/app/sum_china_data/",function (data) {
          console.log(data);
          $.each(data.data,function (k,v) {
              y_data.push(v.name);
              s_data1.push(parseInt(v.sum_definite));
              s_data2.push(parseInt(v.sum_cure));

          });
          chart1.setOption({
                yAxis:{
                    data:y_data
                },
                series:[
                    {data:s_data1},
                    { data:s_data2}]

            });

      });
      chart1.setOption(option);


  }
  function Chart3() {
       var chart_c083cadbb63e4a6bb99b63ce8585e826 = echarts.init(
            document.getElementById('c083cadbb63e4a6bb99b63ce8585e826'), 'white', {renderer: 'canvas'});
       var s_data=[];
        var option_c083cadbb63e4a6bb99b63ce8585e826 = {
    "animation": true,
    "animationThreshold": 2000,
    "animationDuration": 1000,
    "animationEasing": "cubicOut",
    "animationDelay": 0,
    "animationDurationUpdate": 300,
    "animationEasingUpdate": "cubicOut",
    "animationDelayUpdate": 0,
    "color": [
        "#c23531",
        "#2f4554",
        "#61a0a8",
        "#d48265",
        "#749f83",
        "#ca8622",
        "#bda29a",
        "#6e7074",
        "#546570",
        "#c4ccd3",
        "#f05b72",
        "#ef5b9c",
        "#f47920",
        "#905a3d",
        "#fab27b",
        "#2a5caa",
        "#444693",
        "#726930",
        "#b2d235",
        "#6d8346",
        "#ac6767",
        "#1d953f",
        "#6950a1",
        "#918597"
    ],
    "series": [
        {
            "type": "map",
            "name": "\u4e2d\u56fd\u75ab\u60c5\u5730\u56fe",
            "label": {
                "show": true,
                "position": "top",
                "margin": 8
            },
            "mapType": "china",
            "data": s_data,
            "roam": true,
            "zoom": 1,
            "showLegendSymbol": true,
            "emphasis": {}
        }
    ],
    "legend": [
        {
            "data": [
                "\u4e2d\u56fd\u75ab\u60c5\u5730\u56fe"
            ],
            "selected": {
                "\u4e2d\u56fd\u75ab\u60c5\u5730\u56fe": true
            },
            "show": true,
            "padding": 5,
            "itemGap": 10,
            "itemWidth": 25,
            "itemHeight": 14,
        }
    ],
    "tooltip": {
        "show": true,
        "trigger": "item",
        "triggerOn": "mousemove|click",
        "axisPointer": {
            "type": "line"
        },
        "textStyle": {
            "fontSize": 14
        },
        "borderWidth": 0
    },
    // "title": [
    //     {
    //         "text": "\u4e2d\u56fd\u75ab\u60c5\u5730\u56fe",
    //         "padding": 5,
    //         "itemGap": 10
    //     }
    // ],
    "visualMap": {
        "show": true,
        "type": "piecewise",
        "min": 0,
        "max": 70000,
        "inRange": {
            "color": [
                "#50a3ba",
                "#eac763",
                "#d94e5d"
            ]
        },
        "textStyle":{
            "color":"#FFFFFF",
        },
        "calculable": true,
        "inverse": false,
        "splitNumber": 5,
        "orient": "vertical",
        "showLabel": true,
        "itemWidth": 20,
        "itemHeight": 14,
        "borderWidth": 0,
        "pieces": [
            {
                "max": 100000,
                "min": 5001,
                "lable": ">5000",
                "color": "#8D0000"
            },
            {
                "max": 5000,
                "min": 1001,
                "label": "1000-5000",
                "color": "#B40404"
            },
            {
                "max": 1000,
                "min": 500,
                "label": "500-1000",
                "color": "#B22222"
            },
            {
                "max": 499,
                "min": 100,
                "label": "100-499",
                "color": "#DF0101"
            },
            {
                "max": 99,
                "min": 10,
                "label": "10-99",
                "color": "#F78181"
            },
            {
                "max": 9,
                "min": 0,
                "label": "0-9",
                "color": "#F5A9A9"
            },
        ]
    }
};
        $.get("http://121.41.228.236:8000/app/china_data/",function (data) {
            $.each(data.data,function (k,v) {
                var sdata={name:v.province_name,value:v.sum_definite};
                s_data.push(sdata);

            });
            chart_c083cadbb63e4a6bb99b63ce8585e826.hideLoading();
            chart_c083cadbb63e4a6bb99b63ce8585e826.setOption({
                series:{
                    data:s_data
                }
            });

        });
        chart_c083cadbb63e4a6bb99b63ce8585e826.setOption(option_c083cadbb63e4a6bb99b63ce8585e826);


  }

  function Chart4() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('chart_3'));
        var x_data=[];
        var s_data1=[];
        var s_data2=[];
        var s_data3=[];
        myChart.clear();
        option = {
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data:['治愈人数','确诊人数','死亡人数'],
                textStyle:{
                    color: '#fff'
                },
                top: '8%'
            },
            grid: {
                top: '40%',
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            color: ['#FF4949','#FFA74D','#40E0D0'],
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: x_data,
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                }
            },
            yAxis: {
                name: '人数',
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLine: {
                    lineStyle: {
                        color: '#fff'
                    }
                },
                  axisLabel: {
                    show:true,
                    textStyle:{
                        color:'#c3dbff',
                        fontSize:8
                    }
                },
            },
            series: [
                {
                    name:'治愈人数',
                    type:'line',
                    data:s_data1
                },
                {
                    name:'确诊人数',
                    type:'line',
                    data:s_data2
                },
                {
                    name:'死亡人数',
                    type:'line',
                    data:s_data3
                }
            ]
        };
              $.get("http://121.41.228.236:8000/app/index_ze/",function(data){
             // console.log(data);
            $.each(data.data,function (k,v) {
                x_data.push(v.date);
                s_data1.push(parseInt(v.sum_cure));
                s_data2.push(parseInt(v.sum_definite));
                s_data3.push(parseInt(v.sum_die));

            });
            myChart.hideLoading();
            myChart.setOption({
                xAxis:{
                    data:x_data
                },
                series:[
                    {
                    data:s_data1
                    },
                    {
                        data: s_data2
                    },
                    {
                        data:s_data3
                    }

                ]
            });


        });
        myChart.setOption(option);

    }
 });
