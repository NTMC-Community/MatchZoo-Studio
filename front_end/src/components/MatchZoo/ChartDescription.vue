<template>
    <div id="chart-description">
    </div>
</template>

<script>
  import * as d3 from 'd3'
  export default {
    name: 'ChartDescription',
    mounted: function () {
      var svg = d3.select('#chart-description')
        .append('svg')
        .attr('height', '150px')
        .attr('width', '80%')

      // 图例一
      svg.append('rect')
        .attr('fill', '#FF9933')
        .attr('height', '15px')
        .attr('width', '25px')
        .attr('stroke', 'gray')
        .attr('stroke-width', '2px')
        .attr('transform', 'translate(0, 0)')

      svg.append('text')
        .attr('class', 'label-text')
        .attr('y', 14)
        .attr('x', 50)
        .attr('font-size', 16)
        .text('NDCG@3')

      // 图例二
      svg.append('rect')
        .attr('fill', '#0099FF')
        .attr('height', '15px')
        .attr('width', '25px')
        .attr('stroke', 'gray')
        .attr('stroke-width', '1.5px')
        .attr('transform', 'translate(0, 30)')

      svg.append('text')
        .attr('class', 'label-text')
        .attr('y', 44)
        .attr('x', 50)
        .attr('font-size', 16)
        .text('NDCG@5')

      // 图例三
      svg.append('rect')
        .attr('fill', '#FF3300')
        .attr('height', '15px')
        .attr('width', '25px')
        .attr('stroke', 'gray')
        .attr('stroke-width', '1.5px')
        .attr('transform', 'translate(0, 60)')

      svg.append('text')
        .attr('class', 'label-text')
        .attr('y', 74)
        .attr('x', 50)
        .attr('font-size', 16)
        .text('MAP')
    }
  }
</script>

<style scoped>
  .label-text {
    font-size: 14px;
    color: #909399;
  }
</style>
