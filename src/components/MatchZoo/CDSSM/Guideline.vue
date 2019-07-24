<template>
    <div id="cdssm-guideline">
      <iframe :src="jupyter_url" frameborder="0" id="embedding"></iframe>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Guideline',
    data: function () {
      return {
        guidline_id: '',
        jupyter_url: ''
      }
    },
    mounted: function () {
      var title = document.querySelector('#title')
      var title_height = parseInt(window.getComputedStyle(title, null).getPropertyValue('height'))
      var winHeight = 0
      if (window.innerHeight) {
        winHeight = window.innerHeight
      } else if ((document.body) && (document.body.clientHeight)) {
        winHeight = document.body.clientHeight
      }
      if (document.documentElement && document.documentElement.clientHeight) {
        winHeight = document.documentElement.clientHeight
      }
      var embedding_height = winHeight - title_height - (20 + 8 + 60 + 15 + 40) + 'px'
      var embedding_iframe = document.querySelector('#embedding')
      embedding_iframe.style.height = embedding_height

      //设置guidelineid
      var myself = this
      this.guideline_id = Math.random().toString(36).substr(2)
      var obj = {
        'guideline_id': this.guideline_id,
        'model_name': 'cdssm'
      }
      axios.post('./get_jupyter', obj).then(function (response) {
        myself.jupyter_url = response.data['jupyter_url']
      }).catch(function (err) {
        console.log('加载guideline时出错')
      })
    }
  }
</script>

<style scoped>
  #embedding {
    width: 100%;
  }
</style>
