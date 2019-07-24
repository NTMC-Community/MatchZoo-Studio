<template>
  <div id="conv_knrm-description">

      <el-row :gutter="20">
        <el-col :span="15">
          <el-card>
            <el-scrollbar style="height:100%;">
              <div class="description-content">
                <h2>1. Introduction</h2>
                <p>The Conv-KNRM stands for the convolutional kernel-based neural ranking model, which is published WSDM 2018. The paper title is “Convolutional Neural Networks for Soft-Matching N-Grams in Ad-hoc Search”. The Conv-KNRM uses convolutional neural networks to represent n-grams of various lengths and soft matches them in a unified embedding space. The n-gram soft matches are then utilized by the kernel pooling and learning-to-rank layers to generate the final ranking score.</p>
                <h2>2. Structure</h2>
                <p>The overall structure of the Conv-KNRM  is shown in the figure. Given a query and a document, Conv-KNRM embeds their words by a word embedding layer, composes n-grams with a CNN layer, and cross-matches query n-grams and document n-grams of variant lengths to the translation matrices. Firstly, the word embedding layer maps each word to an L-dimension continuous vector. Secondly, the convolutional layer applies convolution filters to compose n-grams from the text. A convolution filter slide over the text like a sliding window. Thirdly, the cross-match layer matches query n-grams and document n-grams of different lengths. Then, as is the same with KNRM model, Conv-KNRM uses the kernel-pooling technique and a learning-to-rank layer to calculate the ranking score using the n-gram translations.</p>
                <h2>3. Performances</h2>
                <p>The experiments of Conv-KNRM is conducted on two search logs in different languages (Sougou, Bing), and a TREC dataset (ClueWeb09-B). The details of the two collections are provided in Table 1.</p>
                <table class="result-data60" cellspacing="0">
                  <caption>Table 1: Training and testing dataset characteristics.</caption>
                  <tr>
                    <td rowspan="2" class="top-line right-line"></td>
                    <td colspan="2" class="top-line right-line text-weight">Sogou-Log</td>
                    <td colspan="2" class="top-line text-weight">Bing-Log</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line text-weight">Training</td>
                    <td class="top-line right-line text-weight">Testing</td>
                    <td class="top-line right-line text-weight">Training</td>
                    <td class="top-line text-weight">Testing</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line">Language</td>
                    <td colspan="2" class="top-line right-line">Chinese</td>
                    <td colspan="2" class="top-line">English</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line">Fields</td>
                    <td colspan="2" class="top-line right-line">Title</td>
                    <td colspan="2" class="top-line">Title, Snippet</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line">Queries</td>
                    <td class="top-line right-line">95,229</td>
                    <td class="top-line right-line">1,000</td>
                    <td class="top-line right-line">99,043</td>
                    <td class="top-line">1,000</td>
                  </tr>
                  <tr>
                    <td class="right-line">Docs Per Query</td>
                    <td class="right-line">12.17</td>
                    <td class="right-line">30.50</td>
                    <td class="right-line">50</td>
                    <td>50</td>
                  </tr>
                  <tr>
                    <td class="right-line">Search Sessions</td>
                    <td class="right-line">31M</td>
                    <td class="right-line">4.1M</td>
                    <td class="right-line">2.10M</td>
                    <td>0.14M</td>
                  </tr>
                  <tr>
                    <td class="bottom-line right-line">Vocabulary Size</td>
                    <td class="bottom-line right-line">165,877</td>
                    <td class="bottom-line right-line">19,079</td>
                    <td class="bottom-line right-line">131,225</td>
                    <td class="bottom-line ">41,940</td>
                  </tr>
                </table>
                <p>The overall results are summarized in Table 2.</p>
                <table class="result-data" cellspacing="0">
                  <caption>Table 2(a): Ranking accuracy of Conv-KNRM and baseline methods.</caption>
                  <tr>
                    <td rowspan="3" class="top-line right-line text-weight">Method</td>
                    <td colspan="3" class="top-line right-line text-weight">Sougou-Log</td>
                    <td colspan="3" class="top-line text-weight">Bing-Log</td>
                  </tr>
                  <tr>
                    <td colspan="2" class="top-line right-line text-weight">Testing-SAME</td>
                    <td class="top-line right-line text-weight">Testing-Raw</td>
                    <td colspan="2" class="top-line right-line text-weight">Testing-SAME</td>
                    <td class="top-line text-weight">Testing-Raw</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line text-weight">NDCG@1</td>
                    <td class="top-line right-line text-weight">NDCG@10</td>
                    <td class="top-line right-line text-weight">MRR</td>
                    <td class="top-line right-line text-weight">NDCG@1</td>
                    <td class="top-line right-line text-weight">NDCG@10</td>
                    <td class="top-line text-weight">MRR</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line">BM25</td>
                    <td class="top-line">0.142</td>
                    <td class="top-line">0.287</td>
                    <td class="top-line right-line">0.228</td>
                    <td class="top-line">0.043</td>
                    <td class="top-line">0.123</td>
                    <td class="top-line">0.102</td>
                  </tr>
                  <tr>
                    <td class="right-line">RankSVM</td>
                    <td>0.146</td>
                    <td>0.309</td>
                    <td class="right-line">0.224</td>
                    <td>0.128</td>
                    <td>0.266</td>
                    <td>0.207</td>
                  </tr>
                  <tr>
                    <td class="right-line">Coor-Ascent</td>
                    <td>0.169</td>
                    <td>0.355</td>
                    <td class="right-line">0.242</td>
                    <td>0.142</td>
                    <td>0.268</td>
                    <td>0.208</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line">DRMM</td>
                    <td class="top-line">0.137</td>
                    <td class="top-line">0.315</td>
                    <td class="top-line right-line">0.234</td>
                    <td class="top-line">0.137</td>
                    <td class="top-line">0.247</td>
                    <td class="top-line">0.200</td>
                  </tr>
                  <tr>
                    <td class="right-line">CDSSM</td>
                    <td>0.144</td>
                    <td>0.333</td>
                    <td class="right-line">0.232</td>
                    <td>0.156</td>
                    <td>0.273</td>
                    <td>0.212</td>
                  </tr>
                  <tr>
                    <td class="right-line">MP</td>
                    <td>0.218</td>
                    <td>0.379</td>
                    <td class="right-line">0.240</td>
                    <td>0.182</td>
                    <td>0.301</td>
                    <td>0.244</td>
                  </tr>
                  <tr>
                    <td class="right-line">K-NRM</td>
                    <td>0.264</td>
                    <td>0.428</td>
                    <td class="right-line">0.338</td>
                    <td>0.208</td>
                    <td>0.334</td>
                    <td>0.265</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line bottom-line">Conv-KNRM</td>
                    <td class="top-line bottom-line text-weight">0.336</td>
                    <td class="top-line bottom-line text-weight">0.481</td>
                    <td class="top-line right-line bottom-line text-weight">0.358</td>
                    <td class="top-line bottom-line text-weight">0.300</td>
                    <td class="top-line bottom-line text-weight">0.437</td>
                    <td class="top-line bottom-line text-weight">0.354</td>
                  </tr>
                </table>
                <br>
                <table class="result-data" cellspacing="0">
                  <caption>Table 2(b): Performance on ClueWeb09-B using domain adaptation.</caption>
                  <tr>
                    <td rowspan="2" class="top-line right-line text-weight">Method</td>
                    <td colspan="7" class="top-line text-weight">ClueWeb09-B</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line text-weight">NDCG@1</td>
                    <td class="top-line right-line text-weight">ERR@1</td>
                    <td class="top-line right-line text-weight">NDCG@10</td>
                    <td class="top-line right-line text-weight">ERR@10</td>
                    <td class="top-line right-line text-weight">NDCG@20</td>
                    <td class="top-line right-line text-weight">ERR@20</td>
                    <td class="top-line text-weight">W/T/L</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line">Indri</td>
                    <td class="top-line">0.239</td>
                    <td class="top-line">0.062</td>
                    <td class="top-line">0.229</td>
                    <td class="top-line">0.130</td>
                    <td class="top-line">0.236</td>
                    <td class="top-line">0.139</td>
                    <td class="top-line">68/31/101</td>
                  </tr>
                  <tr>
                    <td class="right-line">Galago-SDM</td>
                    <td>0.219</td>
                    <td>0.053</td>
                    <td>0.238</td>
                    <td>0.130</td>
                    <td>0.250</td>
                    <td>0.139</td>
                    <td>63/39/98</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line">RankSVM</td>
                    <td class="top-line">0.236</td>
                    <td class="top-line">0.064</td>
                    <td class="top-line">0.256</td>
                    <td class="top-line">0.146</td>
                    <td class="top-line">0.263</td>
                    <td class="top-line">0.154</td>
                    <td class="top-line">82/47/71</td>
                  </tr>
                  <tr>
                    <td class="right-line">Coor-Ascent</td>
                    <td>0.255</td>
                    <td>0.071</td>
                    <td>0.268</td>
                    <td>0.154</td>
                    <td>0.268</td>
                    <td>0.162</td>
                    <td>-/-/-</td>
                  </tr>
                  <tr>
                    <td class="right-line">DRMM+SDM</td>
                    <td>0.215</td>
                    <td>0.049</td>
                    <td>0.261</td>
                    <td>0.136</td>
                    <td>0.243</td>
                    <td>0.138</td>
                    <td>66/34/100</td>
                  </tr>
                  <tr>
                    <td class="top-line right-line">K-NRM</td>
                    <td class="top-line">0.235</td>
                    <td class="top-line">0.057</td>
                    <td class="top-line">0.264</td>
                    <td class="top-line">0.140</td>
                    <td class="top-line">0.269</td>
                    <td class="top-line">0.149</td>
                    <td class="top-line">69/42/89</td>
                  </tr>
                  <tr>
                    <td class="right-line">Conv-KNRM-exact</td>
                    <td>0.231</td>
                    <td>0.064</td>
                    <td>0.263</td>
                    <td>0.146</td>
                    <td>0.270</td>
                    <td>0.155</td>
                    <td>78/42/80</td>
                  </tr>
                  <tr>
                    <td class="right-line bottom-line">Conv-KNRM</td>
                    <td class="bottom-line text-weight">0.294</td>
                    <td class="bottom-line text-weight">0.093</td>
                    <td class="bottom-line text-weight">0.289</td>
                    <td class="bottom-line text-weight">0.172</td>
                    <td class="bottom-line text-weight">0.287</td>
                    <td class="bottom-line text-weight">0.181</td>
                    <td class="bottom-line text-weight">88/38/74</td>
                  </tr>
                </table>
                <h2>4. Reference</h2>
                <p>[1] Zhuyun Dai, Chenyan Xiong, et al. Convolutional Neural Networks for Soft-Matching N-Grams in Ad-hoc Search[C]. In Proceedings of the 11th ACM International Conference on Web Search and Data Mining. ACM, 2018.</p>
              </div>
            </el-scrollbar>
          </el-card>
        </el-col>
        <el-col :span="9">
          <el-scrollbar style="height:100%;">
            <div class="description-content">
              <el-card>
                <el-scrollbar style="height:100%;">
                  <img src="../../../assets/convknrm.png" width="100%">
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
      // console.log(document.querySelectorAll('.el-scrollbar__wrap'))
      var scrollbar_list = document.querySelectorAll('.el-scrollbar__wrap')
      console.log(scrollbar_list)
      for (var i = 0; i < 4; i++) {
        scrollbar_list[i].style.overflowX = 'hidden'
      }
      //设置content区域的高度
      var content_block = document.querySelectorAll('.description-content')
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

  .result-data60 {
    margin:auto;
    width: 60%;
    font-size: 15px;
  }

  .result-data {
    margin:auto;
    width: 100%;
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
  .right-line{
    border-right: solid 1px black;
  }
</style>
