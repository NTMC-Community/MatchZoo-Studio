<template>
  <div id="cdssm-description">

      <el-row :gutter="20">
        <el-col :span="15">
          <el-card>
            <el-scrollbar style="height:100%;">
              <div class="description-content">
                <h2>1. Introduction</h2>
                <p>The CDSSM is an extension model based on DSSM. It uses the same token level encoding strategy, and build multi-layer convolution to get the semantic representation of sentences, instead of the DNN in DSSM. The output layer is the same as DSSM.</p>
                <h2>2. Structure</h2>
                <p>The overall structure of the CDSSM is shown in the figure. It employs a convolution layer at first to encode sentence with context information, which is different from the method in DSSM. In this paper, the kernel size (sliding window length) is set to be 3. The convolution layer encodes the window to a low dimension dense vector as DSSM does. After the final convolution layer, a dense transfer a 300-d vector to 128-d. The similarity between different documents can be compute by the cosine of their low dimension representation.</p>
                <h2>3. Performances</h2>
                <p>The experiments of CDSSM are conducted on the same dataset as DSSM, the result are provided in the following</p>
                <table class="result-data" cellspacing="0">
                  <caption>Table 5: Comparative results with the previous state of the art approaches.</caption>
                  <tr>
                    <th class="top-line">Models</th>
                    <th class="top-line">NDCG@1</th>
                    <th class="top-line">NDCG@3</th>
                    <th class="top-line">NDCG@10</th>
                  </tr>
                  <tr>
                    <td class="top-line">BM25</td>
                    <td class="top-line">0.305</td>
                    <td class="top-line">0.328</td>
                    <td class="top-line">0.388</td>
                  </tr>
                  <tr>
                    <td>ULM</td>
                    <td>0.304</td>
                    <td>0.327</td>
                    <td>0.385</td>
                  </tr>
                  <tr>
                    <td>PLSA(T=100)</td>
                    <td>0.305</td>
                    <td>0.335</td>
                    <td>0.402</td>
                  </tr>
                  <tr>
                    <td>PLSA(T=500)</td>
                    <td>0.308</td>
                    <td>0.337</td>
                    <td>0.402</td>
                  </tr>
                  <tr>
                    <td>LDA(T=100)</td>
                    <td>0.308</td>
                    <td>0.339</td>
                    <td>0.403</td>
                  </tr>
                  <tr>
                    <td>LDA(T=500)</td>
                    <td>0.310</td>
                    <td>0.339</td>
                    <td>0.403</td>
                  </tr>
                  <tr>
                    <td>BLTM</td>
                    <td>0.316</td>
                    <td>0.344</td>
                    <td>0.410</td>
                  </tr>
                  <tr>
                    <td>MRF</td>
                    <td>0.315</td>
                    <td>0.341</td>
                    <td>0.409</td>
                  </tr>
                  <tr>
                    <td>LCE</td>
                    <td>0.312</td>
                    <td>0.337</td>
                    <td>0.407</td>
                  </tr>
                  <tr>
                    <td>WTM</td>
                    <td>0.315</td>
                    <td>0.342</td>
                    <td>0.411</td>
                  </tr>
                  <tr>
                    <td>PTM(maxlen=3)</td>
                    <td>0.319</td>
                    <td>0.347</td>
                    <td>0.413</td>
                  </tr>
                  <tr>
                    <td>DSSM(J=4)</td>
                    <td>0.320</td>
                    <td>0.355</td>
                    <td>0.431</td>
                  </tr>
                  <tr>
                    <td>DSSM(J=50)</td>
                    <td>0.327</td>
                    <td>0.363</td>
                    <td>0.438</td>
                  </tr>
                  <tr>
                    <td>CLSM(J=4)</td>
                    <td>0.342</td>
                    <td>0.374</td>
                    <td>0.447</td>
                  </tr>
                  <tr>
                    <td class="bottom-line text-weight">CLSM(J=50)</td>
                    <td class="bottom-line text-weight">0.348</td>
                    <td class="bottom-line text-weight">0.379</td>
                    <td class="bottom-line text-weight">0.449</td>
                  </tr>
                </table>
                <p>The difference performance between CDSSM and DSSM is also shown in the following.</p>
                <table class="result-data" cellspacing="0">
                  <caption>Table 6: Comparative results of the CLSMs using different convolution window sizes.</caption>
                  <tr>
                    <th class="top-line">Models</th>
                    <th class="top-line">NDCG@1</th>
                    <th class="top-line">NDCG@3</th>
                    <th class="top-line">NDCG@10</th>
                  </tr>
                  <tr>
                    <td class="top-line">DSSM(J=50)</td>
                    <td class="top-line">0.327</td>
                    <td class="top-line">0.363</td>
                    <td class="top-line">0.438</td>
                  </tr>
                  <tr>
                    <td>CLSM(J=50) win=1</td>
                    <td>0.340</td>
                    <td>0.374</td>
                    <td>0.443</td>
                  </tr>
                  <tr>
                    <td>CLSM(J=50) win=3</td>
                    <td>0.348</td>
                    <td>0.379</td>
                    <td>0.449</td>
                  </tr>
                  <tr>
                    <td class="bottom-line">CLSM(J=50) win=5</td>
                    <td class="bottom-line">0.344</td>
                    <td class="bottom-line">0.376</td>
                    <td class="bottom-line">0.448</td>
                  </tr>
                </table>
                <h2>4. Reference</h2>
                <p>[1] Yelong Shen, Xiaodong He, et al. A Latent Semantic Model with Convolutional-Pooling Structure for Information Retrieval [C]. In Proceedings of the 23rd ACM International Conference on Conference on Information and Knowledge Management. ACM, 2014.</p>
              </div>
            </el-scrollbar>
          </el-card>
        </el-col>
        <el-col :span="9">
          <el-scrollbar style="height:100%;">
            <div class="description-content">
              <el-card>
                <el-scrollbar style="height:100%;">
                  <img src="../../../assets/cdssm_structure.png" width="100%">
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
