<template>
  <div id="twovecs">
    <el-row :gutter="20">
      <el-col :span="12">
        <el-tag type="info">query representation</el-tag>
        <div style="height:15px"></div>
        <table v-show="cansee">
          <tr v-for="i in n" v-bind:key="i">
            <el-tooltip class="item" effect="dark" v-for="j in k" v-bind:key="j" placement="top-start">
              <div slot="content">
                dim:&nbsp{{ (j - 1) * n + i}} <br>
                <br>
                value1:&nbsp{{val_list1[(i - 1) * k + j - 1]}} <br>
                value2:&nbsp{{val_list2[(i - 1) * k + j - 1]}}
              </div>
              <td>
                <div class="normal-td1" v-on:mousemove="getChecked1"></div>
              </td>
            </el-tooltip>
          </tr>
        </table>
      </el-col>
      <el-col :span="12">
        <el-tag type="info">document representation</el-tag>
        <div style="height:15px"></div>
        <table v-show="cansee">
          <tr v-for="i in n" v-bind:key="i">
            <el-tooltip class="item" effect="dark" v-for="j in k" v-bind:key="j" placement="top-start">
              <div slot="content">
                dim:&nbsp{{ (j - 1) * n + i}} <br>
                <br>
                value1:&nbsp{{val_list1[(i - 1) * k + j - 1]}} <br>
                value2:&nbsp{{val_list2[(i - 1) * k + j - 1]}}
              </div>
              <td>
                <div class="normal-td2" v-on:mousemove="getChecked2"></div>
              </td>
            </el-tooltip>
          </tr>
        </table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  export default {
    name: 'TwoVecs',
    methods: {
      startHacking () {
        this.$notify({
          title: 'It works!',
          type: 'success',
          message: 'We\'ve laid the ground work for you. It\'s time for you to build something epic!',
          duration: 5000
        })
      },
      getChecked1: function (event) {
        var td_list1 = document.getElementsByClassName('normal-td1')
        var x = event.target.tdx
        var y = event.target.tdy
        for (var i = 0; i < this.n; i++) {
          for (var j = 0; j < this.k; j++) {
            if (i === x) {
              td_list1[i * this.k + j].style.boxShadow = 'inset 0px 15px 15px -15px #888, inset 0px -15px 15px -15px #888'
            }
            else if (j === y) {
              td_list1[i * this.k + j].style.boxShadow = 'inset 15px 0px 15px -15px #888, inset -15px 0px 15px -15px #888'
            }
            else {
              td_list1[i * this.k + j].style.boxShadow = 'none'
            }
          }
        }
        td_list1[x * this.k + y].style.boxShadow = 'inset 0px 0px 2px #888'
      },
      getChecked2: function () {
        var td_list2 = document.getElementsByClassName('normal-td2')
        var x = event.target.tdx
        var y = event.target.tdy
        for (var i = 0; i < this.n; i++) {
          for (var j = 0; j < this.k; j++) {
            if (i === x) {
              td_list2[i * this.k + j].style.boxShadow = 'inset 0px 15px 15px -15px #888, inset 0px -15px 15px -15px #888'
            }
            else if (j === y) {
              td_list2[i * this.k + j].style.boxShadow = 'inset 15px 0px 15px -15px #888, inset -15px 0px 15px -15px #888'
            }
            else {
              td_list2[i * this.k + j].style.boxShadow = 'none'
            }
          }
        }
        td_list2[x * this.k + y].style.boxShadow = 'inset 0px 0px 2px #888'
      },
      getToolTipText: function (x, y) {
        var textString = `dim: ${x*this.k + y} ${'\n'} vector1: ${this.val_list1[x * this.k + y]} ${'\n'} vector2:${this.val_list2[x * this.k + y]}`
        return textString
      }
    },
    data () {
      return {
        n: 16,
        k: 8,
        val_list1: [],
        val_list2: [],
        row_val: [],
        col_val: [],
        name_val: [],
        cansee: false
      }
    },
    props: {
      tabledata: {
        type: Object,
        required: false
      }
    },
    mounted: function () {
      for (var i = 0; i < this.n; i++) {
        for (var j = 0; j < this.k; j++) {
          this.val_list1.push(Math.random().toFixed(6))
          this.val_list2.push(Math.random().toFixed(6))
        }
      }
      for (var i = 0; i <= this.n; i++) {
        this.row_val.push('row' + i)
      }
      for (var j = 0; j <= this.k; j++) {
        this.col_val.push('col' + j)
        this.name_val.push(((j - 1) * this.n + 1) + ':' + j * this.n)
      }

      function getColor (value) {
        //var color_list = ['#f2f9fe', '#d2eafd', '#a6d4fa', '#79bff8', '#4daaf6', '#0c87eb', '#0b78d1', '#0a69b7', '#085a9d', '#074b83']
        var color_list =
          ['#2980B9', '#2F88BF', '#3590C5', '#3B98CB', '#41A0D1', '#47A8D7', '#4DB0DD', '#53B8E3',
            '#59C0E9', '#5FC8EF', '#6DD5FA', '#71D6FA', '#75D7FA', '#79D8FA', '#7DD9FA', '#81DAFA',
            '#85DBFA', '#89DCFA', '#8DDDFA', '#91DEFA', '#95DFFA', '#99E0FA', '#9DE1FA', '#A1E2FA',
            '#A5E3FA', '#A9E4FA', '#ADE5FA', '#B1E6FA', '#B5E7FA', '#B9E8FA', '#BDE9FA', '#C1EAFA',
            '#C5EBFA', '#C9ECFA', '#CDEDFA', '#D1EEFA', '#D5EFFA', '#D9F0FA', '#DDF1FA', '#E1F2FA'
          ]
        for (var i = 0; i < color_list.length; i++) {
          if (value >= 1 - (i + 1) * 0.025) {
            return color_list[i]
          }
        }
      }

      var td_list1 = document.getElementsByClassName('normal-td1')
      for (var i = 0; i < this.n; i++) {
        for (var j = 0; j < this.k; j++) {
          td_list1[i * this.k + j].tdx = i
          td_list1[i * this.k + j].tdy = j
          td_list1[i * this.k + j].num_value = this.val_list1[i * this.k + j]
          td_list1[i * this.k + j].origin_color = getColor(td_list1[i * this.k + j].num_value)
          td_list1[i * this.k + j].style.backgroundColor = td_list1[i * this.k + j].origin_color
        }
      }

      var td_list2 = document.getElementsByClassName('normal-td2')
      for (let i = 0; i < this.n; i++) {
        for (let j = 0; j < this.k; j++) {
          td_list2[i * this.k + j].tdx = i
          td_list2[i * this.k + j].tdy = j
          td_list2[i * this.k + j].num_value = this.val_list2[i * this.k + j]
          td_list2[i * this.k + j].origin_color = getColor(td_list2[i * this.k + j].num_value)
          td_list2[i * this.k + j].style.backgroundColor = td_list2[i * this.k + j].origin_color
        }
      }

      this.cansee = true
    }
  }
</script>

<style scoped>
  .wmdowntoup {
    /*
    writing-mode: vertical-lr;
    -webkit-writing-mode: vertical-lr;
    -ms-writing-mode: vertical-lr;
    */
    transform: rotate(-90deg);
    -ms-transform: rotate(-90deg); /* Internet Explorer */
    -moz-transform: rotate(-90deg); /* Firefox */
    -webkit-transform: rotate(-90deg); /* Safari 和 Chrome */
    -o-transform: rotate(-90deg); /* Opera */
    line-height: 30px;
    width: 30px;
    height: 30px;
  }

  .normal-td1 {
    width: 25px;
    height: 25px;
    z-index: 999;
    /*box-shadow: 1px 1px 1px #888888;*/
  }

  .normal-td2 {
    width: 25px;
    height: 25px;
    z-index: 999;
    /*box-shadow: 1px 1px 1px #888888;*/
  }

  #twovecs {
    font-family: Helvetica, sans-serif;
    text-align: center;
  }

  table {
    margin: 0 auto;
    border-collapse: collapse;
    /*border:1px solid black;*/
  }

  /*
  tr{
    border:1px solid black;
  }*/

  td {
    width: 25px;
    height: 25px;
    /*border:1px solid black;*/
  }

  #test-table0 {
    background-color: red;
  }

  #test-table1 {
    background-color: blue;
  }
</style>
