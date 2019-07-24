<template>
    <div id="losschart">
      <p v-show="false">{{traindata}}</p>
    </div>
</template>

<script>
  import * as d3 from 'd3'

  export default {
    name: 'LossChart',
    data () {
      return {
        data: [[{'x': 0, 'y': 1}, {'x': 1, 'y': 0.86}, {'x': 2, 'y': 0.77},
                {'x': 3, 'y': 0.65}, {'x': 4, 'y': 0.62}, {'x': 5, 'y': 0.57},
                {'x': 6, 'y': 0.55}, {'x': 7, 'y': 0.49}, {'x': 8, 'y': 0.47},
                {'x': 9, 'y': 0.44}, {'x': 10, 'y': 0.37}, {'x': 11, 'y': 0.35},
                {'x': 12, 'y': 0.30}, {'x': 13, 'y': 0.29}, {'x': 14, 'y': 0.29}]
        ],
        point_sum: 0
      }
    },
    props: {
      traindata: {
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
      var y = d3.scaleLinear().domain([0, 2]).range([height, 0]) // height, 0是因为要让y坐标从下往上变大，竖直方向默认是从上向下变大
      // x轴设置
      var xAxis = d3.axisBottom(x)
              .ticks(10)// 调节刻度大小
              .tickSize(-height)// 如果指定了 size 则设置 内侧 和 外侧 竖直方向网线的长度，负值时表示是内侧
              .tickPadding(20) // 横坐标0,1,2不紧贴着坐标轴的x轴

      // y轴设置
      var yAxis = d3.axisLeft(y)
              .ticks(10)
              .tickPadding(10)
              .tickSize(-width)

      // 缩放拖拽
      var zoom = d3.zoom()
              .scaleExtent([1, 1])// 可缩放的范围
              .translateExtent([[0, 0], [100000, 100000]])
              .on('zoom', zoomed)

      var svg = d3.select('#losschart').append('svg')  // 把画布摆出来
              .call(zoom)
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
        .text('Loss')

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

      var area = d3.area()  // v4版本语法是d3.line, 这一段称为数据路径生成器
        .curve(d3.curveLinear)
        .x(function (d) { return x(d.x) })
        .y1(function (d) { return y(d.y) })
        .y0(function (d) { return y(0) })

      var line = d3.line()
        .curve(d3.curveLinear)
        .x(function (d) { return x(d.x) })
        .y(function (d) { return y(d.y) })

      var linebase = svg.selectAll('.line')

       // 这里select是选不到的，就靠后面一手enter
      linebase.data(this.traindata)
        .enter()
        .append('path')
        .attr('class', 'area')
        .attr('clip-path', 'url(#clip)')
        .style('fill', 'rgba(255,165,0,0.3)')
        .attr('d', area)

      linebase.data(this.traindata)
        .enter()
        .append('path')
        .attr('class', 'line')
        .attr('clip-path', 'url(#clip')
        .attr('stroke', 'red')
        .attr('d', line)

      var div = d3.select('#losschart').append('div') // 添加tip提示框
                .attr('class', 'd3-tip')
                .style('opacity', 0)

      var points = svg.selectAll('.dots')
        .data(this.traindata)
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
        .attr('fill', 'orange')
        .attr('transform', function (d) {
          return 'translate(' + x(d.point.x) + ',' + y(d.point.y) + ')'
        })
        .on('mouseover', function (d) {    // 添加鼠标监听事件
          div.transition()
            .duration(200)
            .style('opacity', 0.9)
          div.html("<span id='tip' style='color: red'>epoch:" + (d.point.x) + '<br>loss:' + (d.point.y) + '</span>') // 提示框的内容
            // 20是因为el-card有固定值为20px的padding，14是因为往里面写字（Loss，Epoch）加大了padding的宽度，y减18px是因为我不想tooltip垂直方向贴着圈
          .style('left', event.target.getBoundingClientRect().left + 'px').style('top', event.target.getBoundingClientRect().top - 70 + 'px')
        })
        .on('mouseout', function (d) {
          div.transition()
            .duration(200)
            .style('opacity', 0)
        })

      function zoomed () {
        let t = d3.event.transform.rescaleX(x)
        svg.select('.x.axis').call(xAxis.scale(t))
        svg.select('.y.axis').call(yAxis)
        area.x(function (d) { return t(d.x) })
        line.x(function (d) { return t(d.x) })
        svg.selectAll('path.area').attr('d', area)
        svg.selectAll('path.line').attr('d', line)
        points.selectAll('circle').attr('transform', function (d) {
          return 'translate(' + t(d.point.x) + ',' + y(d.point.y) + ')'
        })
        .on('mouseover', function (d) {    // 添加鼠标监听事件
          div.transition()
            .duration(200)
            .style('opacity', 0.9)
          div.html("<span id='tip' style='color: red'>epoch:" + (d.point.x) + '<br>loss:' + (d.point.y) + '</span>') // 提示框的内容
          .style('left', event.target.getBoundingClientRect().left + 'px').style('top', event.target.getBoundingClientRect().top - 70 + 'px')
        })
      }
    },
    updated: function () {
      var body = d3.select('#losschart')
      d3.select('body').selectAll('.d3-tip').remove()
      d3.select('body').selectAll('#tip').remove()

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

      // 缩放拖拽
      var zoom = d3.zoom()
              .scaleExtent([1, 1])// 可缩放的范围
              .translateExtent([[0, 0], [100000, 100000]])
              .on('zoom', zoomed)

      d3.select('svg').remove()

      var svg = d3.select('#losschart').append('svg')  // 把画布摆出来
              .call(zoom)
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
        .text('Loss')

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

      var area = d3.area()  // v4版本语法是d3.line, 这一段称为数据路径生成器
        .curve(d3.curveLinear)
        .x(function (d) { return x(d.x) })
        .y1(function (d) { return y(d.y) })
        .y0(function (d) { return y(0) })

      var line = d3.line()
        .curve(d3.curveLinear)
        .x(function (d) { return x(d.x) })
        .y(function (d) { return y(d.y) })

      var linebase = svg.selectAll('.line')

       // 这里select是选不到的，就靠后面一手enter
      linebase.data(this.traindata)
        .enter()
        .append('path')
        .attr('class', 'area')
        .attr('clip-path', 'url(#clip)')
        .style('fill', 'rgba(255,165,0,0.3)')
        .attr('d', area)

      linebase.data(this.traindata)
        .enter()
        .append('path')
        .attr('class', 'line')
        .attr('clip-path', 'url(#clip')
        .attr('stroke', 'red')
        .attr('d', line)

      var div = d3.selectAll('body').append('div') // 添加tip提示框
                .attr('class', 'd3-tip')
                .style('opacity', 0)

      var points = svg.selectAll('.dots')
        .data(this.traindata)
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
        .attr('fill', 'orange')
        .attr('transform', function (d) {
          return 'translate(' + x(d.point.x) + ',' + y(d.point.y) + ')'
        })
        .on('mouseover', function (d) {    // 添加鼠标监听事件
          console.log(event.target)
          div.transition()
            .duration(200)
            .style('opacity', 0.9)
          div.html("<span id='tip' style='color: red'>epoch:" + (d.point.x) + '<br>loss:' + (d.point.y) + '</span>') // 提示框的内容
          // getBoundingClientRect()是距离浏览器工具栏的高度，而top的高度是相对于div#losschart的高度
          // 60:导航栏高度 20:下方整个页面padding titleHeight:"DSSM"高度 40:标签高度 10:标签下面的缝 20:div#losschart的padding 100:离开点的高度
          .style('left', event.target.getBoundingClientRect().left + 'px').style('top', event.target.getBoundingClientRect().top - 70 + 'px')
        })
        .on('mouseout', function (d) {
          div.transition()
            .duration(0)
            .style('opacity', 0)
        })

      function zoomed () {
        let t = d3.event.transform.rescaleX(x)
        svg.select('.x.axis').call(xAxis.scale(t))
        svg.select('.y.axis').call(yAxis)
        area.x(function (d) { return t(d.x) })
        line.x(function (d) { return t(d.x) })
        svg.selectAll('path.area').attr('d', area)
        svg.selectAll('path.line').attr('d', line)
        points.selectAll('circle').attr('transform', function (d) {
          return 'translate(' + t(d.point.x) + ',' + y(d.point.y) + ')'
        })
        .on('mouseover', function (d) {    // 添加鼠标监听事件
          div.transition()
            .duration(200)
            .style('opacity', 0.9)
          div.html("<span id='tip' style='color: red'>epoch:" + (d.point.x) + '<br>loss:' + (d.point.y) + '</span>') // 提示框的内容
          .style('left', event.target.getBoundingClientRect().left + 'px').style('top', event.target.getBoundingClientRect().top - 70 + 'px')
        })
      }
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

    .d3-tip{    /*提示框的样式*/
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

		.d3-tip:after{
			box-sizing: border-box;
			display: inline;
			font-size: 20px;
			width:100%;
			line-height: 1;
			color:  antiquewhite;
			content:'\25E4';
			position: absolute; 	/*不可缺少*/
			text-align: left;
			top: 40px;
			left: -1px;
		}

		.d3-tip.n:after {
      margin: -1px 0 0 0;
      top: 100%;
      left: 0;
    }
</style>
