<template>
    <div id="matchzootrainshow">
      <losschart v-bind:traindata="traindata"></losschart>
      <accuracychart v-bind:accuracydata="accuracydata"></accuracychart>
      <!--  <div>{{accuracydata}}</div>   -->
    </div>
</template>

<script>
  import LossChart from './LossChart'
  import AccuracyChart from './AccuracyChart'

  export default {
    name: 'MatchZooTrainShow',
    data () {
      return {

      }
    },
    components: {
      'losschart': LossChart,
      'accuracychart': AccuracyChart
    },
    props: {
      traindata: {
        type: Array,
        required: true
      },
      accuracydata: {
        type: Array,
        required: true
      }
    }
  }
</script>

<style>
</style>
