<div align='center'>
<img src="../../../assets/matchzoo-logo.png" width = "400"  alt="图片名称" align=center />
</div>

[![Build Status](https://travis-ci.org/NTMC-Community/MatchZoo.svg?branch=master)](https://travis-ci.org/NTMC-Community/MatchZoo/)
[![MatchZoo 2.0](https://img.shields.io/badge/marchzoo%202.0-WIP-blue.svg)](https://github.com/NTMC-Community/MatchZoo/tree/2.0)
---
MatchZoo is a toolkit for text matching. It was developed with a focus on facilitating the design, comparison and sharing of deep text matching models. There are a number of deep matching methods, such as DRMM, MatchPyramid, MV-LSTM, aNMM, DUET, ARC-I, ARC-II, DSSM, and CDSSM, designed with a unified interface (collection of papers: [awesome-neural-models-for-semantic-match](https://github.com/NTSC-Community/awaresome-neural-models-for-semantic-match)). Potential tasks related to MatchZoo include document retrieval, question answering, conversational response ranking, paraphrase identification, etc. We are always happy to receive any code contributions, suggestions, comments from all our MatchZoo users.

<table>
  <tr>
    <th width=30%, bgcolor=#999999 >Tasks</th> 
    <th width=20%, bgcolor=#999999>Text 1</th>
    <th width="20%", bgcolor=#999999>Text 2</th>
    <th width="20%", bgcolor=#999999>Objective</th>
  </tr>
  <tr>
    <td align="center", bgcolor=#eeeeee> Paraphrase Indentification </td>
    <td align="center", bgcolor=#eeeeee> string 1 </td>
    <td align="center", bgcolor=#eeeeee> string 2 </td>
    <td align="center", bgcolor=#eeeeee> classification </td>
  </tr>
  <tr>
    <td align="center", bgcolor=#eeeeee> Textual Entailment </td>
    <td align="center", bgcolor=#eeeeee> text </td>
    <td align="center", bgcolor=#eeeeee> hypothesis </td>
    <td align="center", bgcolor=#eeeeee> classification </td>
  </tr>
  <tr>
    <td align="center", bgcolor=#eeeeee> Question Answer </td>
    <td align="center", bgcolor=#eeeeee> question </td>
    <td align="center", bgcolor=#eeeeee> answer </td>
    <td align="center", bgcolor=#eeeeee> classification/ranking </td>
  </tr>
  <tr>
    <td align="center", bgcolor=#eeeeee> Conversation </td>
    <td align="center", bgcolor=#eeeeee> dialog </td>
    <td align="center", bgcolor=#eeeeee> response </td>
    <td align="center", bgcolor=#eeeeee> classification/ranking </td>
  </tr>
  <tr>
    <td align="center", bgcolor=#eeeeee> Information Retrieval </td>
    <td align="center", bgcolor=#eeeeee> query </td>
    <td align="center", bgcolor=#eeeeee> document </td>
    <td align="center", bgcolor=#eeeeee> ranking </td>
  </tr>
</table>

## We're actively developing MatchZoo 2.0 with everything improved, stay tuned! See branch 2.0 for early access.

## Installation
MatchZoo is still under development. Before the first stable release (1.0), please clone the repository and run
```
git clone https://github.com/NTMC-Community/MatchZoo.git
cd MatchZoo
python setup.py install
```
In the main directory, this will install the dependencies automatically.

For usage examples, you can run
```
python matchzoo/main.py --phase train --model_file examples/toy_example/config/arci_ranking.config
python matchzoo/main.py --phase predict --model_file examples/toy_example/config/arci_ranking.config
```

## Overview
The architecture of the MatchZoo toolkit is described in the Figure  in what follows,
<div align='center'>
<img src="../../../assets/matchzoo-logo.png" width = "400" height = "200" alt="图片名称" align=center />
</div>  

There are three major modules in the toolkit, namely data preparation, model construction, training and evaluation, respectively. These three modules are actually organized as a pipeline of data flow.

### Data Preparation
The data preparation module aims to convert dataset of different text matching tasks into a unified format as the input of deep matching models. Users provide datasets which contains pairs of texts along with their labels, and the module produces the following files.

+	**Word Dictionary**: records the mapping from each word to a unique identifier called *wid*. Words that are too frequent (e.g. stopwords), too rare or noisy (e.g. fax numbers) can be  filtered out by predefined rules.
+	**Corpus File**: records the mapping from each text to a unique identifier called *tid*, along with a sequence of word identifiers contained in that text. Note here each text is truncated or padded to a fixed length customized by users.
+	**Relation File**: is used to store the relationship between two texts, each line containing a pair of *tids* and the corresponding label.
+   **Detailed Input Data Format**: a detailed explaination of input data format can be found in [MatchZoo/data/toy_example/readme.md](https://github.com/NTMC-Community/MatchZoo/blob/master/data/toy_example/readme.md).

### Model Construction
In the model construction module, we employ Keras library to help users build the deep matching model layer by layer conveniently. The Keras libarary provides a set of common layers widely used in neural models, such as convolutional layer, pooling layer, dense layer and so on. To further facilitate the construction of deep text matching models, we extend the Keras library to provide some layer interfaces specifically designed for text matching.

Moreover, the toolkit has implemented two schools of representative deep text matching models, namely representation-focused models and interaction-focused models [[Guo et al.]](http://www.bigdatalab.ac.cn/~gjf/papers/2016/CIKM2016a_guo.pdf).

### Training and Evaluation
For learning the deep matching models, the toolkit provides a variety of objective functions for regression, classification and ranking. For example, the ranking-related objective functions include several well-known pointwise, pairwise and listwise losses. It is flexible for users to pick up different objective functions in the training phase for optimization. Once a model has been trained, the toolkit could be used to produce a matching score, predict a matching label, or rank target texts (e.g., a document) against an input text.

## Benchmark Results:
Here, We adopt two representative datasets for examples to show the usage of MatchZoo for ranking and classification. For ranking task, we use <a href="https://www.microsoft.com/en-us/download/details.aspx?id=52419">WikiQA</a> dataset as an example. For classification task, we use <a href="https://www.kaggle.com/c/quora-question-pairs/">QuoraQP</a> dataset as an example.

### WikiQA for Ranking
WikiQA is a popular benchmark dataset for answer sentence selection in question answering. We have provided <a href="./data/WikiQA/run_data.sh">a script</a> to download the dataset, and prepared it into the MatchZoo data format. In the <a href="./examples/wikiqa/config">models directory</a>, there are a number of configurations about each model for WikiQA dataset. 

Take the DRMM as an example. In training phase, you can run
```
python matchzoo/main.py --phase train --model_file examples/wikiqa/config/drmm_wikiqa.config
```
In testing phase, you can run
```
python matchzoo/main.py --phase predict --model_file examples/wikiqa/config/drmm_wikiqa.config
```

We have compared 10 models, the results are as follows.
<table>
  <tr>
    <th width=10%, bgcolor=#999999 >Models</th> 
    <th width=20%, bgcolor=#999999>NDCG@3</th>
    <th width="20%", bgcolor=#999999>NDCG@5</th>
    <th width="20%", bgcolor=#999999>MAP</th>
  </tr>
  <tr>
    <td align="center", bgcolor=#eeeeee> DSSM </td>
    <td align="center", bgcolor=#eeeeee> 0.5439 </td>
    <td align="center", bgcolor=#eeeeee> 0.6134 </td>
    <td align="center", bgcolor=#eeeeee> 0.5647 </td>
  </tr>
  <tr>
  	 <td align="center", bgcolor=#eeeeee> CDSSM </td>
  	 <td align="center", bgcolor=#eeeeee> 0.5489 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6084</td>
  	 <td align="center", bgcolor=#eeeeee> 0.5593 </td>
  </tr>
  <tr>
  	 <td align="center", bgcolor=#eeeeee> ARC-I </td>
  	 <td align="center", bgcolor=#eeeeee> 0.5680 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6317 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.5870 </td>
  </tr>
  <tr>
  	 <td align="center", bgcolor=#eeeeee> ARC-II </td>
  	 <td align="center", bgcolor=#eeeeee> 0.5647 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6176 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.5845 </td>
  </tr>
  <tr>
  	 <td align="center", bgcolor=#eeeeee> MV-LSTM </td>
  	 <td align="center", bgcolor=#eeeeee> 0.5818 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6452 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.5988 </td>
  </tr>
  <tr>
  	 <td align="center", bgcolor=#eeeeee> DRMM </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6107 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6621 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6195 </td>
  </tr>
  <tr>
  	 <td align="center", bgcolor=#eeeeee> K-NRM </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6268 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6693 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6256 </td>
  </tr>
  <tr>
     <td align="center", bgcolor=#eeeeee> aNMM </td>
     <td align="center", bgcolor=#eeeeee> 0.6160 </td>
     <td align="center", bgcolor=#eeeeee> 0.6696 </td>
     <td align="center", bgcolor=#eeeeee> 0.6297 </td>
  </tr>
  <tr>
  	 <td align="center", bgcolor=#eeeeee> DUET </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6065 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6722 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6301 </td>
  </tr>
  <tr>
  	 <td align="center", bgcolor=#eeeeee> MatchPyramid </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6317 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6913 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6434 </td>
  </tr>
  <tr>
  	 <td align="center", bgcolor=#eeeeee> DRMM_TKS </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6458 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6956 </td>
  	 <td align="center", bgcolor=#eeeeee> 0.6586 </td>
  </tr>
 
</table>
The loss of each models in train dataset are described in the following figure,
 <div align='center'>
<img src="../../../assets/matchzoo-logo.png" width = "550" alt="图片名称" align=center />
</div>

The MAP of each models in test dataset are depicted in the following figure,
<div align='center'>
<img src="../../../assets/matchzoo-logo.png" width = "550" alt="图片名称" align=center />
</div>
Here, the DRMM_TKS is a variant of DRMM for short text matching. Specifically, the matching histogram is replaced by a top-k maxpooling layer and the remaining part are fixed. 

### QuoraQP for Classification
QuoraQP (Quora Question Pairs) is a text matching competition from kaggle, which is to predict whether the provided pair of questions have the same meaning. We have provided <a href="./data/QuoraQp/run_data.sh">a script</a> to download the dataset, and prepared it into the MatchZoo data format. In the <a href="./examples/QuoraQP/config">models directory</a>, there are a number of configurations about each model for QuoraQP dataset. 

Take the MatchPyramid as an example. In training phase, you can run
```
python matchzoo/main.py --phase train --model_file examples/QuoraQP/config/matchpyramid_quoraqp.config
```
In testing phase, you can run
```
python matchzoo/main.py --phase predict --model_file examples/QuoraQP/config/matchpyramid_quoraqp.config
```
The loss of each models in train dataset are described in the following figure,
 <div align='center'>
<img src="../../../assets/matchzoo-logo.png" width = "550" alt="图片名称" align=center />
</div>

The precisioin of each models in test dataset are depicted in the following figure,
<div align='center'>
<img src="../../../assets/matchzoo-logo.png" width = "550" alt="图片名称" align=center />
</div>

<script>
export default {
  name: 'Introduction1'
}
</script>
