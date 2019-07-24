<template>
    <div id="matchzoopredictset">
      <el-form ref="form" :model="form" label-width="80px">
        <el-form-item label="Pair Case">
          <el-select v-model="form.value" placeholder="You can choose a case here" @change="choose_doc" style="width:100%;">
            <el-option v-for="n in 10" :key="n" :label="n" :value="n">Document {{ n }}</el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="Document1">
          <el-input ref="doc1" type="textarea" v-model="form.document" :autosize="{ minRows:8, maxRows:20 }"></el-input>
        </el-form-item>
        <el-form-item label="Document2">
          <el-input ref="doc2" type="textarea" v-model="form.document" :autosize="{ minRows:8, maxRows:20 }"></el-input>
        </el-form-item>
      </el-form>
      <el-button v-on:click="submit_pair_text()" type="primary" id="matchzoobutton">Submit <i class="el-icon-upload el-icon--right"></i> </el-button>
    </div>
</template>

<script>
  export default {
    name: 'MatchZooPredictSet',
    data () {
      return {
        form: {
          value: null,
          document: '',
          doc_from: [
            '天津条约是指1858年中国清政府与俄、美、英和法四国在天津签订的一系列不平等条约，包括《中俄天津条约》、《中美天津条约》、《中英天津条约》和《中法天津条约》。',
            '爱迪生8岁上学，但仅仅读了三个月的书，就被老师斥为“低能儿”而撵出校门。从此以后，他的母亲是他的“家庭教师”。由于母亲的良好的教育方法，使得他对读书发生了浓厚的兴趣。“他不仅博览群书，而且一目十行，过目成诵”。8岁时，他读了英国文艺复兴时期最重要的剧作家莎士比亚、狄更斯的著作和许多重要的历史书籍，到9岁时，他能迅速读懂难度较大的书，如帕克的《自然与实验哲学》。',
            '太祖曰：「朕之天下有谁乱者？」刘伯温答曰：天下饥寒有怪异，栋梁龙德乘婴儿，禁宫阔大任横走，长大金龙太平时，老练金精龙壮旺，相传昆玉继龙堂，（英宗复辟）谁人任用保社稷，八千女鬼乱朝纲。（指魏忠贤）（明成祖篡夺江山时，宦官之功劳不小，后来建立了东厂，八千女鬼就是指东厂的宦官）太祖曰：「莫非父子互争国乎？」刘伯温曰：「非也！树上挂曲尺（指明朝朱姓），遇顺则止（遇顺治皇帝而明灭），至此天下未已。',
            '洗一洗就可生吃的蔬菜包括胡萝卜、白萝卜、番茄、黄瓜、柿子椒、大白菜心等。',
            '东风雪铁龙是一个中法合资品牌，东风是中国的，雪铁龙是法国的。',
            '东汉末年，社会危机日益深重，广大农民与豪强地主及封建国家的矛盾激化。黄巾起义正是在农民斗争蓬勃开展的基础上爆发的。',
            '天接云涛连晓雾，星河欲转千帆舞。',
            '现在罗马是意大利的首都，古罗马通常指从前9世纪初在意大利半岛中部兴起的文明，历罗马王政时代、罗马共和国，于1世纪前后扩张成为横跨欧洲、亚洲、非洲称霸地中海的庞大罗马帝国，历史上罗马帝国的首都是罗马城。',
            '1950年，11月22日，明尼阿波利斯湖人队和韦恩堡活塞队的比赛中，创下了nba最低比分，19：19。',
            '童话是一个美妙而又神奇的世界,它里面有着许许多多美好的幻想.大家一定读过安徒生爷爷写的童话吧!他写的故事是那样的扣人心弦,扑朔迷离,离奇有趣.那你们知道安徒生是这样创造出这些令人惊叹的杰作吗?<e>安徒生的童年是不幸的,他的爸爸谢世后,他与妈妈相依为命.但是悲惨的命运并没有使他倒下.他有着远大的理想与目标,他决心实现自己的梦想.虽然他经历过无数次的坎坷与失败,可他从来没有放弃过,从来没有自卑过.他凭着澎湃的热情,百折不挠的精神,终于成为了一名童话大师.'
          ]
        }
      }
    },
    methods: {
      choose_doc () {
        this.form.document = this.form.doc_from[this.form.value - 1]
      },
      submit_pair_text: function () {
        var pair_text = {
          doc1: this.$refs.doc1.value,
          doc2: this.$refs.doc2.value
        }
        this.$emit('pair_text', pair_text)
      }
    }
  }
</script>

<style scoped>

</style>
