<template>
  <div id="duet-description">

      <el-row :gutter="20">
        <el-col :span="15">
          <el-card>
            <el-scrollbar style="height:100%;">
              <div class="description-content">
                <h2>1. Introduction</h2>
                <p>The DUET model is compose by two separate deep neural networks, one that matches the query and the document using a local representation which is always captured by exact term matches, and another that matches the query and the document using learned distributed representations which is always captured in a latent semantic space. The two DNNs  are jointly trained as part of a single neural network, so it is named as a ‘duet’ architecture because the two networks co-operate to achieve a common goal.</p>
                <h2>2. Structure</h2>
                <p>The overall structure of the DUET is shown in the figure. The DUET model projects the query and the document text into an embedding space before matching. The final score under the DUET setup is the sum of scores from the local and the distributed networks. The local model estimates document relevance based on patterns of exact matches of query terms in the document. It generates a interaction matrix which captures every exact match (and position) of query terms in the document. The interaction matrix is first passed through a convolutional layer and then passed through two fully-connected layers, a dropout layer, and a final fully-connected layer that produces a single real-valued output.The distributed model learns dense lower-dimensional vector representations of the query and the document text, and then computes the positional similarity between them in the learnt embedding space. Instead of a one-hot encoding of terms, as in the local model, it use a character n-graph based representation of each term in the query and document. The character-based input then pass through convolution step and then conduct a max-pooling step. The output of the max-pooling layer for the query is then passed through a fully-connected layer. For the document, the output is operated on by another convolutional layer. Finally, it conduct the element-wise or Hadamard product between the embedded document matrix and the extended or broadcasted query embedding. After this, we pass the matrix through fully connected layers, and a dropout layer until we arrive at a single score.</p>
                <h2>3. Performances</h2>
                <p>The experiments of DUET is conducted on a randomly sampled from Bing ‘s search logs from a period between January, 2012 and September, 2014. The details of the dataset are provided in Table 1.</p>
                <table class="result-data" cellspacing="0">
                  <caption>Table 1: Statistics of the three test sets randomly sampled from Bing's search logs.</caption>
                  <tr>
                    <th class="top-line"></th>
                    <th class="top-line">queries</th>
                    <th class="top-line">documents</th>
                    <th class="top-line">documents/query</th>
                  </tr>
                  <tr>
                    <td class="top-line">training</td>
                    <td class="top-line">199,753</td>
                    <td class="top-line">998,765</td>
                    <td class="top-line">5</td>
                  </tr>
                  <tr>
                    <td>weighted</td>
                    <td>7,741</td>
                    <td>171,302</td>
                    <td>24.9</td>
                  </tr>
                  <tr>
                    <td class="bottom-line">unweighted</td>
                    <td class="bottom-line">6,808</td>
                    <td class="bottom-line">71,722</td>
                    <td class="bottom-line">10.6</td>
                  </tr>
                </table>
                <p>The overall results are summarized in Table 2.</p>
                <table class="result-data" cellspacing="0">
                  <caption>Table 2(a): weighted</caption>
                  <tr>
                    <th class="top-line"></th>
                    <th class="top-line">NDCG@1</th>
                    <th class="top-line">NDCG@10</th>
                  </tr>
                  <tr>
                    <td class="top-line text-weight">Non-neural baselines</td>
                    <td class="top-line"></td>
                    <td class="top-line"></td>
                  </tr>
                  <tr>
                    <td>LSA</td>
                    <td>22.4</td>
                    <td>44.2</td>
                  </tr>
                  <tr>
                    <td>BM25</td>
                    <td>24.2</td>
                    <td>45.5</td>
                  </tr>
                  <tr>
                    <td>DM</td>
                    <td>24.7</td>
                    <td>46.2</td>
                  </tr>
                  <tr>
                    <td>QL</td>
                    <td>24.6</td>
                    <td>46.3</td>
                  </tr>
                  <tr>
                    <td class="top-line text-weight">Neural baselines</td>
                    <td class="top-line"></td>
                    <td class="top-line"></td>
                  </tr>
                  <tr>
                    <td>DRMM</td>
                    <td>24.3</td>
                    <td>45.2</td>
                  </tr>
                  <tr>
                    <td>DSSM</td>
                    <td>25.8</td>
                    <td>48.2</td>
                  </tr>
                  <tr>
                    <td>CDSSM</td>
                    <td>27.3</td>
                    <td>48.2</td>
                  </tr>
                  <tr>
                    <td>DESM</td>
                    <td>25.4</td>
                    <td>48.3</td>
                  </tr>
                  <tr>
                    <td class="top-line text-weight">Our models</td>
                    <td class="top-line"></td>
                    <td class="top-line"></td>
                  </tr>
                  <tr>
                    <td>Local model</td>
                    <td>24.6</td>
                    <td>45.1</td>
                  </tr>
                  <tr>
                    <td>Distributed model</td>
                    <td>28.6</td>
                    <td>50.5</td>
                  </tr>
                  <tr>
                    <td class="bottom-line">Duet model</td>
                    <td class="bottom-line text-weight">32.2</td>
                    <td class="bottom-line text-weight">53.0</td>
                  </tr>
                </table>
                <br>
                <table class="result-data" cellspacing="0">
                  <caption>Table 2(b): unweighted</caption>
                  <tr>
                    <th class="top-line"></th>
                    <th class="top-line">NDCG@1</th>
                    <th class="top-line">NDCG@10</th>
                  </tr>
                  <tr>
                    <td class="top-line text-weight">Non-neural baselines</td>
                    <td class="top-line"></td>
                    <td class="top-line"></td>
                  </tr>
                  <tr>
                    <td>LSA</td>
                    <td>31.9</td>
                    <td>62.7</td>
                  </tr>
                  <tr>
                    <td>BM25</td>
                    <td>34.9</td>
                    <td>63.3</td>
                  </tr>
                  <tr>
                    <td>DM</td>
                    <td>35.0</td>
                    <td>63.4</td>
                  </tr>
                  <tr>
                    <td>QL</td>
                    <td>34.9</td>
                    <td>63.4</td>
                  </tr>
                  <tr>
                    <td class="top-line text-weight">Neural baselines</td>
                    <td class="top-line"></td>
                    <td class="top-line"></td>
                  </tr>
                  <tr>
                    <td>DRMM</td>
                    <td>35.6</td>
                    <td>65.1</td>
                  </tr>
                  <tr>
                    <td>DSSM</td>
                    <td>34.3</td>
                    <td>64.4</td>
                  </tr>
                  <tr>
                    <td>CDSSM</td>
                    <td>34.3</td>
                    <td>64.0</td>
                  </tr>
                  <tr>
                    <td>DESM</td>
                    <td>35.0</td>
                    <td>64.7</td>
                  </tr>
                  <tr>
                    <td class="top-line text-weight">Our models</td>
                    <td class="top-line"></td>
                    <td class="top-line"></td>
                  </tr>
                  <tr>
                    <td>Local model</td>
                    <td>35.0</td>
                    <td>64.4</td>
                  </tr>
                  <tr>
                    <td>Distributed model</td>
                    <td>35.2</td>
                    <td>64.9</td>
                  </tr>
                  <tr>
                    <td class="bottom-line">Duet model</td>
                    <td class="bottom-line text-weight">37.8</td>
                    <td class="bottom-line text-weight">66.4</td>
                  </tr>
                </table>
                <h2>4. Reference</h2>
                <p>
                  [1] Bhaskar Mitra, Fernando Diaz, Nick Craswell. Learning to Match using Local and Distributed Representations of Text for Web Search [C].

                </p>
              </div>
            </el-scrollbar>
          </el-card>
        </el-col>
        <el-col :span="9">
          <el-scrollbar style="height:100%;">
            <div class="description-content">
              <el-card>
                <el-scrollbar style="height:100%;">
                  <img src="../../../assets/duet_structure.jpg" width="100%">
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
