<template>
  <div id="introleftcard">
    <div align='center' id="top-matchzoo">
      <img src="../../../assets/matchzoo-logo.png" width="400" alt="图片名称" align=center />
    </div>
    <h2 id="h2-1">
      <a href="https://travis-ci.org/NTMC-Community/MatchZoo/" rel="nofollow"><img
        src="https://camo.githubusercontent.com/a2bf004e942eb1406bb48a3e40b11614c1e4373f/68747470733a2f2f7472617669732d63692e6f72672f4e544d432d436f6d6d756e6974792f4d617463685a6f6f2e7376673f6272616e63683d6d6173746572"
        alt="Build Status" data-canonical-src="https://travis-ci.org/NTMC-Community/MatchZoo.svg?branch=master"
        style="max-width:100%;"></a>
      <a href="https://github.com/NTMC-Community/MatchZoo/tree/2.0"><img
        src="https://camo.githubusercontent.com/f88f9305a2cc942ba37018416928302f7a63b821/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6d617263687a6f6f253230322e302d5749502d626c75652e737667"
        alt="MatchZoo 2.0" data-canonical-src="https://img.shields.io/badge/marchzoo%202.0-WIP-blue.svg"
        style="max-width:100%;"></a>
    </h2>
    <p>MatchZoo is a toolkit for text matching. It was developed with a focus on facilitating the design, comparison and
      sharing of deep text matching models. There are a number of deep matching methods, such as DRMM, MatchPyramid,
      MV-LSTM, aNMM, DUET, ARC-I, ARC-II, DSSM, and CDSSM, designed with a unified interface (collection of papers: <a
        href="https://github.com/NTSC-Community/awaresome-neural-models-for-semantic-match">awesome-neural-models-for-semantic-match</a>).
      Potential tasks related to MatchZoo include document retrieval, question answering, conversational response
      ranking, paraphrase identification, etc. We are always happy to receive any code contributions, suggestions,
      comments from all our MatchZoo users.
    </p>
    <el-table
      :data="tableData1"
      stripe
      style="width: 100%"
      :row-style="row_height_style">
      <el-table-column
        prop="tasks"
        label="Tasks"
        width="185">
      </el-table-column>
      <el-table-column
        prop="text1"
        label="Text 1"
        width="180">
      </el-table-column>
      <el-table-column
        prop="text2"
        label="Text 2">
      </el-table-column>
      <el-table-column
        prop="objective"
        label="Objective">
      </el-table-column>
    </el-table>
    <h2 id="h2-2">
      <a
        id="user-content-were-actively-developing-matchzoo-20-with-everything-improved-stay-tuned-see-branch-20-for-early-access"
        class="anchor" aria-hidden="true"
        href="#were-actively-developing-matchzoo-20-with-everything-improved-stay-tuned-see-branch-20-for-early-access">
      </a>We're actively developing MatchZoo 2.0 with everything improved, stay tuned! See branch 2.0 for early access.
    </h2>
    <h2 id="h2-3">
      <a id="user-content-installation" class="anchor" aria-hidden="true" href="#installation"></a>
      Installation
    </h2>
    <p>MatchZoo is still under development. Before the first stable release (1.0), please clone the repository and
      run</p>
    <pre id="pre-1"><code>git clone https://github.com/NTMC-Community/MatchZoo.git
cd MatchZoo
python setup.py install</code></pre>
    <p>In the main directory, this will install the dependencies automatically.</p>
    <p>For usage examples, you can run</p>
    <pre id="pre-2"><code>python matchzoo/main.py --phase train --model_file examples/toy_example/config/arci_ranking.config
python matchzoo/main.py --phase predict --model_file examples/toy_example/config/arci_ranking.config
</code></pre>
    <h2 id="h2-4"><a id="user-content-benchmark-results" class="anchor" aria-hidden="true" href="#benchmark-results"></a>Benchmark Results:</h2>
    <p>Here, We adopt two representative datasets for examples to show the usage of MatchZoo for ranking and classification. For ranking task, we use <a href="https://www.microsoft.com/en-us/download/details.aspx?id=52419" rel="nofollow">WikiQA</a> dataset as an example. For classification task, we use <a href="https://www.kaggle.com/c/quora-question-pairs/" rel="nofollow">QuoraQP</a> dataset as an example.</p>
    <h3 id="h3-1"><a id="user-content-wikiqa-for-ranking" class="anchor" aria-hidden="true" href="#wikiqa-for-ranking"></a>WikiQA for Ranking</h3>
    <p>WikiQA is a popular benchmark dataset for answer sentence selection in question answering. We have provided <a href="/NTMC-Community/MatchZoo/blob/master/data/WikiQA/run_data.sh">a script</a> to download the dataset, and prepared it into the MatchZoo data format. In the <a href="/NTMC-Community/MatchZoo/blob/master/examples/wikiqa/config">models directory</a>, there are a number of configurations about each model for WikiQA dataset.</p>
    <p>Take the DRMM as an example. In training phase, you can run</p>
    <pre id="pre-3"><code>python matchzoo/main.py --phase train --model_file examples/wikiqa/config/drmm_wikiqa.config
</code></pre>
    <p>In testing phase, you can run</p>
    <pre id="pre-4"><code>python matchzoo/main.py --phase predict --model_file examples/wikiqa/config/drmm_wikiqa.config
</code></pre>
    <p>We have compared 10 models, the results are as follows.</p>
    <el-table
      :data="tableData2"
      stripe
      style="width: 100%"
      >
      <el-table-column
        prop="models"
        label="Models"
        width="180">
      </el-table-column>
      <el-table-column
        prop="ndcg3"
        label="NDCG@3"
        width="180">
      </el-table-column>
      <el-table-column
        prop="ndcg5"
        label="NDCG@5">
      </el-table-column>
      <el-table-column
        prop="map"
        label="MAP">
      </el-table-column>
    </el-table>
    <p>The loss of each models in train dataset are described in the following figure,</p>
    <img src="../../../assets/matchzoo_wikiqa_loss.png" width="550" alt="图片名称" align="center" />
    <p>The MAP of each models in test dataset are depicted in the following figure,</p>
    <img src="../../../assets/matchzoo_wikiqa_map.png" width="550" alt="图片名称" align="center" />
    <p>Here, the DRMM_TKS is a variant of DRMM for short text matching. Specifically, the matching histogram is replaced by a top-k maxpooling layer and the remaining part are fixed. </p>
    <h3 id="h3-2">
      <a id="user-content-quoraqp-for-classification" class="anchor" aria-hidden="true" href="#quoraqp-for-classification"></a>
      QuoraQP for Classification
    </h3>
    <p>QuoraQP (Quora Question Pairs) is a text matching competition from kaggle, which is to predict whether the provided pair of questions have the same meaning. We have provided <a href="/NTMC-Community/MatchZoo/blob/master/data/QuoraQp/run_data.sh">a script</a> to download the dataset, and prepared it into the MatchZoo data format. In the <a href="/NTMC-Community/MatchZoo/blob/master/examples/QuoraQP/config">models directory</a>, there are a number of configurations about each model for QuoraQP dataset.</p>
    <p>Take the MatchPyramid as an example. In training phase, you can run</p>
    <pre id="pre-5"><code>python matchzoo/main.py --phase train --model_file examples/QuoraQP/config/matchpyramid_quoraqp.config
</code></pre>
    <p>In testing phase, you can run</p>
    <pre id="pre-6"><code>python matchzoo/main.py --phase predict --model_file examples/QuoraQP/config/matchpyramid_quoraqp.config
</code></pre>
    <p>The loss of each models in train dataset are described in the following figure,</p>
    <img src="../../../assets/matchzoo_quoraqp_loss.png" width="550" alt="图片名称" align="center" />
    <p>The precisioin of each models in test dataset are depicted in the following figure,</p>
    <img src="../../../assets/matchzoo_quoraqp_precision.png" width="550" alt="图片名称" align="center" />
  </div>
</template>

<script>
  import VueMarkdown from 'vue-markdown'

  export default {
    name: 'IntroLeftCard',
    components: {
      VueMarkdown
    },
    methods: {
      tableRowClassName ({row, rowIndex}) {
        if (rowIndex === 1) {
          return 'warning-row'
        } else if (rowIndex === 3) {
          return 'success-row'
        }
        return ''
      }
    },
    data: function () {
      return {
        tableData1: [{
          tasks: 'Paraphrase Indentification',
          text1: 'string 1',
          text2: 'string 2',
          objective: 'classification'
        }, {
          tasks: 'Textual',
          text1: 'Entailment',
          text2: 'hypothesis',
          objective: 'classification'
        }, {
          tasks: 'Question',
          text1: 'Answer question',
          text2: 'answer',
          objective: 'classification/ranking'
        }, {
          tasks: 'Conversation',
          text1: 'dialog',
          text2: 'response',
          objective: 'classification/ranking'
        }, {
          tasks: 'Information',
          text1: 'Retrieval query',
          text2: 'document',
          objective: 'ranking'
        }],
        tableData2: [{
          models: 'DSSM',
          ndcg3: '0.5439',
          ndcg5: '0.6134',
          map: '0.5647'
        }, {
          models: 'CDSSM',
          ndcg3: '0.5489',
          ndcg5: '0.6084',
          map: '0.5593'
        }, {
          models: 'ARC-I',
          ndcg3: '0.5680',
          ndcg5: '0.6317',
          map: '0.5870'
        }, {
          models: 'ARC-II',
          ndcg3: '0.5647',
          ndcg5: '0.6176',
          map: '0.5845'
        }, {
          models: 'MV-LSTM',
          ndcg3: '0.5818',
          ndcg5: '0.6452',
          map: '0.5988'
        }, {
          models: 'DRMM',
          ndcg3: '0.6107',
          ndcg5: '0.6621',
          map: '0.6195'
        }, {
          models: 'K-NRM',
          ndcg3: '0.6268',
          ndcg5: '0.6693',
          map: '0.6256'
        }, {
          models: 'aNMM',
          ndcg3: '0.6160',
          ndcg5: '0.6696',
          map: '0.6297'
        }, {
          models: 'DUET',
          ndcg3: '0.6065',
          ndcg5: '0.6722',
          map: '0.6301'
        }, {
          models: 'MatchPyramid',
          ndcg3: '0.6317',
          ndcg5: '0.6913',
          map: '0.6434'
        }, {
          models: 'DRMM_TKS',
          ndcg3: '0.6458',
          ndcg5: '0.6956',
          map: '0.6586'
        }],
        row_height_style: {
          height: '20px'
        }
      }
    }
  }
</script>

<style scoped>
  #introleftcard {
    font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol;
  }

  a {
    color: #0366d6;
    background-color: initial;
    text-decoration: none;
  }

  a:hover {
    text-decoration: underline;
  }

  h2 {
    display: block;
    font-size: 1.5em;
    margin-block-start: 0.83em;
    margin-block-end: 0.83em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
  }

  pre {
    display: block;
    white-space: pre;
    margin: 1em 0px;
  }

  code {
    font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace;
    padding: 0px;
  }

  h3 {
    display: block;
    font-size: 1.17em;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
  }

  #top-matchzoo {
    margin-bottom: 20px;
  }

  .el-table .warning-row {
    background: oldlace;
  }

  .el-table .success-row {
    background: #f0f9eb;
  }

  #h2-1 {
    border-bottom: 1px solid #eaecef;
    padding-bottom: .3em;
  }

  #h2-2 {
    border-bottom: 1px solid #eaecef;
    padding-bottom: .3em;
  }

  #h2-3 {
    border-bottom: 1px solid #eaecef;
    padding-bottom: .3em;
  }

  #h2-4 {
    border-bottom: 1px solid #eaecef;
    padding-bottom: .3em;
  }

  #h3-1 {
    font-size: 1.25em;
    font-weight: 600;
    line-height: 1.25;
    margin-bottom: 16px;
    margin-top: 24px;
  }

  #h3-2 {
    font-size: 1.25em;
    font-weight: 600;
    line-height: 1.25;
    margin-bottom: 16px;
    margin-top: 24px;
  }

  #pre-1 {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    padding: 16px;
    word-wrap: normal;
    margin-bottom: 16px;
    margin-top: 0;
  }

  #pre-2 {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    padding: 16px;
    word-wrap: normal;
    margin-bottom: 16px;
    margin-top: 0;
  }

  #pre-3 {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    padding: 16px;
    word-wrap: normal;
    margin-bottom: 16px;
    margin-top: 0;
  }

  #pre-4 {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    padding: 16px;
    word-wrap: normal;
    margin-bottom: 16px;
    margin-top: 0;
  }

  #pre-5 {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    padding: 16px;
    word-wrap: normal;
    margin-bottom: 16px;
    margin-top: 0;
  }

  #pre-6 {
    background-color: #f6f8fa;
    border-radius: 3px;
    font-size: 85%;
    line-height: 1.45;
    padding: 16px;
    word-wrap: normal;
    margin-bottom: 16px;
    margin-top: 0;
  }
</style>
