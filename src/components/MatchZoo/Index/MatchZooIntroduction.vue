<template>
  <div id="matchzoointroduction">
    <el-row :gutter="20">
      <el-col :span="15">
        <el-card>
          <el-scrollbar style="height:100%;">
            <introleftcard></introleftcard>
          </el-scrollbar>
        </el-card>
      </el-col>
      <el-col :span="9">
        <el-scrollbar style="height:100%;">
          <el-card>
            <el-scrollbar style="height:100%;">
              <introrightcard></introrightcard>
            </el-scrollbar>
          </el-card>
        </el-scrollbar>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import VueMarkdown from 'vue-markdown'
  import IntroLeftCard from './IntroLeftCard'
  import IntroRightCard from './IntroRightCard'

  export default {
    name: 'MatchZooIntroduction',
    components: {
      'introleftcard': IntroLeftCard,
      'introrightcard': IntroRightCard,
      VueMarkdown
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
      // 设置两张卡片的高度
      document.querySelector('.el-card__body').style.height = winHeight - 20 - 20 + 'px'
      document.querySelectorAll('.el-card__body')[1].style.height = winHeight - 20 - 20 + 'px'
      console.log(document.querySelectorAll('.el-card__body'))
      var scrollbar_list = document.querySelectorAll('.el-scrollbar__wrap')
      for (var i = 0 ; i < 4 ; i++) {
        scrollbar_list[i].style.overflowX = 'hidden'
      }
    }
  }
</script>

<style scoped>
  #matchzoointroduction {
    text-align: left;
  }
</style>
