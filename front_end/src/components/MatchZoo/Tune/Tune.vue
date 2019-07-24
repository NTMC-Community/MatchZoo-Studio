<template>
  <div id="dssm-demo">
    <el-row :gutter="20">
      <el-col :span="14">
        <el-card id="card1">
          <div slot="header" class="clearfix" id="title">
            <span>Tune</span>
          </div>
          <el-scrollbar style="height:100%">
            <div class="config-page">
              <!-- 下面是上传数据集有关的显示 -->
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

              </div>

              <!-- 这里开始是model tuning部分的前端代码 -->
              <el-card style="margin-top: 20px">
                <div slot="header" class="clearfix">
                  <span>Config Models</span>
                  <i class="el-icon-edit"></i>
                </div>

                <el-form label-width="130px" label-position="left" size="medium" style="text-align: left;">
                  <el-form-item label="Choose Models">
                    <el-select v-model="chosen_models" multiple placeholder="click here to add and delete model"
                               style="width:100%;" v-on:change="change_models()">
                      <el-option
                        v-for="item in models"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                      </el-option>
                    </el-select>
                  </el-form-item>

                  <el-form-item label="Set Epochs">
                    <el-input-number v-model="epochs" size="small"></el-input-number>
                  </el-form-item>
                </el-form>

                <!-- DRMM -->
                <div v-if="model_config.DRMM.chosen" class="model_config_block">
                  <div class="divider"></div>
                  <el-tag style="font-size:16px;">DRMM</el-tag>
                  <br>
                  <el-form label-width="130px" label-position="left" size="medium">
                    <el-form-item label="mlp_num_units">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.DRMM.mlp_num_units_low" controls-position="right" :min="8"
                                       :max="model_config.DRMM.mlp_num_units_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.DRMM.mlp_num_units_high" controls-position="right"
                                       :min="model_config.DRMM.mlp_num_units_low" :max="255"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_layers">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.DRMM.mlp_num_layers_low" controls-position="right" :min="1"
                                       :max="model_config.DRMM.mlp_num_layers_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.DRMM.mlp_num_layers_high" controls-position="right"
                                       :min="model_config.DRMM.mlp_num_layers_low" :max="5"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_fan_out">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.DRMM.mlp_num_fan_out_low" controls-position="right"
                                       :min="4" :max="model_config.DRMM.mlp_num_fan_out_high"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.DRMM.mlp_num_fan_out_high" controls-position="right"
                                       :min="model_config.DRMM.mlp_num_fan_out_low" :max="127"
                                       size="small"></el-input-number>
                    </el-form-item>
                  </el-form>
                </div>

                <!-- ARCI -->
                <div v-if="model_config.ARCI.chosen" class="model_config_block">
                  <div class="divider"></div>
                  <el-tag style="font-size:16px;">ARC-I</el-tag>
                  <br>
                  <el-form label-width="130px" label-position="left" size="medium">
                    <el-form-item label="mlp_num_units">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.ARCI.mlp_num_units_low" controls-position="right" :min="8"
                                       :max="model_config.ARCI.mlp_num_units_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.ARCI.mlp_num_units_high" controls-position="right"
                                       :min="model_config.ARCI.mlp_num_units_low" :max="255"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_layers">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.ARCI.mlp_num_layers_low" controls-position="right" :min="1"
                                       :max="model_config.ARCI.mlp_num_layers_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.ARCI.mlp_num_layers_high" controls-position="right"
                                       :min="model_config.ARCI.mlp_num_layers_low" :max="5"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_fan_out">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.ARCI.mlp_num_fan_out_low" controls-position="right"
                                       :min="4" :max="model_config.ARCI.mlp_num_fan_out_high"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.ARCI.mlp_num_fan_out_high" controls-position="right"
                                       :min="model_config.ARCI.mlp_num_fan_out_low" :max="127"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="dropout_rate">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.ARCI.dropout_rate_low" controls-position="right" :min="0.0"
                                       :max="model_config.ARCI.dropout_rate_high" :precision="1" :step="0.1"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.ARCI.dropout_rate_high" controls-position="right"
                                       :min="model_config.ARCI.dropout_rate_low" :max="0.8" :precision="1" :step="0.1"
                                       size="small"></el-input-number>
                    </el-form-item>
                  </el-form>
                </div>

                <!-- DSSM -->
                <div v-if="model_config.DSSM.chosen" class="model_config_block">
                  <div class="divider"></div>
                  <el-tag style="font-size:16px;">DSSM</el-tag>
                  <br>
                  <el-form label-width="130px" label-position="left" size="medium">
                    <el-form-item label="mlp_num_units">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.DSSM.mlp_num_units_low" controls-position="right" :min="8"
                                       :max="model_config.DSSM.mlp_num_units_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.DSSM.mlp_num_units_high" controls-position="right"
                                       :min="model_config.DSSM.mlp_num_units_low" :max="255"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_layers">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.DSSM.mlp_num_layers_low" controls-position="right" :min="1"
                                       :max="model_config.DSSM.mlp_num_layers_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.DSSM.mlp_num_layers_high" controls-position="right"
                                       :min="model_config.DSSM.mlp_num_layers_low" :max="5"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_fan_out">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.DSSM.mlp_num_fan_out_low" controls-position="right"
                                       :min="4" :max="model_config.DSSM.mlp_num_fan_out_high"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.DSSM.mlp_num_fan_out_high" controls-position="right"
                                       :min="model_config.DSSM.mlp_num_fan_out_low" :max="127"
                                       size="small"></el-input-number>
                    </el-form-item>
                  </el-form>
                </div>

                <!-- CDSSM -->
                <div v-if="model_config.CDSSM.chosen" class="model_config_block">
                  <div class="divider"></div>
                  <el-tag style="font-size:16px;">CDSSM</el-tag>
                  <br>
                  <el-form label-width="130px" label-position="left" size="medium">
                    <el-form-item label="mlp_num_units">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.CDSSM.mlp_num_units_low" controls-position="right" :min="8"
                                       :max="model_config.CDSSM.mlp_num_units_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.CDSSM.mlp_num_units_high" controls-position="right"
                                       :min="model_config.CDSSM.mlp_num_units_low" :max="255"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_layers">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.CDSSM.mlp_num_layers_low" controls-position="right" :min="1"
                                       :max="model_config.CDSSM.mlp_num_layers_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.CDSSM.mlp_num_layers_high" controls-position="right"
                                       :min="model_config.CDSSM.mlp_num_layers_low" :max="5"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_fan_out">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.CDSSM.mlp_num_fan_out_low" controls-position="right"
                                       :min="4" :max="model_config.CDSSM.mlp_num_fan_out_high"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.CDSSM.mlp_num_fan_out_high" controls-position="right"
                                       :min="model_config.CDSSM.mlp_num_fan_out_low" :max="127"
                                       size="small"></el-input-number>
                    </el-form-item>
                  </el-form>
                </div>

                <!-- ARCII -->
                <div v-if="model_config.ARCII.chosen" class="model_config_block">
                  <div class="divider"></div>
                  <el-tag style="font-size:16px;">ARC-II</el-tag>
                  <br>
                  <el-form label-width="130px" label-position="left" size="medium">
                    <el-form-item label="dropout_rate">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.ARCII.dropout_rate_low" controls-position="right"
                                       :min="0.0" :max="model_config.ARCII.dropout_rate_high" :precision="1" :step="0.1"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.ARCII.dropout_rate_high" controls-position="right"
                                       :min="model_config.ARCII.dropout_rate_low" :max="0.8" :precision="1" :step="0.1"
                                       size="small"></el-input-number>
                    </el-form-item>
                    <el-form-item label="optimizer">
                      <el-checkbox-group v-model="model_config.ARCII.optimizer" :min="1">
                        <el-checkbox label="adam"></el-checkbox>
                        <el-checkbox label="rmsprop"></el-checkbox>
                        <el-checkbox label="adagrad"></el-checkbox>
                      </el-checkbox-group>
                    </el-form-item>
                  </el-form>
                </div>

                <!-- MVLSTM -->
                <div v-if="model_config.MVLSTM.chosen" class="model_config_block">
                  <div class="divider"></div>
                  <el-tag style="font-size:16px;">MVLSTM</el-tag>
                  <br>
                  <el-form label-width="130px" label-position="left" size="medium">
                    <el-form-item label="mlp_num_units">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.MVLSTM.mlp_num_units_low" controls-position="right" :min="8"
                                       :max="model_config.MVLSTM.mlp_num_units_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.MVLSTM.mlp_num_units_high" controls-position="right"
                                       :min="model_config.MVLSTM.mlp_num_units_low" :max="255"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_layers">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.MVLSTM.mlp_num_layers_low" controls-position="right" :min="1"
                                       :max="model_config.MVLSTM.mlp_num_layers_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.MVLSTM.mlp_num_layers_high" controls-position="right"
                                       :min="model_config.MVLSTM.mlp_num_layers_low" :max="5"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="mlp_num_fan_out">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.MVLSTM.mlp_num_fan_out_low" controls-position="right"
                                       :min="4" :max="model_config.MVLSTM.mlp_num_fan_out_high"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.MVLSTM.mlp_num_fan_out_high" controls-position="right"
                                       :min="model_config.MVLSTM.mlp_num_fan_out_low" :max="127"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="top_k">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.MVLSTM.top_k_low" controls-position="right"
                                       :min="4" :max="model_config.MVLSTM.top_k_high"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.MVLSTM.top_k_high" controls-position="right"
                                       :min="model_config.MVLSTM.top_k_low" :max="127"
                                       size="small"></el-input-number>
                    </el-form-item>
                  </el-form>
                </div>

                <!-- DUET -->
                <div v-if="model_config.DUET.chosen" class="model_config_block">
                  <div class="divider"></div>
                  <el-tag style="font-size:16px;">DUET</el-tag>
                  <br>
                  <el-form label-width="130px" label-position="left" size="medium">
                    <el-form-item label="dropout_rate">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.DUET.dropout_rate_low" controls-position="right"
                                       :min="0.0" :max="model_config.DUET.dropout_rate_high" :precision="1" :step="0.1"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.DUET.dropout_rate_high" controls-position="right"
                                       :min="model_config.DUET.dropout_rate_low" :max="0.8" :precision="1" :step="0.1"
                                       size="small"></el-input-number>
                    </el-form-item>
                  </el-form>
                </div>

                <!-- KNRM -->
                <div v-if="model_config.KNRM.chosen" class="model_config_block">
                  <div class="divider"></div>
                  <el-tag style="font-size:16px;">KNRM</el-tag>
                  <br>
                  <el-form label-width="130px" label-position="left" size="medium">
                    <el-form-item label="kernel_num">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.KNRM.kernel_num_low" controls-position="right" :min="5"
                                       :max="model_config.KNRM.kernel_num_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.KNRM.kernel_num_high" controls-position="right"
                                       :min="model_config.KNRM.kernel_num_low" :max="19"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="kernel_num">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.KNRM.sigma_low" controls-position="right"
                                       :min="0.01" :max="model_config.KNRM.sigma_high" :precision="2" :step="0.01"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.KNRM.sigma_high" controls-position="right"
                                       :min="model_config.KNRM.sigma_low" :max="0.19" :precision="2" :step="0.01"
                                       size="small"></el-input-number>
                    </el-form-item>
                  </el-form>
                </div>


                <!-- CONVKNRM -->
                <div v-if="model_config.CONVKNRM.chosen" class="model_config_block">
                  <div class="divider"></div>
                  <el-tag style="font-size:16px;">CONV-KNRM</el-tag>
                  <br>
                  <el-form label-width="130px" label-position="left" size="medium">
                    <el-form-item label="kernel_num">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.CONVKNRM.kernel_num_low" controls-position="right" :min="5"
                                       :max="model_config.CONVKNRM.kernel_num_high" size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.CONVKNRM.kernel_num_high" controls-position="right"
                                       :min="model_config.CONVKNRM.kernel_num_low" :max="19"
                                       size="small"></el-input-number>
                    </el-form-item>

                    <el-form-item label="kernel_num">
                      <el-tag>min</el-tag>
                      <el-input-number v-model="model_config.CONVKNRM.sigma_low" controls-position="right"
                                       :min="0.01" :max="model_config.CONVKNRM.sigma_high" :precision="2" :step="0.01"
                                       size="small"></el-input-number>
                      <el-tag style="margin-left: 20px;">max</el-tag>
                      <el-input-number v-model="model_config.CONVKNRM.sigma_high" controls-position="right"
                                       :min="model_config.CONVKNRM.sigma_low" :max="0.19" :precision="2" :step="0.01"
                                       size="small"></el-input-number>
                    </el-form-item>
                  </el-form>
                </div>
              </el-card>

              <!-- preprocess按钮逻辑：if (要自己上传&&还没有上传成功)||禁用按钮  则按钮禁用-->
              <el-button type="primary" icon="el-icon-view" style="margin-top:20px"
                         @mouseup.native="sendTrainHead()"
                         v-on:click="clickTrain()"
                         :disabled="(dataset_method && not_upload) || disabled_train_button">Train
              </el-button>
            </div>
          </el-scrollbar>
        </el-card>
      </el-col>
      <el-col :span="10">
        <el-card>
          <el-scrollbar style="height:100%;">
            <div style="text-align: left;">
              <el-tag style="font-size:16px;">chart</el-tag>
            </div>
            <tunechart v-bind:accuracydata="next_tune_data"
                       v-bind:min_height="tune_min_height"
                       v-bind:max_height="tune_max_height"
                       v-bind:x_axis="x_axis"
                       v-bind:line_color="line_color"
                       v-bind:line_num="line_num"
                       v-if="show_train_card"></tunechart>
            <tunechartdescription
              v-if="show_train_card && (lock_tag===3 || (lock_tag===0))"
              v-bind:selected_models="model_config">
            </tunechartdescription>

            <div class="divider"></div>
            <div style="height:50px;"></div>

            <div style="text-align: left;">
              <el-tag style="font-size:16px;">information</el-tag>
            </div>
            <el-table
              :data="model_data"
              stripe
              style="width: 100%">
              <el-table-column
                prop="ks"
                label="parameter">
              </el-table-column>
              <el-table-column
                prop="vs"
                label="value">
              </el-table-column>
            </el-table>

            <!-- <twovecs></twovecs>  -->
            <div v-if="!show_train_card">
              <el-input v-model="temp_val">
                <template slot="prepend">Matching Score</template>
              </el-input>
              <div style="height:30px"></div>
              <twovecs></twovecs>
            </div>
          </el-scrollbar>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
  import axios from 'axios'
  import TuneChart from './TuneChart'
  import MatchZooTab from '../MatchZooTab'
  import TuneChartDescription from './TuneChartDescription'
  import TwoVecs from '../TwoVecs'

  export default {
    name: 'Tune',
    data () {
      return {
        // 下面是选中的模型
        models: [
          {
            value: 'DRMM',
            label: 'DRMM'
          },
          {
            value: 'MatchPyramid',
            label: 'MatchPyramid'
          },
          {
            value: 'ARCI',
            label: 'ARC-I'
          },
          {
            value: 'DSSM',
            label: 'DSSM'
          },
          {
            value: 'CDSSM',
            label: 'CDSSM'
          },
          {
            value: 'ARCII',
            label: 'ARC-II'
          },
          {
            value: 'MVLSTM',
            label: 'MV-LSTM'
          },
          {
            value: 'DUET',
            label: 'DUET'
          },
          {
            value: 'KNRM',
            label: 'K-NRM'
          },
          {
            value: 'CONVKNRM',
            label: 'CONV-KNRM'
          }
        ],
        model_data: [],
        chosen_models: [],
        model_config: {
          DRMM: {
            chosen: false,
            mlp_num_units_low: 8,
            mlp_num_units_high: 255,
            mlp_num_layers_low: 1,
            mlp_num_layers_high: 5,
            mlp_num_fan_out_low: 4,
            mlp_num_fan_out_high: 127
          },
          MatchPyramid: {
            chosen: false
          },
          ARCI: {
            chosen: false,
            mlp_num_units_low: 8,
            mlp_num_units_high: 255,
            mlp_num_layers_low: 1,
            mlp_num_layers_high: 5,
            mlp_num_fan_out_low: 4,
            mlp_num_fan_out_high: 127,
            dropout_rate_low: 0,
            dropout_rate_high: 0.8
          },
          DSSM: {
            chosen: false,
            mlp_num_units_low: 8,
            mlp_num_units_high: 255,
            mlp_num_layers_low: 1,
            mlp_num_layers_high: 5,
            mlp_num_fan_out_low: 4,
            mlp_num_fan_out_high: 127
          },
          CDSSM: {
            chosen: false,
            mlp_num_units_low: 8,
            mlp_num_units_high: 255,
            mlp_num_layers_low: 1,
            mlp_num_layers_high: 5,
            mlp_num_fan_out_low: 4,
            mlp_num_fan_out_high: 127
          },
          ARCII: {
            chosen: false,
            dropout_rate_low: 0,
            dropout_rate_high: 0.8,
            optimizer: ['adam', 'rmsprop', 'adagrad']
          },
          MVLSTM: {
            chosen: false,
            mlp_num_units_low: 8,
            mlp_num_units_high: 255,
            mlp_num_layers_low: 1,
            mlp_num_layers_high: 5,
            mlp_num_fan_out_low: 4,
            mlp_num_fan_out_high: 127,
            top_k_low: 2,
            top_k_high: 99
          },
          DUET: {
            chosen: false,
            dropout_rate_low: 0,
            dropout_rate_high: 0.8
          },
          KNRM: {
            chosen: false,
            kernel_num_low: 5,
            kernel_num_high: 19,
            sigma_low: 0.01,
            sigma_high: 0.19
          },
          CONVKNRM: {
            chosen: false,
            kernel_num_low: 5,
            kernel_num_high: 19,
            sigma_low: 0.01,
            sigma_high: 0.19
          }
        },
        best_score: -1,
        color_mapping: {
          'DRMM': '#CC0000',
          'MatchPyramid': '#FF9900',
          'ARCI': '#663300',
          'DSSM': '#FFFF33',
          'CDSSM': '#9999FF',
          'ARCII': '#6600FF',
          'MVLSTM': '#009900',
          'DUET': '#006600',
          'KNRM': '#0099FF',
          'CONVKNRM': '#0033FF'
        },
        line_color: [],
        line_num: 3,
        // 下面是控制相关的变量
        activeNameBefore: '1',
        activeName: '1',
        train_id: '',
        end_train: false,
        show_train_card: true,
        temp_val: -1,
        disabled_preprocess_button: false,
        disabled_train_button: false,
        upload_first: false, // 第一个文件是否上传
        not_upload: true, // 两个文件没有全部上传
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
        tune_data: [],
        next_tune_data: [],
        tune_min_height: 0,
        tune_max_height: 1,
        x_axis: 5,
        epochs: 5,
        lock_tag: 0
      }
    },
    components: {
      'tunechart': TuneChart,
      'matchzootab': MatchZooTab,
      'tunechartdescription': TuneChartDescription,
      'twovecs': TwoVecs
    },
    methods: {
      change_models: function () {
        var mapping = {
          'DRMM': false,
          'MatchPyramid': false,
          'ARCI': false,
          'DSSM': false,
          'CDSSM': false,
          'ARCII': false,
          'MVLSTM': false,
          'DUET': false,
          'KNRM': false,
          'CONVKNRM': false
        }
        for (var i = 0; i < this.chosen_models.length; i++) {
          mapping[this.chosen_models[i]] = true
        }
        for (var key in mapping) {
          this.model_config[key].chosen = mapping[key]
        }
      },
      // 对于上传的文件进行检查
      uploadCheck: function (file) {
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
          else if (file.name === 'test.csv' && this.test_csv_upload === true) {
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
        var head_obj = {
          id: Math.random().toString(36).substr(2),
          train_id: this.train_id,
          epochs: this.epochs,
          parameter: this.model_config
        }
        axios.post('./tune/head', head_obj).then(function (response) {

        }).catch(function (err) {
          console.log('在train发送首请求之后出现了错误:' + err)
        })
      },
      // 点击Train按钮时触发的函数，设置计时器并定时向后端进行轮询
      clickTrain: function () {
        this.disabled_train_button = true
        var myself = this
        // 3s轮询一次后端，得到tuning的结果
        var timer = setInterval(getPreprocessData, 3000)
        var chart_timer = setInterval(setTrainData, 600)

        function getPreprocessData () {
          var obj = {
            id: Math.random().toString(36).substr(2),
            tune_id: myself.train_id,
            best_score: myself.best_score
          }
          axios.post('./tune/query', obj).then(function (response) {
            var dt = response.data
            console.log(dt)
            if (dt['update'] === true) {
              myself.model_data = []
              for (let key_name in dt['info']) {
                myself.model_data.push({
                  'ks': key_name,
                  'vs': dt['info'][key_name]
                })
              }
            }
            if (dt['state'] === 'run') {
              myself.tune_data = dt['chart']
              console.log('收到了tune轮询的结果')
            } else if (dt['state'] === 'end') {
              myself.tune_data = dt['chart']
              clearInterval(timer)
              myself.end_train = true
            }
          }).catch(function (err) {
            console.log('tune轮询时出错:' + err)
          })
        }

        function setTrainData () {
          console.log('tune data returned')
          var tag = true
          while (myself.tune_data.length > myself.next_tune_data.length) {
            myself.next_tune_data.push([])
          }
          for (var i = 0; i < myself.next_tune_data.length; i++) {
            if (myself.tune_data[i].length > myself.next_tune_data[i].length) {
              tag = false
              myself.next_tune_data[i].push(myself.tune_data[i][myself.next_tune_data[i].length])
            }
          }
          // 正确设置loss_chart的高度
          var maxv = -10000000, minv = 10000000
          for (var i = 0; i < myself.next_tune_data.length; i++) {
            for (var j = 0; j < myself.next_tune_data[i].length; j++) {
              maxv = Math.max(myself.next_tune_data[i][j].y, maxv)
              minv = Math.min(myself.next_tune_data[i][j].y, minv)
            }
          }

          myself.line_num = myself.next_tune_data.length
          if (myself.next_tune_data.length > myself.line_color.length) {
            // console.log('长度：', myself.next_tune_data.length, myself.line_color.length)
            for (var i = myself.line_color.length; i < myself.next_tune_data.length; i++) {
              if (myself.next_tune_data[i].length > 0) {
                let cur_model = myself.next_tune_data[i][0]['m']
                let cur_color = myself.color_mapping[cur_model]
                myself.line_color.push(cur_color)
              }
            }
          }

          if (myself.next_tune_data.length > 0 && myself.next_tune_data[0].length > myself.x_axis) {
            if (2 * myself.x_axis <= myself.epochs) {
              myself.x_axis = 2 * myself.x_axis
            }
            else {
              myself.x_axis = myself.epochs
            }
            console.log('！！！现在一共有' + myself.x_axis)
          }

          if (tag && myself.end_train === true) {
            clearInterval(chart_timer)
            myself.disabled_train_button = true
            myself.activeName = '2'
            myself.activeNameBefore = myself.activeName
          }
        }

      }
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
      // 设置卡片的高度
      var title = document.querySelector('#title')
      var titleHeight = parseInt(window.getComputedStyle(title, null).getPropertyValue('height'))
      console.log(document.querySelectorAll('.el-card__body'))
      document.querySelectorAll('.el-card__body')[0].style.height = winHeight + titleHeight - 28 - 140 + 'px'
      document.querySelectorAll('.el-card__body')[3].style.height = winHeight + titleHeight - 28 - 40 + 'px'
      // 去掉三个卡片最下面的自带的横向滚动条，因为三个滚动条太显眼了影响美观
      var scrollbar_list = document.querySelectorAll('.el-scrollbar__wrap')
      console.log(scrollbar_list)
      scrollbar_list[0].style.overflowX = 'hidden'
      scrollbar_list[1].style.overflowX = 'hidden'
      scrollbar_list[scrollbar_list.length - 1].style.overflowX = 'hidden'
      // configuration当中两个卡片的header的padding太大了，喧宾夺主的感觉，去掉
      var card_header = document.querySelectorAll('.el-card__header')
      for (var i = 1; i < 3; i++) {
        card_header[i].style.padding = '5px 20px'
      }
    }
  }
</script>

<style scoped>
  #title {
    font-size: 30px;
    text-align: center;
  }

  #dssm-demo {
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
  }

  .clearfix {
    text-align: left;
    font-size: 16px;
  }

  #models {
    margin: 30px;
  }

  #choose_models {
    text-align: left;
    font-size: 16px;
  }

  .divider {
    display: block;
    height: 1px;
    width: 100%;
    margin: 24px 0 10px 0;
    background-color: #dcdfe6;
    position: relative;
  }

  .model_config_block {
    text-align: left;
  }
</style>
