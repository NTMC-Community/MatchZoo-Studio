<template>
  <div id="knrm-description">

      <el-row :gutter="20">
        <el-col :span="15">
          <el-card>
            <el-scrollbar style="height:100%;">
              <div class="description-content">
                <h2>1. Introduction</h2>
                <p>The KNRM stands for the Kernel based Neural Ranking Model, which is a model published in SIGIR 2017. The paper title is “End-to-End Neural Ad-ho Ranking with Kernel Pooling”. Given a query and a set of documents, KNRM uses a translation matrix that models word-level similarities via word embeddings, a new kernel-pooling technique that uses kernels to extract multi-level soft match features, and a learning-to-rank layer that combines those features into the final ranking score.</p>
                <h2>2. Structure</h2>
                <p>The overall structure of the KNRM  is shown in the figure. The KNRM contains three components: translation model, kernel-pooling, and learning to rank. The translation model uses an embedding layer to map each word to an L-dimension embedding. The translation layer constructs a translation matrix. The Kernel-pooling layer uses kernels to convert word-word interactions in the translation matrix to query-document ranking features. The kernel pooling layer employs RBF kernel to map each query word’s row of the translation matrix, summarizing (pooling) it into a K-dimensional feature vector. The learning to rank layer utilizes a linear layer to learn the final relevance score.</p>
                <h2>3. Performances</h2>
                <p>The experiments of KNRM is conducted on search logs of Sougou.com, a major Chinese commercial search engine. The details of the collections are provided in Table 1.</p>
                <table class="result-data60" cellspacing="0">
                  <caption>Table 1: Training and testing dataset characteristics.</caption>
                  <tr>
                    <th class="top-line"></th>
                    <th class="top-line">Training</th>
                    <th class="top-line">Testing</th>
                  </tr>
                  <tr>
                    <td class="top-line">Queries</td>
                    <td class="top-line">95,229</td>
                    <td class="top-line">1,000</td>
                  </tr>
                  <tr>
                    <td>Documents Per Query</td>
                    <td>12.17</td>
                    <td>30.57</td>
                  </tr>
                  <tr>
                    <td>Search Sessions</td>
                    <td>31,201,876</td>
                    <td>4,103,230</td>
                  </tr>
                  <tr>
                    <td class="bottom-line">Vocbulary</td>
                    <td class="bottom-line">165,877</td>
                    <td class="bottom-line">19,079</td>
                  </tr>
                </table>
                <p>The overall results are summarized in Table 2.</p>
                <table class="result-data" cellspacing="0">
                  <caption>Table 2(a): Testing-SAME.</caption>
                  <tr>
                    <th class="top-line">Method</th>
                    <th class="top-line" colspan="2">NDCG@1</th>
                    <th class="top-line" colspan="2">NDCG@3</th>
                    <th class="top-line" colspan="2">NDCG@10</th>
                    <th class="top-line">W/T/L</th>
                  </tr>
                  <tr>
                    <td class="top-line">Lm</td>
                    <td class="top-line">0.1261</td>
                    <td class="top-line">-20.89%</td>
                    <td class="top-line">0.1648</td>
                    <td class="top-line">-26.46%</td>
                    <td class="top-line">0.2821</td>
                    <td class="top-line">-20.45%</td>
                    <td class="top-line">293/116/498</td>
                  </tr>
                  <tr>
                    <td>BM25</td>
                    <td>0.1422</td>
                    <td>-10.79%</td>
                    <td>0.1757</td>
                    <td>-21.60%</td>
                    <td>0.2868</td>
                    <td>-10.14%</td>
                    <td>299/125/483</td>
                  </tr>
                  <tr>
                    <td class="top-line">RankSVM</td>
                    <td class="top-line">0.1457</td>
                    <td class="top-line">-8.59%</td>
                    <td class="top-line">0.1905</td>
                    <td class="top-line">-14.99%</td>
                    <td class="top-line">0.3087</td>
                    <td class="top-line">-12.97%</td>
                    <td class="top-line">371/151/385</td>
                  </tr>
                  <tr>
                    <td>Coor-Ascent</td>
                    <td>0.1594</td>
                    <td>-</td>
                    <td>0.2241</td>
                    <td>-</td>
                    <td>0.3547</td>
                    <td>-</td>
                    <td>-/-/-</td>
                  </tr>
                  <tr>
                    <td class="top-line">Trans</td>
                    <td class="top-line">0.1347</td>
                    <td class="top-line">-15.50%</td>
                    <td class="top-line">0.1852</td>
                    <td class="top-line">-17.36%</td>
                    <td class="top-line">0.3147</td>
                    <td class="top-line">-11.28%</td>
                    <td class="top-line">318/140/449</td>
                  </tr>
                  <tr>
                    <td>DRMM</td>
                    <td>0.1366</td>
                    <td>-14.30</td>
                    <td>0.1902</td>
                    <td>-15.13</td>
                    <td>0.3150</td>
                    <td>-11.20%</td>
                    <td>318/132/457</td>
                  </tr>
                  <tr>
                    <td>CDSSM</td>
                    <td>0.1441</td>
                    <td>-9.59%</td>
                    <td>0.2014</td>
                    <td>-10.13%</td>
                    <td>0.3329</td>
                    <td>-6.14%</td>
                    <td>341/149/417</td>
                  </tr>
                  <tr>
                    <td class="top-line bottom-line">K-NRM</td>
                    <td class="top-line bottom-line text-weight">0.2642</td>
                    <td class="top-line bottom-line text-weight">+65.75%</td>
                    <td class="top-line bottom-line text-weight">0.3210</td>
                    <td class="top-line bottom-line text-weight">+43.25%</td>
                    <td class="top-line bottom-line text-weight">0.4277</td>
                    <td class="top-line bottom-line text-weight">+20.58%</td>
                    <td class="top-line bottom-line text-weight">447/153/307</td>
                  </tr>
                </table>
                <br>
                <table class="result-data" cellspacing="0">
                  <caption>Table 2(b): Testing-DIFF</caption>
                  <tr>
                    <th class="top-line">Method</th>
                    <th class="top-line" colspan="2">NDCG@1</th>
                    <th class="top-line" colspan="2">NDCG@3</th>
                    <th class="top-line" colspan="2">NDCG@10</th>
                    <th class="top-line">W/T/L</th>
                  </tr>
                  <tr>
                    <td class="top-line">Lm</td>
                    <td class="top-line">0.1852</td>
                    <td class="top-line">-11.34%</td>
                    <td class="top-line">0.1989</td>
                    <td class="top-line">-17.23%</td>
                    <td class="top-line">0.3270</td>
                    <td class="top-line">-13.38%</td>
                    <td class="top-line">369/50/513</td>
                  </tr>
                  <tr>
                    <td>BM25</td>
                    <td>0.1631</td>
                    <td>-21.92%</td>
                    <td>0.1894</td>
                    <td>-21.18%</td>
                    <td>0.3254</td>
                    <td>-13.81%</td>
                    <td>349/53/530</td>
                  </tr>
                  <tr>
                    <td class="top-line">RankSVM</td>
                    <td class="top-line">0.1700</td>
                    <td class="top-line">-18.62%</td>
                    <td class="top-line">0.2036</td>
                    <td class="top-line">-15.27%</td>
                    <td class="top-line">0.3519</td>
                    <td class="top-line">-6.78%</td>
                    <td class="top-line">380/75/477</td>
                  </tr>
                  <tr>
                    <td>Coor-Ascent</td>
                    <td>0.2089</td>
                    <td>-</td>
                    <td>0.2403</td>
                    <td>-</td>
                    <td>0.3775</td>
                    <td>-</td>
                    <td>-/-/-</td>
                  </tr>
                  <tr>
                    <td class="top-line">Trans</td>
                    <td class="top-line">0.1874</td>
                    <td class="top-line">-10.29%</td>
                    <td class="top-line">0.2127</td>
                    <td class="top-line">-11.50%</td>
                    <td class="top-line">0.3454</td>
                    <td class="top-line">-8.51%</td>
                    <td class="top-line">385/68/479</td>
                  </tr>
                  <tr>
                    <td>DRMM</td>
                    <td>0.2068</td>
                    <td>-1.00%</td>
                    <td>0.2491</td>
                    <td>-3.67%</td>
                    <td>0.3809</td>
                    <td>+0.91%</td>
                    <td>430/66/436</td>
                  </tr>
                  <tr>
                    <td>CDSSM</td>
                    <td>0.1846</td>
                    <td>-10.77%</td>
                    <td>0.2358</td>
                    <td>-1.86%</td>
                    <td>0.3557</td>
                    <td>-5.79%</td>
                    <td>391/65/476</td>
                  </tr>
                  <tr>
                    <td class="top-line bottom-line">K-NRM</td>
                    <td class="top-line bottom-line text-weight">0.2984</td>
                    <td class="top-line bottom-line text-weight">+42.84%</td>
                    <td class="top-line bottom-line text-weight">0.3092</td>
                    <td class="top-line bottom-line text-weight">+28.26%</td>
                    <td class="top-line bottom-line text-weight">0.4201</td>
                    <td class="top-line bottom-line text-weight">+11.28%</td>
                    <td class="top-line bottom-line text-weight">474/63/395</td>
                  </tr>
                </table>
                <h2>4. Reference</h2>
                <p>[1] Chenyan Xiong, Zhuyun Dai, et al. End-to-End Neural Ad-hoc Ranking with Kernel Pooling[J]. arXiv preprint arXiv:1706.06613, 2017.</p>
              </div>
            </el-scrollbar>
          </el-card>
        </el-col>
        <el-col :span="9">
          <el-scrollbar style="height:100%;">
            <div class="description-content">
              <el-card>
                <el-scrollbar style="height:100%;">
                  <img src="../../../assets/knrm_sturcture.png" width="100%">
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

  .result-data {
    margin:auto;
    width: 95%;
    font-size: 15px;
  }

  .result-data60 {
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
