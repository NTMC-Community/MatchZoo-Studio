<template>
  <div id="arci-description">

      <el-row :gutter="20">
        <el-col :span="15">
          <el-card>
            <el-scrollbar style="height:100%;">
              <div class="description-content">
                <h2>1. Introduction</h2>
                <p>ARC-I is a representation-based model designed for semantic matching task. The model utilizes padding and mask method to deal the length variability. ARC-I uses word embeddings to capture semantic information instead of traditional one-hot encoding method, then uses convolution and max-pooling layers to get the sentence representation individually. In the final, it compares the representation for the two sentences with a multi-layer perceptron.</p>
                <h2>2. Structure</h2>
                <p>The overall structure of the ARC-I is shown in the figure. ARC-I employs a Siamese architecture to model two sentences. With encoded by pre-trained word embeddings, the model utilizes convolution and max-pooling layers to get sentence representation, and get the matching score between sentences by MLP.</p>
                <h2>3. Performances</h2>
                <p>The experiments of ARC-I are conducted on three different tasks, i.e. sentence completion, tweet matching and paraphrase identification. The results are listed as following.</p>
                <p>For sentence completion, the result is</p>
                <table class="result-data" cellspacing="0">
                  <caption>Table 1: Sentence Completion.</caption>
                  <tr>
                    <th class="top-line">Model</th>
                    <th class="top-line">P@1(%)</th>
                  </tr>
                  <tr>
                    <td class="top-line">Random Guess</td>
                    <td class="top-line">20.00</td>
                  </tr>
                  <tr>
                    <td>DEEPMATCH</td>
                    <td>32.5</td>
                  </tr>
                  <tr>
                    <td>WORDEMBED</td>
                    <td>37.63</td>
                  </tr>
                  <tr>
                    <td>SENMLP</td>
                    <td>36.14</td>
                  </tr>
                  <tr>
                    <td>SENNA + MLP</td>
                    <td>41.56</td>
                  </tr>
                  <tr>
                    <td>URAE + MLP</td>
                    <td>25.76</td>
                  </tr>
                  <tr>
                    <td class="top-line">ARC-I</td>
                    <td class="top-line">47.51</td>
                  </tr>
                  <tr>
                    <td class="bottom-line">ARC-II</td>
                    <td class="bottom-line text-weight">49.62</td>
                  </tr>
                </table>
                <p>For tweet matching, the result is</p>
                <table class="result-data" cellspacing="0">
                  <caption>Table 2: Tweet Matching.</caption>
                  <tr>
                    <th class="top-line">Model</th>
                    <th class="top-line">P@1(%)</th>
                  </tr>
                  <tr>
                    <td class="top-line">Random Guess</td>
                    <td class="top-line">20.00</td>
                  </tr>
                  <tr>
                    <td>DEEPMATCH</td>
                    <td>49.85</td>
                  </tr>
                  <tr>
                    <td>WORDEMBED</td>
                    <td>37.63</td>
                  </tr>
                  <tr>
                    <td>SENMLP</td>
                    <td>52.22</td>
                  </tr>
                  <tr>
                    <td>SENNA + MLP</td>
                    <td>56.48</td>
                  </tr>
                  <tr>
                    <td class="top-line">ARC-I</td>
                    <td class="top-line">59.18</td>
                  </tr>
                  <tr>
                    <td class="bottom-line">ARC-II</td>
                    <td class="bottom-line text-weight">61.95</td>
                  </tr>
                </table>
                <p>For paraphrase identification, the result is</p>
                <table class="result-data" cellspacing="0">
                  <caption>Table 3: The results on Paraphrase.</caption>
                  <tr>
                    <th class="top-line">Model</th>
                    <th class="top-line">Acc.(%)</th>
                    <th class="top-line">F1(%)</th>
                  </tr>
                  <tr>
                    <td class="top-line">Baseline</td>
                    <td class="top-line">66.5</td>
                    <td class="top-line">77.90</td>
                  </tr>
                  <tr>
                    <td>Rus et al. (2008)</td>
                    <td>70.6</td>
                    <td>80.5</td>
                  </tr>
                  <tr>
                    <td class="top-line">WORDEMBED</td>
                    <td class="top-line">68.7</td>
                    <td class="top-line">80.49</td>
                  </tr>
                  <tr>
                    <td>SENNA+MLP</td>
                    <td>68.4</td>
                    <td>79.7</td>
                  </tr>
                  <tr>
                    <td>SENMLP</td>
                    <td>68.4</td>
                    <td>79.5</td>
                  </tr>
                  <tr>
                    <td class="top-line">ARC-I</td>
                    <td class="top-line">69.6</td>
                    <td class="top-line">80.27</td>
                  </tr>
                  <tr>
                    <td class="bottom-line">ARC-II</td>
                    <td class="bottom-line">69.9</td>
                    <td class="bottom-line">80.91</td>
                  </tr>
                </table>
                <h2>4. Reference</h2>
                <p>[1] Shengxian Wan, Yanyan Lan, Jiafeng Guo, et al. A Deep Architecture for Semantic Matching with Multiple Positional Sentence Representations [C]. In Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence (AAAI), 2016.</p>
              </div>
            </el-scrollbar>
          </el-card>
        </el-col>
        <el-col :span="9">
          <el-scrollbar style="height:100%;">
            <div class="description-content">
              <el-card>
                <el-scrollbar style="height:100%;">
                  <img src="../../../assets/arci_architecture.png" width="100%">
                </el-scrollbar>
              </el-card>
            </div>
          </el-scrollbar>
        </el-col>
      </el-row>
    </div>
</template>

<script>
  export default {
    name: 'Description',
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
      document.querySelector('.el-card__body').style.height = winHeight - 60 - 20 - 40 - 10 - 70 + 'px'
      document.querySelectorAll('.el-card__body')[1].style.height = winHeight - 60 - 20 - 40 - 10 - 70 + 'px'
      var scrollbar_list = document.querySelectorAll('.el-scrollbar__wrap')
      // console.log(scrollbar_list)
      for (var i = 0; i < 4; i++) {
        scrollbar_list[i].style.overflowX = 'hidden'
      }
      //设置content区域的高度
      var content_block = document.querySelectorAll('.description-content')
      console.log(content_block)
      var content_height = winHeight - 60 + 'px'
      for (var i = 0; i < 2; i++) {
        content_block[i].style.height = content_height
      }
    }
  }
</script>

<style scoped>
  .description-content {
    text-align: left;
    font-size: 16px;
    line-height: 24px;
    font-weight: normal;
    font-family: "Lato", "proxima-nova", "Helvetica Neue", Arial, sans-serif;
  }

  .result-data {
    margin:auto;
    width: 60%;
    font-size: 15px;
  }

  .top-line {
    border-top: solid 1px black;
  }

  .bottom-line {
    border-bottom: solid 1px black;
  }

  .text-weight {
    font-weight: bold;
  }
</style>
