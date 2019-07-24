<template>
  <div id="introrightcard">
    <h2 id="h2-1">
      <a id="user-content-overview" class="anchor" aria-hidden="true" href="#overview"></a>
      Overview
    </h2>
    <p>The architecture of the MatchZoo toolkit is described in the Figure  in what follows,</p>
    <img src="../../../assets/overview.png" width="400" height="200" alt="图片名称" align="center" style="max-width:100%;">
    <p>There are three major modules in the toolkit, namely data preparation, model construction, training and evaluation, respectively. These three modules are actually organized as a pipeline of data flow.</p>
    <h3 id="h3-1"><a id="user-content-data-preparation" class="anchor" aria-hidden="true" href="#data-preparation"></a>Data Preparation</h3>
    <p>The data preparation module aims to convert dataset of different text matching tasks into a unified format as the input of deep matching models. Users provide datasets which contains pairs of texts along with their labels, and the module produces the following files.</p>
    <ul>
      <li><strong>Word Dictionary</strong>: records the mapping from each word to a unique identifier called <em>wid</em>. Words that are too frequent (e.g. stopwords), too rare or noisy (e.g. fax numbers) can be  filtered out by predefined rules.</li>
      <li><strong>Corpus File</strong>: records the mapping from each text to a unique identifier called <em>tid</em>, along with a sequence of word identifiers contained in that text. Note here each text is truncated or padded to a fixed length customized by users.</li>
      <li><strong>Relation File</strong>: is used to store the relationship between two texts, each line containing a pair of <em>tids</em> and the corresponding label.</li>
      <li><strong>Detailed Input Data Format</strong>: a detailed explaination of input data format can be found in <a href="https://github.com/NTMC-Community/MatchZoo/blob/master/data/toy_example/readme.md">MatchZoo/data/toy_example/readme.md</a>.</li>
    </ul>
    <h3 id="h3-2"><a id="user-content-model-construction" class="anchor" aria-hidden="true" href="#model-construction"></a>Model Construction</h3>
    <p>In the model construction module, we employ Keras library to help users build the deep matching model layer by layer conveniently. The Keras libarary provides a set of common layers widely used in neural models, such as convolutional layer, pooling layer, dense layer and so on. To further facilitate the construction of deep text matching models, we extend the Keras library to provide some layer interfaces specifically designed for text matching.</p>
    <p>Moreover, the toolkit has implemented two schools of representative deep text matching models, namely representation-focused models and interaction-focused models <a href="http://www.bigdatalab.ac.cn/~gjf/papers/2016/CIKM2016a_guo.pdf" rel="nofollow">[Guo et al.]</a>.</p>
    <h3 id="h3-3"><a id="user-content-training-and-evaluation" class="anchor" aria-hidden="true" href="#training-and-evaluation"></a>Training and Evaluation</h3>
    <p>For learning the deep matching models, the toolkit provides a variety of objective functions for regression, classification and ranking. For example, the ranking-related objective functions include several well-known pointwise, pairwise and listwise losses. It is flexible for users to pick up different objective functions in the training phase for optimization. Once a model has been trained, the toolkit could be used to produce a matching score, predict a matching label, or rank target texts (e.g., a document) against an input text.</p>

  </div>
</template>

<script>
  export default {
    name: 'IntroRightCard'
  }
</script>

<style scoped>
  #introrightcard {
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

  h3 {
    display: block;
    font-size: 1.17em;
    margin-block-start: 1em;
    margin-block-end: 1em;
    margin-inline-start: 0px;
    margin-inline-end: 0px;
    font-weight: bold;
  }

  #h2-1 {
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

  #h3-3 {
    font-size: 1.25em;
    font-weight: 600;
    line-height: 1.25;
    margin-bottom: 16px;
    margin-top: 24px;
  }
</style>
