<template>
  <div id="matchzoopredictshow">
    <el-input v-model="input" :disabled="true">
      <template slot="prepend">
        Rate
      </template>
    </el-input>
    <div style="padding:20px 0;"></div>
    <matchzootab v-bind:tabledata="tabledata"></matchzootab>
  </div>
</template>

<script>
  import MatchZooTab from './MatchZooTab'
  export default {
    name: 'MatchZooPredictShow',
    components: {
      'matchzootab': MatchZooTab
    },
    data () {
      return {
        input: ''
      }
    },
    props: {
      tabledata: {
        type: Object,
        required: true
      }
    },
    mounted: function () {
      console.log(this.tabledata)
      this.input = this.tabledata.rate
    }
  }
</script>

<style scoped>

</style>
