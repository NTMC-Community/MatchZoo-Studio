<template>
  <div id="chart-description">
    <svg height="150px" width="80%">

      <rect v-if="models[0].chosen" fill="#CC0000" height="15px" width="25px" stroke="gray" stroke-width="2px"
            :transform="models[0].translate"></rect>
      <text v-if="models[0].chosen" class="label-text" :y="models[0].y" :x="models[0].x" style="font-size: 16px;">DRMM</text>

      <rect v-if="models[1].chosen" fill="#FF9900" height="15px" width="25px" stroke="gray" stroke-width="1.5px"
            :transform="models[1].translate"></rect>
      <text v-if="models[1].chosen" class="label-text" :y="models[1].y" :x="models[1].x" style="font-size: 16px;">MatchPyramid</text>

      <rect v-if="models[2].chosen" fill="#663300" height="15px" width="25px" stroke="gray" stroke-width="1.5px"
            :transform="models[2].translate"></rect>
      <text v-if="models[2].chosen" class="label-text" :y="models[2].y" :x="models[2].x" style="font-size: 16px;">ARC-I</text>

      <rect v-if="models[3].chosen" fill="#FFFF33" height="15px" width="25px" stroke="gray" stroke-width="1.5px"
            :transform="models[3].translate"></rect>
      <text v-if="models[3].chosen" class="label-text" :y="models[3].y" :x="models[3].x" style="font-size: 16px;">DSSM</text>

      <rect v-if="models[4].chosen" fill="#9999FF" height="15px" width="25px" stroke="gray" stroke-width="1.5px"
            :transform="models[4].translate"></rect>
      <text v-if="models[4].chosen" class="label-text" :y="models[4].y" :x="models[4].x" style="font-size: 16px;">CDSSM</text>

      <rect v-if="models[5].chosen" fill="#6600FF" height="15px" width="25px" stroke="gray" stroke-width="2px"
            :transform="models[5].translate"></rect>
      <text v-if="models[5].chosen" class="label-text" :y="models[5].y" :x="models[5].x" style="font-size: 16px;">ARC-II</text>

      <rect v-if="models[6].chosen" fill="#009900" height="15px" width="25px" stroke="gray" stroke-width="2px"
            :transform="models[6].translate"></rect>
      <text v-if="models[6].chosen" class="label-text" :y="models[6].y" :x="models[6].x" style="font-size: 16px;">MV-LSTM</text>

      <rect v-if="models[7].chosen" fill="#006600" height="15px" width="25px" stroke="gray" stroke-width="2px"
            :transform="models[7].translate"></rect>
      <text v-if="models[7].chosen" class="label-text" :y="models[7].y" :x="models[7].x" style="font-size: 16px;">DUET</text>

      <rect v-if="models[8].chosen" fill="#0099FF" height="15px" width="25px" stroke="gray" stroke-width="2px"
            :transform="models[8].translate"></rect>
      <text v-if="models[8].chosen" class="label-text" :y="models[8].y" :x="models[8].x" style="font-size: 16px;">K-NRM</text>

      <rect v-if="models[9].chosen" fill="#0033FF" height="15px" width="25px" stroke="gray" stroke-width="2px"
            :transform="models[9].translate"></rect>
      <text v-if="models[9].chosen" class="label-text" :y="models[9].y" :x="models[9].x" style="font-size: 16px;">CONV-KNRM</text>
    </svg>
    <p v-show="false">
      {{selected_models}}
    </p>
  </div>
</template>

<script>
  export default {
    name: 'TuneChartDescription',
    data: function () {
      return {
        models: [
          {
            name: 'DRMM',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          },
          {
            name: 'MatchPyramid',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          },
          {
            name: 'ARC-I',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          },
          {
            name: 'DSSM',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          },
          {
            name: 'CDSSM',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          },
          {
            name: 'ARC-II',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          },
          {
            name: 'MV-LSTM',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          },
          {
            name: 'DUET',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          },
          {
            name: 'K-NRM',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          },
          {
            name: 'CONV-KNRM',
            chosen: false,
            x: 0,
            y: 0,
            translate: 'translate(0,0)'
          }
        ]
      }
    },
    props: {
      selected_models: {
        type: Object,
        required: true
      }
    },
    updated: function () {
      var idx = 0
      var chosen_cnt = 0
      for (var md in this.selected_models) {
        let cur = this.selected_models[md]
        this.models[idx].chosen = cur.chosen
        if (this.models[idx].chosen === true) {
          chosen_cnt++
          if (chosen_cnt <= 5) {
            this.models[idx].x = 50
            this.models[idx].y = 14 + 30 * (chosen_cnt - 1)
            this.models[idx].translate = 'translate(0, ' + 30 * (chosen_cnt - 1) + ')'
          } else {
            this.models[idx].x = 250
            this.models[idx].y = 14 + 30 * (chosen_cnt - 6)
            this.models[idx].translate = 'translate(200, ' + 30 * (chosen_cnt - 6) + ')'
          }
        }
        idx++
      }
    }
  }
</script>

<style scoped>
  .label-text {
    font-size: 14px;
    color: #909399;
  }
</style>
