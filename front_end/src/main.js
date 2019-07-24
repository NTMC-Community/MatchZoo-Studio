// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import locale from 'element-ui/lib/locale/lang/en'
import 'element-ui/lib/theme-chalk/index.css'
import 'element-ui/lib/theme-chalk/base.css'
import VueChatScroll from 'vue-chat-scroll'
import VueMarkdown from 'vue-markdown'
import axios from 'axios'
// import vueHeadful from 'vue-headful'
// import 'font-awesome/less/font-awesome.less'

Vue.config.productionTip = false
// Vue.component('vue-headful', vueHeadful)
Vue.component('vue-markdown', VueMarkdown)
Vue.use(ElementUI, { locale })
Vue.use(VueChatScroll)

axios.defaults.withCredentials = true
Vue.prototype.$axios = axios

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {
    App,
    VueMarkdown
  },
  render: h => h(App)
})
