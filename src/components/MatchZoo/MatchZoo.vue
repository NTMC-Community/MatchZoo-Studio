<template>
  <div id="matchzoo">
    <el-container>
      <!-- 左边 -->
      <el-aside id="left_aside" width="12%">
        <!-- logo on the left corner -->
        <router-link to="/">
          <div id="logo">
            <img class="logo-pic" src="../../assets/matchzoo-logo.png" alt="">
          </div>
        </router-link>

        <div id="left_scroll">
          <el-scrollbar style="height:100%" :native="false">
            <el-menu id="left_menu" default-active="13" class="el-menu-vertical-demo"
                     :router="true">
              <el-menu-item index="/drmm">
                <span>DRMM</span>
              </el-menu-item>
              <el-menu-item index="/matchpyramid">
                <span>MatchPyramid</span>
              </el-menu-item>
              <el-menu-item index="/arci">
                <span>ARC-I</span>
              </el-menu-item>
              <el-menu-item index="/dssm">
                <span>DSSM</span>
              </el-menu-item>
              <el-menu-item index="/cdssm">
                <span>CDSSM</span>
              </el-menu-item>
              <el-menu-item index="/arcii">
                <span>ARC-II</span>
              </el-menu-item>
              <el-menu-item index="/mvlstm">
                <span>MV-LSTM</span>
              </el-menu-item>
              <!--
              <el-menu-item index="/matchzoo/anmm">
                <span>aNMM</span>
              </el-menu-item>
               -->
              <el-menu-item index="/duet">
                <span>DUET</span>
              </el-menu-item>
              <el-menu-item index="/knrm">
                <span>K-NRM</span>
              </el-menu-item>
              <el-menu-item index="/conv_knrm">
                <span>CONV-KNRM</span>
              </el-menu-item>
              <el-menu-item index="/new_model">
                <i class="el-icon-location"></i>
                <span>MODEL DESIGN</span>
              </el-menu-item>
              <el-menu-item index="/tune">
                <i class="el-icon-location"></i>
                <span>TUNE</span>
              </el-menu-item>
              <el-menu-item index="14" disabled>
                <span></span>
              </el-menu-item>
            </el-menu>
          </el-scrollbar>
        </div>
      </el-aside>

      <!-- 右边 -->
      <el-main id="center_main">
        <router-view></router-view>
      </el-main>
    </el-container>
  </div>
</template>

<script>
  export default {
    name: 'MatchZoo',
    data () {
      return {}
    },
    mounted: function () {
      document.getElementsByTagName('body')[0].className = 'ban_y_scroll'
      // 获取浏览器窗口高度
      var winHeight = 0
      if (window.innerHeight) {
        winHeight = window.innerHeight
      } else if ((document.body) && (document.body.clientHeight)) {
        winHeight = document.body.clientHeight
      }
      if (document.documentElement && document.documentElement.clientHeight) {
        winHeight = document.documentElement.clientHeight
      }

      // winHeight -= 100
      this.winHeight = winHeight
      document.getElementById('center_main').style.height = winHeight + 'px'
      document.getElementById('left_aside').style.height = winHeight + 'px'

      var leftScrollWidth = parseInt(window.getComputedStyle(document.querySelector('#left_scroll'), null).getPropertyValue('width'))
      // 1359 350 492
      var logoHeight = leftScrollWidth * (492 / 1359)
      document.querySelector('#left_scroll').style.height = this.winHeight - logoHeight + 'px'
    },
    destroyed: function () {
      document.getElementsByTagName('body')[0].className = 'allow_y_scroll'
    }
  }
</script>

<style>
  #logo {
    width: 100%;
    padding-bottom: 20px;
  }

  .logo-pic {
    width: 100%;
  }

  #left_aside {
    overflow: scroll;
    /*overflow-x: hidden;*/
    overflow-y: hidden;
  }

  #center_main {
    padding: 0 10px;
    overflow: hidden;
  }

  #header-font-size {
    font-size: 30px;
  }

  #matchzoo {
    font-family: Helvetica, sans-serif;
    text-align: center;
  }

  #text-dir {
    text-align: left;
    line-height: 150%;
  }

  .ban_y_scroll {
    /*overflow: scroll;*/
    overflow-x: hidden;
    overflow-y: hidden;
  }

  .allow_y_scroll {
    overflow-x: scroll;
    overflow-y: scroll;
  }

  #title-style {
    text-align: left;
    color: #909399;
  }

</style>
