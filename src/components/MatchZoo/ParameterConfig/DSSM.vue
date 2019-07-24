<template>
  <div id="dssm">
    <el-row>
      <el-col :span="12">
        <el-form label-width="130px" label-position="left">
            <el-tooltip class="item" effect="dark" content="Right Top 提示文字" placement="right-start">
              <el-form-item label="input_shapes">
                <el-input-number v-model="input_shapes" :min="0" :max="500"></el-input-number>
              </el-form-item>
            </el-tooltip>

            <el-tooltip class="item" effect="dark" content="Right Top 提示文字" placement="right-start">
              <el-form-item label="dim_fan_out">
                <el-input-number v-model="dim_fan_out" :min="0" :max="500"></el-input-number>
              </el-form-item>
            </el-tooltip>

            <el-tooltip class="item" effect="dark" content="Right Top 提示文字" placement="right-start">
              <el-form-item label="dim_hidden">
                <el-input-number v-model="dim_hidden" :min="0" :max="1000"></el-input-number>
              </el-form-item>
            </el-tooltip>

            <el-tooltip class="item" effect="dark" content="Right Top 提示文字" placement="right-start">
              <el-form-item label="num_hidden_layers">
                <el-input-number v-model="num_hidden_layers" :min="1" :max="10" ></el-input-number>
              </el-form-item>
            </el-tooltip>
        </el-form>
      </el-col>

      <el-col :span="11">
        <el-form label-width="130px" label-position="left">
            <el-tooltip class="item" effect="dark" content="Right Top 提示文字很长很长很长很长很长很长很长很长很长" placement="right-start">
              <el-form-item label="w_initializer">
                <el-select v-model="w_initializer">
                  <el-option
                    v-for="item in w_options"
                    :key="item.label"
                    :label="item.label"
                    :value="item.label">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-tooltip>

            <el-tooltip class="item" effect="dark" content="Right Top 提示文字" placement="right-start">
              <el-form-item label="b_initializer">
                <el-select v-model="b_initializer">
                  <el-option
                    v-for="item in b_options"
                    :key="item.label"
                    :label="item.label"
                    :value="item.label">
                  </el-option>
                </el-select>
              </el-form-item>
            </el-tooltip>

            <el-tooltip class="item" effect="dark" content="Right Top 提示文字" placement="right-start">
              <el-form-item label="activation_hidden">
                <el-select v-model="activation_hidden">
                  <el-option
                    v-for="item in activation_options"
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
  </div>
</template>

<script>
  export default {
    name: 'DSSM',
    data () {
      return {
        input_shapes: 300,
        w_initializer: 'glorot_normal',
        b_initializer: 'zeros',
        dim_fan_out: 128,
        dim_hidden: 300,
        activation_hidden: 'tanh',
        num_hidden_layers: 2,
        w_options: [
          {
            label: 'glorot_normal'
          },
          {
            label: 'test_value'
          }
        ],
        b_options: [
          {
            label: 'zeros'
          },
          {
            label: 'random_value'
          }
        ],
        activation_options: [
          {
            label: 'tanh'
          },
          {
            label: 'relu'
          }
        ]
      }
    },
    mounted: function () {
      // document.getElementById('dssm').style.width = '60%'
    },
    methods: {
      get_data () {
        return {
          model_name: 'DSSM',
          input_shapes: this.input_shapes,
          w_initializer: this.w_initializer,
          b_initializer: this.b_initializer,
          dim_fan_out: this.dim_fan_out,
          dim_hidden: this.dim_hidden,
          activation_hidden: this.activation_hidden,
          num_hidden_layers: this.num_hidden_layers
        }
      }
    }
  }
</script>

<style scoped>
  #dssm {
    text-align: left;
  }
</style>
