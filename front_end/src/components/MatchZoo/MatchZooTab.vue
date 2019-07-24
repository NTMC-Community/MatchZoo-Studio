<template>
  <div id="matchzootab">
    <table v-show="cansee">
      <tr>
        <td class="top-left-td"></td>
        <td v-for="i in k" class="top-td" v-bind:key="i">
          <div class="wmdowntoup">{{ col_val[i] }}</div>
        </td>
      </tr>
      <tr v-for="i in n" v-bind:key="i">
        <td class="left-td">{{ row_val[i] }}</td>
        <el-tooltip class="item" effect="dark"  v-for="j in k"  v-bind:key="j" placement="top-start">
          <div slot="content">
            {{ val_list[(i-1)*k+j-1] }} <br>
            <br>
            Row:&emsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{row_val[i - 1]}} <br>
            Column:&emsp;{{col_val[j - 1]}}
          </div>
          <td>
            <div class="normal-td" v-on:mousemove="getChecked"></div>
          </td>
        </el-tooltip>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  methods: {
    startHacking () {
      this.$notify({
        title: 'It works!',
        type: 'success',
        message: 'We\'ve laid the ground work for you. It\'s time for you to build something epic!',
        duration: 5000
      })
    },
    getChecked: function (event) {
      var td_list = document.getElementsByClassName('normal-td')
      var x = event.target.tdx
      var y = event.target.tdy
      for (var i = 0; i < this.n; i++) {
        for (var j = 0; j < this.k; j++) {
          if (i === x) {
            // td_list[i * this.k + j].bgColor = '#E4E7ED'
            td_list[i * this.k + j].style.boxShadow = 'inset 0px 15px 15px -15px #888, inset 0px -15px 15px -15px #888'
          }
          else if ( j === y) {
            td_list[i * this.k + j].style.boxShadow = 'inset 15px 0px 15px -15px #888, inset -15px 0px 15px -15px #888'
          }
          else {
            // td_list[i * this.k + j].bgColor = td_list[i * this.k + j].origin_color
            td_list[i * this.k + j].style.boxShadow = 'none'
          }
        }
      }
      td_list[x * this.k + y].style.boxShadow = 'inset 0px 0px 2px #888'
    },
    getToolTipText: function (x, y) {
      var textString = `${this.val_list[x * this.k + y]} ${'\n'} row:${this.row_val[x]} ${'\n'} col:${this.col_val[y]}`
      return textString
    }
  },
  data () {
    return {
      n: 50,
      k: 15,
      val_list: [],
      row_val: [],
      col_val: [],
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
    /*
    this.n = this.tabledata.n
    this.k = this.tabledata.k
    this.val_list = this.tabledata.val_list
    this.row_val = this.tabledata.row_val
    this.col_val = this.tabledata.col_val
    */
    for (var i = 0 ; i < this.n ; i++) {
      for (var j = 0 ; j < this.k ; j++) {
        this.val_list.push(Math.random())
      }
    }
    for (var i = 0 ; i <= this.n ; i++) {
      this.row_val.push('row' + i)
    }
    for (var j = 0 ; j <= this.k ; j++) {
      this.col_val.push('col' + j)
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

    var td_list = document.getElementsByClassName('normal-td')
    console.log(td_list.length)
    for (var i = 0; i < this.n; i++) {
      for (var j = 0; j < this.k; j++) {
        td_list[i * this.k + j].tdx = i
        td_list[i * this.k + j].tdy = j
        td_list[i * this.k + j].num_value = this.val_list[i * this.k + j]
        td_list[i * this.k + j].origin_color = getColor(td_list[i * this.k + j].num_value)
        td_list[i * this.k + j].style.backgroundColor = td_list[i * this.k + j].origin_color
      }
    }
    console.log(td_list[55])
    this.cansee = true
  }
}
</script>

<style>
.wmdowntoup{
  /*
  writing-mode: vertical-lr;
  -webkit-writing-mode: vertical-lr;
  -ms-writing-mode: vertical-lr;
  */
  transform:rotate(-90deg);
  -ms-transform:rotate(-90deg); /* Internet Explorer */
  -moz-transform:rotate(-90deg); /* Firefox */
  -webkit-transform:rotate(-90deg); /* Safari 和 Chrome */
  -o-transform:rotate(-90deg); /* Opera */
  line-height: 30px;
  width: 30px;
  height: 30px;
}

.top-left-td{
  border-width:0;
}

.top-td{
  border: 1px solid white;
  height: 60px;
  width: 30px;
  background-color: #E4E7ED;
}

.left-td{
  border: 1px solid white;
  width: 60px;
  height: 30px;
  background-color: #E4E7ED;
}

.normal-td{
  width: 30px;
  height: 30px;
  z-index: 999;
  /*box-shadow: 1px 1px 1px #888888;*/
}

#matchzootab {
  font-family: Helvetica, sans-serif;
  text-align: center;
}

table{
  margin:0 auto;
  border-collapse:collapse;
  /*border:1px solid black;*/
}
/*
tr{
  border:1px solid black;
}*/

td{
  width: 30px;
  height: 30px;
  /*border:1px solid black;*/
}

#test-table0{
  background-color: red;
}
#test-table1{
  background-color: blue;
}
</style>
