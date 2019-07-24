<template>
  <div id="dssm-description">

      <el-row :gutter="20">
        <el-col :span="15">
          <el-card>
            <el-scrollbar style="height:100%;">
              <div class="description-content">
                <h2>1. Introduction</h2>
                <p>DSSM stands for Deep Structured Semantic Model, or more general, Deep Semantic Similarity Model. It is developed for representing text strings (sentences, queries, predicates, entity mentions, etc.) in a continuous semantic space and modeling semantic similarity between two text strings (e.g., Sent2Vec) by the MSR Deep Learning Technology Center(DLTC).</p>
                <p>DSSM uses a deep neural network (DNN) to rank a set of documents for a given query as follows. First, a non-linear projection is performed to map the query and the documents to a common semantic space. Then, the relevance of each document given the query is calculated as the cosine similarity between their vectors in that semantic space. The neural network models are discriminatively trained using the clickthrough data such that the conditional likelihood of the clicked document given the query is maximized. Different from the previous latent semantic models that are learned in an unsupervised fashion, the models are optimized directly for Web document ranking, and thus give superior performance. Furthermore, to deal with large vocabularies, researchers propose the so-called word hashing method, through which the high-dimensional term vectors of queries or documents are projected to low-dimensional letter based n-gram vectors with little information loss.</p>
                <h2>2. Structure</h2>
                <p>The figure on the right is an illustration of the DSSM. It uses a DNN to map a 500K sparse feature vector to a dense vector in 128 dimensions. The original input vector x contains 500k dimensions, which are reduced to 30k by word hashing method. Then, as we can see in the figure, 3 layers of non-linear projections are performed. A 30k * 300 weight matrix W2 and a bias b2 with 300 dimensions is used to transform the first layer with 30k units to the second layer with 300 units. And so on, the second layer with 300 units is transformed to the third layer with 300 units, and the third layer is then transformed to the final result vector y with 128 dimensions.</p>
                <h2>3. Performances</h2>
                <p>researchers have evaluated the retrieval models on a large-scale real world data set, called the evaluation data set henceforth. The evaluation data set contains 16,510 English queries sampled from one-year query log files of a commercial search engine. On average, each query is associated with 15 Web documents (URLs). Each query-title pair has a relevance label. The label is human generated and is on a 5-level relevance scale, 0 to 4, where level 4 means that the document is the most relevant to query Q and 0 means D is not relevant to Q. All the queries and documents are preprocessed such that the text is white-space tokenized and lowercased, numbers are retained, and no stemming/inflection is performed. The performance of all ranking models researchers have evaluated has been measured by mean Normalized Discounted Cumulative Gain (NDCG) , and NDCG scores will be reported at truncation levels 1, 3, and 10.</p>
                <p>The main results of experiments are summarized in the following table, where researchers compared the best version of the DSSM (Row 12) with three sets of baseline models. The first set of baselines includes a couple of widely used lexical matching methods such as TF-IDF (Row 1) and BM25 (Row 2). The second is a word translation model (WTM in Row 3) which is intended to directly address the query-document language discrepancy problem by learning a lexical mapping between query words and document words. The third includes a set of state-of-the-art latent semantic models which are learned either on documents only in an unsupervised manner (LSA, PLSA, DAE as in Rows 4 to 6) or on clickthrough data in a supervised way (BLTM-PR, DPM, as in Rows 7 and 8).</p>
                <table class="result-data" cellspacing="0">
                  <tr>
                    <th class="top-line">Models</th>
                    <th class="top-line">NDCG@1</th>
                    <th class="top-line">NDCG@3</th>
                    <th class="top-line">NDCG@10</th>
                  </tr>
                  <tr>
                    <td class="top-line">TF-IDF</td>
                    <td class="top-line">0.319</td>
                    <td class="top-line">0.382</td>
                    <td class="top-line">0.462</td>
                  </tr>
                  <tr>
                    <td>BM25</td>
                    <td>0.308</td>
                    <td>0.373</td>
                    <td>0.455</td>
                  </tr>
                  <tr>
                    <td>WTM</td>
                    <td>0.332</td>
                    <td>0.400</td>
                    <td>0.478</td>
                  </tr>
                  <tr>
                    <td>LSA</td>
                    <td>0.298</td>
                    <td>0.372</td>
                    <td>0.455</td>
                  </tr>
                  <tr>
                    <td>PLSA</td>
                    <td>0.295</td>
                    <td>0.371</td>
                    <td>0.456</td>
                  </tr>
                  <tr>
                    <td>DAE</td>
                    <td>0.310</td>
                    <td>0.377</td>
                    <td>0.459</td>
                  </tr>
                  <tr>
                    <td>BLTM-PR</td>
                    <td>0.337</td>
                    <td>0.403</td>
                    <td>0.480</td>
                  </tr>
                  <tr>
                    <td>DPM</td>
                    <td>0.329</td>
                    <td>0.401</td>
                    <td>0.479</td>
                  </tr>
                  <tr>
                    <td class="top-line">DNN</td>
                    <td class="top-line">0.342</td>
                    <td class="top-line">0.410</td>
                    <td class="top-line">0.486</td>
                  </tr>
                  <tr>
                    <td>L-WH linear</td>
                    <td>0.357</td>
                    <td>0.422</td>
                    <td>0.495</td>
                  </tr>
                  <tr>
                    <td>L-WH non-linear</td>
                    <td>0.357</td>
                    <td>0.421</td>
                    <td>0.494</td>
                  </tr>
                  <tr>
                    <td class="bottom-line text-weight">L-WH DNN</td>
                    <td class="bottom-line text-weight">0.362</td>
                    <td class="bottom-line text-weight">0.425</td>
                    <td class="bottom-line text-weight">0.498</td>
                  </tr>
                </table>
                <h2>4. Reference</h2>
                <p>[1] Huang P S, He X, Gao J, et al. Learning deep structured semantic models for web search using clickthrough data [C]. In ACM International Conference on Conference on Information & Knowledge Management. ACM, 2013:2333-2338.</p>
              </div>
            </el-scrollbar>
          </el-card>
        </el-col>
        <el-col :span="9">
          <el-scrollbar style="height:100%;">
            <div class="description-content">
              <el-card>
                <el-scrollbar style="height:100%;">
                  <img src="../../../assets/dssm-structure.jpg" width="100%">
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
