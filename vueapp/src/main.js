// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import jquery from 'jquery'
import VueCarousel from 'vue-carousel'
import router from './router'
import store from './Store/store'
import '../w3.css'
import '../w3-colors-2018.css'
import '../w3-theme-red.css'

import VModal from 'vue-js-modal'
Vue.use(VModal)

Vue.config.productionTip = false
Vue.use(jquery)
Vue.use(VueCarousel)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})

Vue.filter('currency', function (value) {
  return '$' + parseFloat(value).toFixed(2)
})
