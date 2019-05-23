// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import VueRouter from 'vue-router' 
// import router from './router'
import {router} from '@/router'
import ElementUI from 'element-ui'
import i18n from './i18n/langs'
import axios from '@/axios'
import store from '@/store'

Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(i18n)
// Vue.prototype.$axios = axios

/*
const router = new VueRouter({
  routes,
  mode: 'history',
  base: __dirname
})
*/

/* eslint-disable no-new */

new Vue({
  el: '#app',
  router,
  i18n,
  store,
  components: { App },
  template: '<App/>',
  render: h => h(App)
})
