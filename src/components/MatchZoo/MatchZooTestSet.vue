<template>
    <div id="matchzootestset">
      <span id="upload-tip">Upload Testing Set</span>
      <el-upload
        class="upload-demo"
        id="upload-block"
        drag
        action="https://jsonplaceholder.typicode.com/posts/"
        :limit="1">
        <i class="el-icon-upload"></i>
        <div class="el-upload__text">Drag your file here，or<em> click to upload</em></div>
        <div class="el-upload__tip" slot="tip">json format only, file does not exceed 1GB</div>
      </el-upload>
    </div>
</template>

<script>
  export default {
    name: 'MatchZooTestSet'
  }
</script>

<style scoped>

</style>
