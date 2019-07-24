<template>
    <div id="accuracychart">
      <p v-show="false">{{accuracydata}}</p>
    </div>
</template>

<script>
  import * as d3 from 'd3'

  export default {
    name: 'TuneChart',
    data () {
      return {
        temp_data: [
          [{'x': 1, 'y': 0.04},{'x': 2, 'y': 0.66},{'x': 3, 'y': 0.57},{'x': 4, 'y': 0.54},{'x': 5, 'y': 0.48},{'x': 6, 'y': 0.23},{'x': 7, 'y': 0.28},{'x': 8, 'y': 0.05},{'x': 9, 'y': 0.44}],
          [{'x': 1, 'y': 0.13},{'x': 2, 'y': 0.55},{'x': 3, 'y': 0.8}]
        ],
        point_sum: 0
      }
    },
    props: {
      accuracydata: {
        type: Array,
        required: true
      },
      max_height: {
        type: Number,
        default: 2,
        required: true
      },
      min_height: {
        type: Number,
        default: 0,
        required: true
      },
      x_axis: {
        type: Number,
        default: 10,
        required: true
      },
      line_color: {
        type: Array,
        default: ['#FF9933', '#0099FF', '#FF3300'],
        required: true
      },
      line_num: {
        type: Number,
        default: 3,
        required: true
      }
    },
    mounted: function () {
      var winWidth = 0
      if (window.innerWidth) {
        winWidth = window.innerWidth
      } else if ((document.body) && (document.body.clientWidth)) {
        winWidth = document.body.clientWidth
      }
      if (document.documentElement && document.documentElement.clientWidth) {
        winWidth = document.documentElement.clientWidth
      }
      var width = winWidth * 0.25
      var height = 0.7 * width
      // console.log(width + 'd' + height)
      var margin = {top: height * 0.12, right: width * 0.12, bottom: height * 0.3, left: width * 0.12}
      var x = d3.scaleLinear().domain([1, this.x_axis]).range([0, width])
      // console.log(width + ' fenge ' + x(0.7))
      var y = d3.scaleLinear().domain([0, 1]).range([height, 0]) // height, 0是因为要让y坐标从下往上变大，竖直方向默认是从上向下变大
      // x轴设置
      var xAxis = d3.axisBottom(x)
              .ticks(5)// 调节刻度大小
              .tickSize(-height)// 如果指定了 size 则设置 内侧 和 外侧 竖直方向网线的长度，负值时表示是内侧
              .tickPadding(20) // 横坐标0,1,2不紧贴着坐标轴的x轴

      // y轴设置
      var yAxis = d3.axisLeft(y)
              .tickPadding(10)
              .tickSize(-width)

      var svg = d3.select('#accuracychart').append('svg')  // 把画布摆出来
              .attr('width', width + margin.left + margin.right)
              .attr('height', height + margin.top + margin.bottom)
              .append('g')
              .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

      svg.append('g') // 加上x轴
        .attr('class', 'x axis')
        .attr('transform', 'translate(0,' + height + ')')
        .call(xAxis)

      svg.append('g') // 加上y轴
        .attr('class', 'y axis')
        .call(yAxis)

      svg.append('g')
        .attr('class', 'y axis')
        .append('text')
        .attr('class', 'axis-label')
        .attr('transform', 'rotate(-90)') // 把字翻转一下，从3到m
        .attr('y', (-margin.left) + 14) // 是不是好像移动反了？没有，其实是先旋转过，物体是在自己的坐标系里面移动的，他自己的坐标系已经转过了
        .attr('x', -height / 2)
        .attr('font-size', 16)
        .text('Score')

      svg.append('g')
        .attr('class', 'x axis')
        .append('text')
        .attr('y', height + margin.top + 12)
        .attr('x', width / 2)
        .attr('font-size', 16)
        .text('Epoch')

      svg.append('clipPath')
        .attr('id', 'clip')
        .append('rect')
        .attr('width', width)
        .attr('height', height)

      var line = d3.line()
        .curve(d3.curveLinear)
        .x(function (d) { return x(d.x) })
        .y(function (d) { return y(d.y) })

      var linebase = svg.selectAll('.line')

      // var line_color = ['#FF9933', '#0099FF', '#FF3300']
      var myself = this
      linebase.data(this.accuracydata)
        .enter()
        .append('path')
        .attr('class', 'line')
        .attr('clip-path', 'url(#clip')
        .attr('stroke', function (d, i) {
          return myself.line_color[i % myself.line_num]
        })
        .style('stroke-width', '1.5px')
        .attr('d', line)

      var points = svg.selectAll('.dots')
        .data(this.accuracydata)
        .enter()
        .append('g')
        .attr('class', 'dots')
        .attr('clip-path', 'url(#clip)')

      points.selectAll('.dot')
        .data(function (d, index) {
          var a = []
          d.forEach(function (point, i) {
            a.push({'index': index, 'point': point})
          })
          return a
        })
        .enter()
        .append('circle')
        .attr('class', 'dot')
        .attr('r', 2)
        .attr('fill', function (d , i) {
          return myself.line_color[d.index % myself.line_num]
        })
        .attr('transform', function (d) {
          return 'translate(' + x(d.point.x) + ',' + y(d.point.y) + ')'
        })
    },
    updated: function () {
      var body = d3.select('#accuracychart')
      d3.select('body').selectAll('.d3-tip-accuracy').remove()
      d3.select('body').selectAll('#tip').remove()

      this.point_sum = this.accuracydata[0].length
      var winWidth = 0
      if (window.innerWidth) {
        winWidth = window.innerWidth
      } else if ((document.body) && (document.body.clientWidth)) {
        winWidth = document.body.clientWidth
      }
      if (document.documentElement && document.documentElement.clientWidth) {
        winWidth = document.documentElement.clientWidth
      }
      var width = winWidth * 0.25
      var height = 0.7 * width
      // console.log(width + 'd' + height)
      var margin = {top: height * 0.12, right: width * 0.12, bottom: height * 0.3, left: width * 0.12}
      var x = d3.scaleLinear().domain([1, this.x_axis]).range([0, width])
      // console.log(width + ' fenge ' + x(0.7))
      var y = d3.scaleLinear().domain([this.min_height, this.max_height]).range([height, 0]) // height, 0是因为要让y坐标从下往上变大，竖直方向默认是从上向下变大
      // x轴设置
      var xAxis = d3.axisBottom(x)
              .ticks(10)// 调节刻度大小
              .tickSize(-height)// 如果指定了 size 则设置 内侧 和 外侧 竖直方向网线的长度，负值时表示是内侧
              .tickPadding(20) // 横坐标0,1,2不紧贴着坐标轴的x轴

      // y轴设置
      var yAxis = d3.axisLeft(y)
              .tickPadding(10)
              .tickSize(-width)

      d3.select('svg').remove()

      var svg = d3.select('#accuracychart').append('svg')  // 把画布摆出来
              .attr('width', width + margin.left + margin.right)
              .attr('height', height + margin.top + margin.bottom)
              .append('g')
              .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')')

      svg.append('g') // 加上x轴
        .attr('class', 'x axis')
        .attr('transform', 'translate(0,' + height + ')')
        .call(xAxis)

      svg.append('g') // 加上y轴
        .attr('class', 'y axis')
        .call(yAxis)

      svg.append('g')
        .attr('class', 'y axis')
        .append('text')
        .attr('class', 'axis-label')
        .attr('transform', 'rotate(-90)') // 把字翻转一下，从3到m
        .attr('y', (-margin.left) + 14) // 是不是好像移动反了？没有，其实是先旋转过，物体是在自己的坐标系里面移动的，他自己的坐标系已经转过了
        .attr('x', -height / 2)
        .attr('font-size', 16)
        .text('Score')

      svg.append('g')
        .attr('class', 'x axis')
        .append('text')
        .attr('y', height + margin.top + 12)
        .attr('x', width / 2)
        .attr('font-size', 16)
        .text('Epoch')

      svg.append('clipPath')
        .attr('id', 'clip')
        .append('rect')
        .attr('width', width)
        .attr('height', height)

      var line = d3.line()
        .curve(d3.curveLinear)
        .x(function (d) { return x(d.x) })
        .y(function (d) { return y(d.y) })

      var linebase = svg.selectAll('.line')

      // var line_color = ['#FF9933', '#0099FF', '#FF3300']
      var myself = this
      linebase.data(this.accuracydata)
        .enter()
        .append('path')
        .attr('class', 'line')
        .attr('clip-path', 'url(#clip')
        .attr('stroke', function (d, i) {
          // console.log('调试tune的图表：', this.line_color, this.line_num)
          return myself.line_color[i % myself.line_num]
        })
        .style('stroke-width', '2px')
        .attr('d', line)

      var points = svg.selectAll('.dots')
        .data(this.accuracydata)
        .enter()
        .append('g')
        .attr('class', 'dots')
        .attr('clip-path', 'url(#clip)')

      points.selectAll('.dot')
        .data(function (d, index) {
          var a = []
          d.forEach(function (point, i) {
            a.push({'index': index, 'point': point})
          })
          return a
        })
        .enter()
        .append('circle')
        .attr('class', 'dot')
        .attr('r', 2)
        .attr('fill', function (d, i) {
          return myself.line_color[d.index % myself.line_num]
        })
        .attr('transform', function (d) {
          return 'translate(' + x(d.point.x) + ',' + y(d.point.y) + ')'
        })
    }
  }
</script>

<style>

    .grid .tick {
        stroke: lightgrey;
        opacity: 0.7;
        shape-rendering: crispEdges;
    }

    .grid path {
        stroke-width: 0;
    }

    .axis path {
        fill: none;
        stroke: #bbb;
        shape-rendering: crispEdges;
    }

    .axis text {
        fill: #555;
    }

    .axis line {
        stroke: #e7e7e7;
        shape-rendering: crispEdges;
    }

    .axis .axis-label {
        font-size: 14px;
    }

    .area {
        fill: none;
        stroke-width: 1px;
    }

    .line {
        fill: none;
        stroke-width: 1px;
    }

    .dot {

        stroke: transparent;
        stroke-width: 10px;
        cursor: pointer;
        /*pointer-events: all;*/
    }

    .dot:hover {
        stroke: rgba(68, 127, 255, 0.3);
    }

    .mouseout{
      width: 0;
      height: 0;
    }

    .d3-tip-accuracy{    /*提示框的样式*/
			display: flex;
			flex-direction: column;
			position: absolute;   /*不可缺少*/
			line-height: 1;
			font-weight: bold;
      font-size:12px;
			padding:12px;
			background-color: antiquewhite;
			color: #fff;
			border-radius: 2px;
		}

		.d3-tip-accuracy:before{
			box-sizing: border-box;
			display: inline;
			font-size: 20px;
			width:100%;
			line-height: 1;
			color:  antiquewhite;
			content:'\25E3';
			position: absolute; 	/*不可缺少*/
			text-align: left;
			top: -10px;
			left: -1px;
		}

		.d3-tip-accuracy.n:before {
      margin: -1px 0 0 0;
      top: 100%;
      left: 0;
    }
</style>
