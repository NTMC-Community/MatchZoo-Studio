<template>
  <div id="cdssm-demo">
    <el-row :gutter="20">
      <el-col :span="14">
        <el-card id="card1">
          <el-scrollbar style="height:100%">
            <el-collapse v-model="activeName" accordion v-on:change="changeActiveName()">
              <el-collapse-item name="1">
                <template slot="title">
                  Train &nbsp;<i class="header-icon el-icon-info"></i>
                </template>
                <div class="config-page">

                  <el-card style="margin-bottom:20px;">
                    <div slot="header" class="clearfix">
                      <span>Train Configuration</span>
                      <i class="el-icon-edit"></i>
                    </div>
                    <el-row>
                      <el-col :span="12">
                        <el-form label-width="130px" label-position="left" size="small">
                          <el-tooltip class="item" effect="dark" content="Right Top 提示文字" placement="right-start">
                            <el-form-item label="batch_size">
                              <el-input-number v-model="batch_size" :min="0" :max="500"></el-input-number>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Right Top 提示文字" placement="right-start">
                            <el-form-item label="epochs">
                              <el-input-number v-model="epochs" :min="0" :max="500"></el-input-number>
                            </el-form-item>
                          </el-tooltip>
                        </el-form>
                      </el-col>

                      <el-col :span="11">
                        <el-form label-width="130px" label-position="left" size="small">
                          <el-tooltip class="item" effect="dark" content="Decides model output shape, loss, and metrics."
                                      placement="right-start">
                            <el-form-item label="task">
                              <el-select v-model="task" size="small">
                                <el-option
                                  v-for="item in task_options"
                                  :key="item.label"
                                  :label="item.label"
                                  :value="item.label">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Right Top 提示文字" placement="right-start">
                            <el-form-item label="optimizer">
                              <el-select v-model="optimizer" size="small">
                                <el-option
                                  v-for="item in optimizer_options"
                                  :key="item.label"
                                  :label="item.label"
                                  :value="item.label">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-tooltip>

                        </el-form>
                      </el-col>
                    </el-row>
                  </el-card>

                  <el-card style="margin-bottom: 20px">
                    <div slot="header" class="clearfix">
                      <span>Model Configuration</span>
                      <i class="el-icon-edit"></i>
                    </div>
                    <el-row>
                      <el-col :span="12">
                        <!-- 每个模型不同的部分：修改开始 -->
                        <el-form label-width="130px" label-position="left" size="small">

                          <el-tooltip class="item" effect="dark" content="Number of filters in the 1D convolution layer." placement="right-start">
                            <el-form-item label="filters">
                              <el-input-number v-model="filters" :min="1" :max="500"></el-input-number>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Number of kernel size in the 1D convolution layer." placement="right-start">
                            <el-form-item label="kernel_size">
                              <el-input-number v-model="kernel_size" :min="1" :max="10"></el-input-number>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Strides in the 1D convolution layer." placement="right-start">
                            <el-form-item label="strides">
                              <el-input-number v-model="strides" :min="1" :max="10"></el-input-number>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Number of units of the layer that connects the multiple layer percetron and the output." placement="right-start">
                            <el-form-item label="mlp_num_fan_out">
                              <el-input-number v-model="mlp_num_fan_out" :min="0" :max="500"></el-input-number>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Number of units in first mlp_num_layers layers." placement="right-start">
                            <el-form-item label="mlp_num_units">
                              <el-input-number v-model="mlp_num_units" :min="0" :max="1000"></el-input-number>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Number of layers of the multiple layer percetron." placement="right-start">
                            <el-form-item label="mlp_num_layers">
                              <el-input-number v-model="mlp_num_layers" :min="1" :max="10"></el-input-number>
                            </el-form-item>
                          </el-tooltip>
                        </el-form>
                      </el-col>

                      <el-col :span="11">
                        <el-form label-width="130px" label-position="left" size="small">

                          <el-tooltip class="item" effect="dark" content="Activation function used in the multiple layer perceptron." placement="right-start">
                            <el-form-item label="mlp_activation_func">
                              <el-select v-model="mlp_activation_func" size="small">
                                <el-option
                                  v-for="item in activation_options"
                                  :key="item.label"
                                  :label="item.label"
                                  :value="item.label">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Activation function in the convolution layer." placement="right-start">
                            <el-form-item label="conv_activation_func">
                              <el-select v-model="conv_activation_func" size="small">
                                <el-option
                                  v-for="item in activation_options"
                                  :key="item.label"
                                  :label="item.label"
                                  :value="item.label">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="The padding mode in the convolution layer." placement="right-start">
                            <el-form-item label="padding">
                              <el-select v-model="padding" size="small">
                                <el-option
                                  v-for="item in padding_options"
                                  :key="item.label"
                                  :label="item.label"
                                  :value="item.label">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Initializer for weight" placement="right-start">
                            <el-form-item label="w_initializer">
                              <el-select v-model="w_initializer" size="small">
                                <el-option
                                  v-for="item in w_options"
                                  :key="item.label"
                                  :label="item.label"
                                  :value="item.label">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-tooltip>

                          <el-tooltip class="item" effect="dark" content="Initializer for bias" placement="right-start">
                            <el-form-item label="b_initializer">
                              <el-select v-model="b_initializer" size="small">
                                <el-option
                                  v-for="item in b_options"
                                  :key="item.label"
                                  :label="item.label"
                                  :value="item.label">
                                </el-option>
                              </el-select>
                            </el-form-item>
                          </el-tooltip>

                        </el-form>
                      </el-col>
                    </el-row>
                  </el-card>
                  <!-- 每个模型不同的部分：修改结束 -->
                  <div class="upload-page">
                    <el-card>
                      <div slot="header" class="clearfix">
                        <span>Choose a dataset</span>
                        <i class="el-icon-edit"></i>
                        <div style="float:right">
                          <el-switch
                            style="display: block"
                            v-model="dataset_method"
                            active-color="#409eff"
                            inactive-color="#13ce66"
                            active-text="Upload new one"
                            inactive-text="Choose an existing dataset"
                          >
                          </el-switch>
                        </div>
                      </div>
                      <div id="self-upload" v-if="dataset_method">
                        <el-upload
                          class="upload-demo"
                          id="upload-block"
                          drag
                          action="./files"
                          :limit="2"
                          :on-success="uploadSuccess"
                          :before-upload="uploadCheck"
                        >
                          <i class="el-icon-upload"></i>
                          <div class="el-upload__text">Upload your training set，<em> click to upload</em></div>
                          <div class="el-upload__tip" slot="tip">json format only, file does not exceed 1GB</div>
                        </el-upload>
                      </div>
                      <div id="existing-dataset" v-if="!dataset_method">
                        <el-radio-group v-model="existing_dataset">
                          <el-radio label="Toy"></el-radio>
                          <el-radio label="WikiQA"></el-radio>
                          <el-radio label="SNLI"></el-radio>
                          <el-radio label="QuoraQP"></el-radio>
                        </el-radio-group>
                      </div>
                    </el-card>
                    <!-- preprocess按钮逻辑：if (要自己上传&&还没有上传成功)||禁用按钮  则按钮禁用-->
                    <el-button type="primary" icon="el-icon-view" style="margin-top:20px"
                               @mouseup.native="sendTrainHead()"
                               v-on:click="clickTrain()"
                               :disabled="(dataset_method && not_upload) || disabled_train_button">Train
                    </el-button>
                  </div>
                </div>
              </el-collapse-item>

              <el-collapse-item name="2">
                <template slot="title">
                  Predict &nbsp;<i class="header-icon el-icon-info"></i>
                </template>
                <div style="width:70%;">
                  <el-form ref="form" :model="form" label-width="80px">
                    <el-form-item label="Pair Case">
                      <el-select v-model="form.value" placeholder="You can choose a case here" @change="choose_doc"
                                 style="width:100%;">
                        <el-option v-for="n in 10" :key="n" :label="n" :value="n">Document {{ n }}</el-option>
                      </el-select>
                    </el-form-item>
                    <el-form-item label="Document1">
                      <el-input ref="doc1" type="textarea" v-model="form.document1"
                                :autosize="{ minRows:7, maxRows:20 }"></el-input>
                    </el-form-item>
                    <el-form-item label="Document2">
                      <el-input ref="doc2" type="textarea" v-model="form.document2"
                                :autosize="{ minRows:7, maxRows:20 }"></el-input>
                    </el-form-item>
                  </el-form>
                  <el-button v-on:click="clickPredict()" type="primary" id="matchzoobutton">Submit <i
                    class="el-icon-upload el-icon--right"></i></el-button>
                </div>
              </el-collapse-item>

            </el-collapse>
          </el-scrollbar>
        </el-card>
      </el-col>
      <el-col :span="10">
        <el-card>
          <el-scrollbar style="height:100%;">
            <!--
            <el-card id="matchzootab-card">
              <matchzootab></matchzootab>
            </el-card>
             -->
            <transition name="el-fade-in-linear">
              <div id="preprocessor-console" v-if="preprocessing">
                {{preprocess_text1}} <br>
                {{preprocess_text2}} <br>
                {{preprocess_text3}} <br>
              </div>
            </transition>
            <losschart v-bind:traindata="next_loss_data"
                       v-bind:min_height="loss_min_height"
                       v-bind:max_height="loss_max_height"
                       v-bind:x_axis="x_axis"
                       v-if="show_train_card"></losschart>
            <accuracychart v-bind:accuracydata="next_accuracy_data"
                           v-bind:min_height="accuracy_min_height"
                           v-bind:max_height="accuracy_max_height"
                           v-bind:x_axis="x_axis"
                           v-if="show_train_card"></accuracychart>
            <chartdescription
              v-if="show_train_card && (lock_tag===3 || (lock_tag===0 && task==='ranking'))">
            </chartdescription>
            <div v-if="!show_train_card">加载成功{{ temp_val }}</div>
          </el-scrollbar>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import axios from 'axios'
  import LossChart from '../LossChart'
  import AccuracyChart from '../AccuracyChart'
  import MatchZooTab from '../MatchZooTab'
  import ChartDescription from '../ChartDescription'

  export default {
    name: 'Demo',
    data () {
      return {
        // 下面是控制相关的变量
        activeNameBefore: '1',
        activeName: '1',
        train_id: '',
        end_train: false,
        show_train_card: true,
        temp_val: -1,
        disabled_preprocess_button: false,
        disabled_train_button: false,
        upload_first: false, //第一个文件是否上传
        not_upload: true, //两个文件没有全部上传
        train_csv_upload: false, // train.csv是否上传
        test_csv_upload: false, // test.csv是否上传
        dataset_method: true,
        existing_dataset: 'Toy',
        // 下面是preprocess打印控制台相关的变量
        preprocessing: false,
        last_line: -1,
        preprocess_queue: [],
        preprocess_text1: '',
        preprocess_text2: '',
        preprocess_text3: '',
        // 下面是绘图相关的变量
        loss_data: [[]],
        accuracy_data: [[],[],[]],
        next_loss_data: [[]],
        next_accuracy_data: [[],[],[]],
        loss_min_height: 0,
        loss_max_height: 2,
        accuracy_min_height: 0,
        accuracy_max_height: 2,
        x_axis: 10,
        lock_tag: 0, // 一旦点击train，accuracy图表就确定是一条线还是三条线：0表示未确定，1表示确定1条线，3表示确定3条线
        // 下面是训练相关的参数
        batch_size: 32,
        epochs: 30,
        task: 'ranking',
        optimizer: 'sgd',
        task_options: [
          {
            label: 'ranking'
          },
          {
            label: 'classification'
          }
        ],
        optimizer_options: [
          {
            label: 'sgd'
          },
          {
            label: 'rmsprops'
          },
          {
            label: 'adagrad'
          },
          {
            label: 'adadelta'
          },
          {
            label: 'adam'
          },
          {
            label: 'adamax'
          },
          {
            label: 'nadam'
          }
        ],
        // 下面是模型的参数
        filters: 32,
        kernel_size: 3,
        conv_activation_func: 'relu',
        strides: 1,
        padding: 'same',
        w_initializer: 'glorot_normal',
        b_initializer: 'zeros',
        mlp_num_fan_out: 128,
        mlp_num_units: 300,
        mlp_activation_func: 'relu',
        mlp_num_layers: 3,
        activation_options: [
          {
            label: 'relu'
          },
          {
            label: 'tanh'
          }
        ],
        padding_options: [
          {
            label: 'same'
          },
          {
            label: 'valid'
          },
          {
            label: 'causal'
          }
        ],
        w_options: [
          {
            label: 'glorot_normal'
          }
        ],
        b_options: [
          {
            label: 'zeros'
          },
          {
            label: 'ones'
          }
        ],

        form: {
          value: null,
          document1: '',
          document2: '',
          doc_from1: [
            'how are glacier caves formed?',
            'How are the directions of the velocity and force vectors related in a circular motion',
            'how did apollo creed die',
            'how long is the term for federal judges',
            'how a beretta model 21 pistols magazines works',
            'how a vul works D9 Variable universal life insurance',
            'how an outdoor wood boiler works',
            'how big did girl scout cookie boxes used to be',
            'how big is the purdue greek system',
            'how big do sebaceous cysts get'
          ],
          doc_from2: [
            'A glacier cave is a cave formed within the ice of a glacier .',
            'In physics , circular motion is a movement of an object along the circumference of a circle or rotation along a circular path.',
            'Urban legend states that Apollo Creed\'s name is a wordplay on the Apostles\' Creed , a statement of belief used in Christian churches.',
            'Every judge appointed to such a court may be categorized as a federal judge; such positions include the Chief Justice and Associate Justices of the Supreme Court, Circuit Judges of the courts of appeals, and district judges of the United States district courts .',
            'The Beretta 21A Bobcat is a small pocket-sized semi-automatic pistol designed by Beretta in Italy.',
            'Variable Universal Life Insurance (often shortened to VUL) is a type of life insurance that builds a cash value.',
            'The outdoor wood boiler is a variant of the classic wood stove adapted for set-up outdoors while still transferring the heat to interior buildings.',
            'There are also unit incentives if the unit as a whole does well.',
            'Purdue was founded on May 6, 1869, as a land-grant university when the Indiana General Assembly , taking advantage of the Morrill Act , accepted a donation of land and money from Lafayette businessman John Purdue to establish a college of science, technology, and agriculture in his name.',
            'n practice, however, the terms are often used interchangeably..'
          ]
        }
      }
    },
    components: {
      'losschart': LossChart,
      'accuracychart': AccuracyChart,
      'matchzootab': MatchZooTab,
      'chartdescription': ChartDescription
    },
    methods: {
      // 控制折叠面板折叠和打开的触发函数，保证至少有且只有一个是展开状态的
      changeActiveName: function () {
        if (this.activeNameBefore === '1' && this.activeName === '') {
          this.activeName = '2'
        } else if (this.activeNameBefore === '1' && this.activeName === '2') {
          this.activeName = '2'
        } else if (this.activeNameBefore === '2' && this.activeName === '') {
          this.activeName = '1'
        } else if (this.activeNameBefore === '2' && this.activeName === '1') {
          this.activeName = '1'
        }
        this.activeNameBefore = this.activeName
      },
      // 对于上传的文件进行检查
      uploadCheck: function(file) {
        let name_check = true
        if (file.name !== 'train.csv' && file.name !== 'test.csv') {
          name_check = false
          this.$message({
            showClose: true,
            message: 'Please check your file name',
            type: 'error'
          })
        }
        else {
          if (file.name === 'train.csv' && this.train_csv_upload === true) {
            name_check = false
            this.$message({
              showClose: true,
              message: 'Repeatedly upload train.csv',
              type: 'error'
            })
          }
          else if(file.name === 'test.csv' && this.test_csv_upload === true){
            name_check = false
            this.$message({
              showClose: true,
              message: 'Repeatedly upload test.csv',
              type: 'error'
            })
          }
        }
        let size_check = ((file.size / 1024 / 1024) <= 2)
        if (size_check === false) {
          this.$message({
            showClose: true,
            message: 'File size should not exceed 20MB',
            type: 'error'
          })
        }
        return name_check && size_check
      },
      // 上传文件成功时触发的函数
      uploadSuccess: function (response, file, fileList) {
        var new_file_name
        if (this.upload_first === false) { // 如果是第一个文件成功上传，生成一个train_id
          this.train_id = Math.random().toString(36).substr(2)
        }
        if (file.name === 'train.csv') {
          this.train_csv_upload = true
          new_file_name = this.train_id + '.train'
        }
        else {
          this.test_csv_upload = true
          new_file_name = this.train_id + '.valid'
        }
        var obj = {
          'old_name': file.name,
          'new_name': new_file_name
        }
        axios.post('./file_rename', obj).then(function (response) {

        }).catch(function (err) {
          console.log('When rename the uploaded file, an error happend!')
        })
        if (this.upload_first === false) {
          this.upload_first = true
        }
        else {
          this.not_upload = false
        }
      },
      // 发送train的首请求，把后台训练的进程跑起来
      sendTrainHead: function () {
        // 如果是选择现成的训练数据，那么就没有产生train_id，那就在单击Train的时候生成一个
        if (this.not_upload) {
          this.train_id = Math.random().toString(36).substr(2)
        }
        else { // 如果是自己上传数据，那么existing_dataset置为'$None$'
          this.existing_dataset = '$None$'
        }
        // 黑色控制台幕布出现
        this.preprocessing = true
        var dataobject = {
          batch_size: this.batch_size,
          epochs: this.epochs,
          task: this.task,
          optimizer: this.optimizer,
          filters: this.filters,
          kernel_size: this.kernel_size,
          conv_activation_func: this.conv_activation_func,
          strides: this.strides,
          padding: this.padding,
          w_initializer: this.w_initializer,
          b_initializer: this.b_initializer,
          mlp_num_fan_out: this.mlp_num_fan_out,
          mlp_num_units: this.mlp_num_units,
          mlp_activation_func: this.mlp_activation_func,
          mlp_num_layers: this.mlp_num_layers,
          existing_dataset: this.existing_dataset
        }
        var head_obj = {
          id: Math.random().toString(36).substr(2),
          train_id: this.train_id,
          parameter: dataobject
        }
        axios.post('./train/head/cdssm', head_obj).then(function (response) {

        }).catch(function (err) {
          console.log('在train发送首请求之后出现了错误:' + err)
        })
      },
      // 点击Train按钮时触发的函数，设置计时器并定时向后端进行轮询
      clickTrain: function () {
        this.disabled_train_button = true
        if (this.task === 'ranking') {
          this.lock_tag = 3
        } else {
          this.lock_tag = 1
        }
        //发送第2类请求并定时进行轮询
        var myself = this
        //3s轮询一次后端，要来preprocessing过程最新的控制台输出
        var preprocess_timer = setInterval(getPreprocessData, 3000)
        //0.6秒刷新一次页面，把最新的preprocessing控制台信息显示出来
        var setPreprocessTimer = setInterval(setPreprocessData, 600)
        //声明获取训练结果，利用训练结果刷新页面两个功能的定时器
        var timer,setTrainTimer
        function getPreprocessData () {
          var obj = {
            id: Math.random().toString(36).substr(2),
            preprocess_id: myself.train_id,
            last_line: myself.last_line
          }
          axios.post('./preprocess/cdssm', obj).then(function (response) {
            var console_list = response.data['console_list']
            for (var i = myself.last_line; i < console_list.length; i++) {
              myself.preprocess_queue.push(console_list[i])
            }
            myself.last_line = console_list.length
            if (myself.preprocess_queue.length >= 1 && myself.preprocess_queue[myself.preprocess_queue.length - 1].indexOf('Preprocess finished!') >= 0) {
              clearInterval(preprocess_timer)
            }
          }).catch(function (err) {
            console.log('preprocess轮询时出错:' + err)
          })
        }

        function setPreprocessData () {
          while (myself.preprocess_queue.length > 1) {
            var new_text = myself.preprocess_queue[0]
            myself.preprocess_queue.shift()
            if (new_text.length < 2) {
              continue
            }
            if (myself.preprocess_text1.length < 2) {
              myself.preprocess_text1 = new_text
              break
            }
            else if (myself.preprocess_text2.length < 2) {
              myself.preprocess_text2 = new_text
              break
            }
            else if (myself.preprocess_text3.length < 2) {
              myself.preprocess_text3 = new_text
              break
            }
            else {
              myself.preprocess_text1 = myself.preprocess_text2
              myself.preprocess_text2 = myself.preprocess_text3
              myself.preprocess_text3 = myself.preprocess_queue[0]
            }
          }
          if (myself.preprocess_text3.indexOf('Preprocess finished!') >= 0) {
            clearInterval(setPreprocessTimer)
            myself.preprocessing = false
            //控制台显示preprocessing信息结束时开始轮询训练得到的数据
            timer = setInterval(getTrainData, 10000)
            setTrainTimer = setInterval(setTrainData, 700)
          }
        }

        function getTrainData () {
          var obj = {
            id: Math.random().toString(36).substr(2),
            train_id: myself.train_id,
            epochs: myself.epochs
          }
          axios.post('./train/query/cdssm', obj).then(function (response) {
            if (response.data['state'] === 'run') {
              myself.loss_data = response.data['data']['loss']
              myself.accuracy_data = response.data['data']['accuracy']
              console.log('收到了轮询的结果')
            } else if (response.data['state'] === 'end') {
              myself.loss_data = response.data['data']['loss']
              myself.accuracy_data = response.data['data']['accuracy']
              // myself.activeName = '2'
              // myself.activeNameBefore = myself.activeName
              clearInterval(timer)
              myself.end_train = true
            }
          }).catch(function (error) {
            console.log('出错!', error)
          })
        }

        function setTrainData () {
          console.log('call set train data')
          var tag = true
          if (myself.loss_data[0].length > myself.next_loss_data[0].length) {
            tag = false
            myself.next_loss_data[0].push(myself.loss_data[0][myself.next_loss_data[0].length])
          }
          if (myself.accuracy_data[0].length > myself.next_accuracy_data[0].length) {
            tag = false
            myself.next_accuracy_data[0].push(myself.accuracy_data[0][myself.next_accuracy_data[0].length])
            myself.next_accuracy_data[1].push(myself.accuracy_data[1][myself.next_accuracy_data[1].length])
            myself.next_accuracy_data[2].push(myself.accuracy_data[2][myself.next_accuracy_data[2].length])
          }
          // 正确设置loss_chart的高度
          var maxv = -10000000, minv = 10000000
          for (var i = 0; i < myself.next_loss_data[0].length; i++) {
            maxv = Math.max(myself.next_loss_data[0][i].y, maxv)
            minv = Math.min(myself.next_loss_data[0][i].y, minv)
          }
          var half_loss_height = (maxv - minv) / 2.0
          myself.loss_min_height = minv - half_loss_height
          myself.loss_max_height = maxv + half_loss_height
          // 正确设置accuracy_chart的高度
          maxv = -100000000
          minv = 100000000
          for (var i = 0; i < myself.next_accuracy_data[0].length; i++) {
            for (var j = 0; j < 3; j++) {
              maxv = Math.max(myself.next_accuracy_data[j][i].y, maxv)
              minv = Math.min(myself.next_accuracy_data[j][i].y, minv)
            }
          }
          var half_accuracy_height = (maxv - minv) / 2.0
          myself.accuracy_min_height = minv - half_accuracy_height
          myself.accuracy_max_height = maxv + half_accuracy_height

          if (myself.next_loss_data[0].length > myself.x_axis) {
            if (2 * myself.x_axis <= myself.epochs) {
              myself.x_axis = 2 * myself.x_axis
            }
            else {
              myself.x_axis = myself.epochs
            }
          }

          if (tag && myself.end_train === true) {
            clearInterval(setTrainTimer)
            myself.disabled_train_button = true
            myself.activeName = '2'
            myself.activeNameBefore = myself.activeName
          }
        }

      },
      clickPredict: function () {
        var myself = this
        var obj = {
          'text1': this.form.document1,
          'text2': this.form.document2,
          'train_id': this.train_id
        }
        if (this.end_train === false) {
          alert('Please finish training first')
        } else {
          axios.post('./predict/cdssm', obj).then(function (response) {
            myself.show_train_card = false
            myself.temp_val = response.data['score']
          }).catch(function (err) {
            console.log('预测时出错')
          })
        }
      },
      choose_doc: function () {
        this.form.document1 = this.form.doc_from1[this.form.value - 1]
        this.form.document2 = this.form.doc_from2[this.form.value - 1]
      },
    },
    mounted: function () {
      // 去掉第一个card的margin，不至于显得层数太多太难看
      var leftCard = document.querySelectorAll('.el-card__body')[2]
      leftCard.style.paddingTop = '0'

      // 把折叠面板的两个箭头从上面移到中间
      var arrow1 = document.getElementsByClassName('el-collapse-item__header')[0].getElementsByTagName('i')[0]
      arrow1.style.lineHeight = '48px'
      document.getElementsByClassName('el-collapse-item__header')[0].style.fontSize = '16px'
      document.getElementsByClassName('el-collapse-item__header')[0].style.textAlign = 'left'
      // document.getElementsByClassName('el-collapse-item__header')[0].style.marginLeft = '20px'

      var arrow2 = document.getElementsByClassName('el-collapse-item__header')[1].getElementsByTagName('i')[0]
      document.getElementsByClassName('el-collapse-item__header')[1].style.fontSize = '16px'
      document.getElementsByClassName('el-collapse-item__header')[1].style.textAlign = 'left'
      // document.getElementsByClassName('el-collapse-item__header')[1].style.marginLeft = '20px'
      arrow2.style.lineHeight = '48px'

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
      // 设置卡片的高度
      var title = document.querySelector('#title')
      var titleHeight = parseInt(window.getComputedStyle(title, null).getPropertyValue('height'))
      document.querySelectorAll('.el-card__body')[0].style.height = winHeight - 60 - 20 - titleHeight - 40 - 10 + 'px'
      document.querySelectorAll('.el-card__body')[1].style.height = winHeight - 60 - 20 - titleHeight - 40 - 10 + 'px'
      document.querySelectorAll('.el-card__body')[2].style.height = winHeight - 60 - 20 - titleHeight - 40 - 10 + 20 + 'px'
      document.querySelectorAll('.el-card__body')[6].style.height = winHeight - 60 - 20 - titleHeight - 40 - 10 + 'px'
      //去掉三个卡片最下面的自带的横向滚动条，因为三个滚动条太显眼了影响美观
      var scrollbar_list = document.querySelectorAll('.el-scrollbar__wrap')
      scrollbar_list[0].style.overflowX = 'hidden'
      scrollbar_list[4].style.overflowX = 'hidden'
      scrollbar_list[scrollbar_list.length - 1].style.overflowX = 'hidden'
      // configuration当中两个卡片的header的padding太大了，喧宾夺主的感觉，去掉
      var card_header = document.querySelectorAll('.el-card__header')
      for (var i = 0 ; i < 3 ; i++) {
        card_header[i].style.padding = '5px 20px'
      }
    }
  }
</script>

<style scoped>
  #cdssm-demo {
    overflow: hidden;
  }

  .config-page {
    margin-left: 5px;
  }

  .upload-page {
    width: 100%;
  }

  #matchzootab-card {
    overflow-y: hidden;
    overflow-x: scroll;
  }

  #preprocessor-console {
    position: absolute;
    width: 100%;
    height: 500px;
    border: 1px solid black;
    background-color: rgba(0, 0, 0, 0.8);
    text-align: left;
    line-height: 1.5em;
    padding: 10px 10px;
    word-wrap: break-word;
    color: #409eff;
    z-index: 2000;
    font-size: 16px;
  }

  .clearfix {
    text-align: left;
    font-size: 16px;
  }
</style>
