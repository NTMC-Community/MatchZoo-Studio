<template>
  <div id="new-model">
    <el-row :gutter="20">
      <el-col :span="15">
        <el-card>
          <el-scrollbar style="height:100%;">
            <iframe :src="jupyter_url1" frameborder="0" class="embedding"></iframe>
          </el-scrollbar>
        </el-card>
      </el-col>
      <el-col :span="9">
        <el-scrollbar style="height:100%;">
          <el-card>
            <el-scrollbar style="height:100%;">
              <iframe :src="jupyter_url2" frameborder="0" class="embedding"></iframe>
            </el-scrollbar>
          </el-card>
        </el-scrollbar>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'NewModel',
    components: {
    },
    mounted: function () {
      // 为了得到卡片的高度，得到窗口的高度
      var winHeight = 0
      if (window.innerHeight) {
        winHeight = window.innerHeight
      } else if ((document.body) && (document.body.clientHeight)) {
        winHeight = document.body.clientHeight
      }
      if (document.documentElement && document.documentElement.clientHeight) {
        winHeight = document.documentElement.clientHeight
      }
      //设置两张卡片的高度
      document.querySelector('.el-card__body').style.height = winHeight - 60 - 20 - 40 - 10 + 'px'
      document.querySelectorAll('.el-card__body')[1].style.height = winHeight - 60 - 20 - 40 - 10 + 'px'
      console.log(document.querySelectorAll('.el-scrollbar__wrap'))
      var scrollbar_list = document.querySelectorAll('.el-scrollbar__wrap')
      for (var i = 0 ; i < 4 ; i++) {
        scrollbar_list[i].style.overflowX = 'hidden'
      }
      //设置embedding区域的高度
      var embedding_block = document.querySelectorAll('.embedding')
      var embedding_height = winHeight - 60 + 'px'
      for (var i = 0 ; i < 2 ; i++) {
        embedding_block[i].style.height = embedding_height
      }
      //这一页允许进行滚动
      document.getElementsByTagName('body')[0].className = 'allow_scroll'
      //设置guidelineid
      var myself = this
      this.guideline_id = Math.random().toString(36).substr(2)
      var obj = {
        'guideline_id': this.guideline_id,
        'model_name': 'dssm'
      }
      axios.post('./get_jupyter', obj).then(function (response) {
        myself.jupyter_url1 = response.data['jupyter_url']
      }).catch(function (err) {
        console.log('加载guideline时出错')
      })
    },
    data: function () {
      return {
        jupyter_url1: '',
        jupyter_url2: 'https://matchzoo.readthedocs.io/en/master/modules.html'
      }
    }
  }
</script>

<style scoped>
  .embedding {
    width: 100%
  }

  .allow_scroll {
    overflow: scroll;
  }
</style>
