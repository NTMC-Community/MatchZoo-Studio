<template>
  <div id="matchpyramid-description">

      <el-row :gutter="20">
        <el-col :span="15">
          <el-card>
            <el-scrollbar style="height:100%;">
              <div class="description-content">
                <h2>1. Introduction</h2>
                <p>Inspired by the success of convolutional neural network in image, the MatchPyramid proposes a novel view of text matching task, and models this task as the problem of image recognition. This model constructs a matching matrix to represent the similarities between words, then use a convolutional neural network to capture rich matching patterns in layer-by-layer way.</p>
                <h2>2. Structure</h2>
                <p>The overall structure of the MatchPyramid is shown in the figure. Firstly, MatchPyramid employs a matching matrix to bridge the gap between text matching and image recognition, it uses three different methods to model the similarity between tokens of two involved texts, as indicator function, cosine and dot product. Then it uses hierarchical convolutional layers to capture rich grains matching patterns from token level to sentence level. For the first convolution layer, it uses dynamic pooling strategy to handle text length variance. The matching score is produced by a multi-layer perception, and the object function can be change to fit different requirement of tasks.</p>
                <h2>3. Performances</h2>
                <p>MatchPyramid conducts experiments on two tasks, i.e. paraphrase identification and paper citation matching. The result for paraphrase identification is summarized in table 1.</p>
                <table class="result-data" cellspacing=0>
                    <caption>Table1: Results on MSRP.</caption>
                    <tr>
                      <th class="top-line">Model</th>
                      <th class="top-line">Acc.(%)</th>
                      <th class="top-line">F<sub>1</sub>(%)</th>
                    </tr>
                    <tr>
                      <td class="top-line">ALL POSITIVE</td>
                      <td class="top-line">66.50</td>
                      <td class="top-line">79.87</td>
                    </tr>
                    <tr>
                      <td>TF-IDF</td>
                      <td>70.31</td>
                      <td>77.62</td>
                    </tr>
                    <tr>
                      <td class="top-line">DSSM</td>
                      <td class="top-line">70.09</td>
                      <td class="top-line">80.96</td>
                    </tr>
                    <tr>
                      <td>CDSSM</td>
                      <td>69.80</td>
                      <td>80.42</td>
                    </tr>
                    <tr>
                      <td>ARC-I</td>
                      <td>69.60</td>
                      <td>80.27</td>
                    </tr>
                    <tr>
                      <td>ARC-II</td>
                      <td>69.90</td>
                      <td>80.91</td>
                    </tr>
                    <tr>
                      <td class="top-line">MP-IND</td>
                      <td class="top-line">75.77</td>
                      <td class="top-line">82.66</td>
                    </tr>
                    <tr>
                      <td>MP-COS</td>
                      <td>75.13</td>
                      <td>82.45</td>
                    </tr>
                    <tr>
                      <td class="bottom-line">MP-DOT</td>
                      <td class="bottom-line text-weight">75.94</td>
                      <td class="bottom-line text-weight">83.01</td>
                    </tr>
                  </table>
                <p>And the result for paper citation matching is table 2.</p>
                <table class="result-data" cellspacing=0>
                    <caption>Table2: Results on the task of paper citation matching.</caption>
                    <tr>
                      <th class="top-line">Model</th>
                      <th class="top-line">Acc.(%)</th>
                      <th class="top-line">F<sub>1</sub>(%)</th>
                    </tr>
                    <tr>
                      <td class="top-line">ALL POSITIVE</td>
                      <td class="top-line">33.33</td>
                      <td class="top-line">50.00</td>
                    </tr>
                    <tr>
                      <td>TF-IDF</td>
                      <td>82.63</td>
                      <td>70.21</td>
                    </tr>
                    <tr>
                      <td class="top-line">DSSM</td>
                      <td class="top-line">71.97</td>
                      <td class="top-line">29.88</td>
                    </tr>
                    <tr>
                      <td>CDSSM</td>
                      <td>69.84</td>
                      <td>19.97</td>
                    </tr>
                    <tr>
                      <td>ARC-I</td>
                      <td>84.51</td>
                      <td>76.79</td>
                    </tr>
                    <tr>
                      <td>ARC-II</td>
                      <td>86.48</td>
                      <td>79.57</td>
                    </tr>
                    <tr>
                      <td class="top-line">MP-IND</td>
                      <td class="top-line">73.76</td>
                      <td class="top-line">44.71</td>
                    </tr>
                    <tr>
                      <td>MP-COS</td>
                      <td>86.65</td>
                      <td>79.70</td>
                    </tr>
                    <tr>
                      <td class="bottom-line">MP-DOT</td>
                      <td class="bottom-line text-weight">88.73</td>
                      <td class="bottom-line text-weight">82.86</td>
                    </tr>
                  </table>
                <h2>4.Reference</h2>
                <p>[1] Liang Pang, Shengxian Wan, Yanyan Lan, et al. Text Matching as Image Recognition [C]. In Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence (AAAI), 2016.</p>
                <p></p>
              </div>
            </el-scrollbar>
          </el-card>
        </el-col>
        <el-col :span="9">
          <el-scrollbar style="height:100%;">
            <div class="description-content">
              <el-card>
                <el-scrollbar style="height:100%;">
                  <img src="../../../assets/matchpyramid.png" width="100%">
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
