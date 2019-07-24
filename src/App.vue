<template>
  <div id="app">
    <!-- <vue-headful title="NLP Platform - NDST CAS" description="NLP Platform" /> -->
    <el-container>
      <!--
      <el-header>
        <el-menu
          :default-active="activeIndex"
          mode="horizontal"
          :router="true"
          active-text-color="#409eff"
        >
          <el-menu-item index="/tr/text_segmentation">Core NLU</el-menu-item>

          <!--   <el-submenu index="2">
            <template slot="title">Tasks</template>
              <el-menu-item index="/qa">Question Answering</el-menu-item>
              <el-menu-item index="/rc">Reading Comprehension</el-menu-item>
              <el-menu-item index="/search">Search</el-menu-item>
              <el-menu-item index="2-4-3">Machine Translation</el-menu-item>
              <el-menu-item index="/summarization">Summarization</el-menu-item>
          </el-submenu>


          <el-menu-item index="/matchzoo/matchzoointroduction">MatchZoo</el-menu-item>


        </el-menu>
      </el-header>
       -->
      <el-main>
        <!-- <el-tabs tab-position="top" v-model="activeName" @tab-click="handleClick">
            <el-tab-pane label="Info" name="/">Info</el-tab-pane>
            <el-tab-pane label="QA" name="qa"></el-tab-pane>
            <el-tab-pane label="Summarization" name="summarization"><p>Text Summarization</p></el-tab-pane>
            <el-tab-pane label="Recommendation" name="recommendation">Recommendation</el-tab-pane> -->
        <!-- <router-view/>  -->
        <!-- </el-tabs> -->
        <matchzoo></matchzoo>
      </el-main>
      <el-footer></el-footer>
    </el-container>
  </div>
</template>

<script>
  /* eslint-disable */
  import router from './router'
  import MatchZoo from '@/components/MatchZoo/MatchZoo'

  export default {
    name: 'app',
    data () {
      return {
        activeIndex: '/',
        activeName: 'second'
      }
    },
    methods: {
      handleClick (tab, event) {
        router.push(this.activeName),
          console.log(tab, event)
      }
    },
    components: {
      'matchzoo': MatchZoo
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    /*margin-top: -10px;*/
  }
</style>
