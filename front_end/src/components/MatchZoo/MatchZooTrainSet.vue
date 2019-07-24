<template>
  <div id="matchzootrainset">
    <el-collapse v-model="activenames">
      <el-collapse-item name="1">
        <template slot="title">
          set parameters here &nbsp;<i class="header-icon el-icon-info"></i>
        </template>
        <dssm v-if="chosen_model===3" ref="dssm_ref"></dssm>
        <arci v-if="chosen_model===2" ref="arci_ref"></arci>
      </el-collapse-item>
    </el-collapse>

    <el-collapse v-model="activenames">
      <el-collapse-item name="1">
        <template slot="title">
          upload train data &nbsp;<i class="header-icon el-icon-info"></i>
        </template>
        <el-upload
          class="upload-demo"
          id="upload-block"
          drag
          action="/api/files"
          :limit="1"
          :on-success="uploadSuccess"
          >
          <i class="el-icon-upload"></i>
          <div class="el-upload__text">Drag your file here，or<em> click to upload</em></div>
          <div class="el-upload__tip" slot="tip">json format only, file does not exceed 1GB</div>
        </el-upload>
      </el-collapse-item>
    </el-collapse>
    <el-button type="primary" icon="el-icon-view" style="margin-top:20px" v-on:click="clickTrain()">Train</el-button>
  </div>
</template>

<script>
  import axios from 'axios'
  import DSSM from './ParameterConfig/DSSM'
  import ARCI from './ParameterConfig/ARCI'
  export default {
    name: 'MatchZooTrainSet',
    components: {
      'dssm': DSSM,
      'arci': ARCI
    },
    data () {
      return {
        train_id: '',
        activenames: ['1', '2']
      }
    },
    props: {
      chosen_model: {
        type: Number,
        required: true
      }
    },
    methods: {
      uploadSuccess () {
        this.train_id = Math.random().toString(36).substr(2)
        console.log('成功上传：' + this.train_id)
      },
      clickTrain () {
        var myself = this
        // console.log(this.$refs.dssm_ref.get_data())
        function getTrainData () {
          var dataobject = {}
          if (this.chosen_model === '2') {
            dataobject = myself.$refs.arci_ref.get_data()
          } else if (this.chosen_model === '3') {
            dataobject = myself.$refs.dssm_ref.get_data()
          }
          var obj = {
            id: Math.random().toString(36).substr(2),
            train_id: myself.train_id,
            parameters: dataobject
          }
          axios.post('/api/train', obj).then(function (response) {
            // console.log(obj)
            if (response.data['state'] === 'run') {
              myself.$emit('traindata', response.data['data'])
            } else if (response.data['state'] === 'end') {
              clearInterval(timer)
            }
          }).catch(function (error) {
            console.log('出错!', error)
          })
        }
        var timer = setInterval(getTrainData, 10000)
      }
    },
    mounted: function () {
      var arrow1 = document.getElementsByClassName('el-collapse-item__header')[0].getElementsByTagName('i')[0]
      arrow1.style.lineHeight = '48px'
      document.getElementsByClassName('el-collapse-item__header')[0].style.fontSize = '16px'
      document.getElementsByClassName('el-collapse-item__header')[0].style.textAlign = 'left'
      var arrow2 = document.getElementsByClassName('el-collapse-item__header')[1].getElementsByTagName('i')[0]
      document.getElementsByClassName('el-collapse-item__header')[1].style.fontSize = '16px'
      document.getElementsByClassName('el-collapse-item__header')[1].style.textAlign = 'left'
      arrow2.style.lineHeight = '48px'
    }
  }
</script>

<style>
  #upload-block{
    margin-top: 50px;
  }
  #upload-tip{
    display:block;
    margin-top: 50px;
  }
  #para-title {
    line-height: 48px;
  }
</style>
