import axios from 'axios'
import store from '@/store'
import {router} from '@/router'

axios.defaults.timeout = process.env.TIMEOUT
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
// axios.defaults.baseURL = process.env.BASE_URL
const URL_PREFIX = '/v1.0'
// axios.defaults.baseURL = 'http://10.0.14.132:8009' + URL_PREFIX
axios.defaults.baseURL = 'http://10.0.14.188:8009' + URL_PREFIX

axios.interceptors.request.use(config => {
  // config.url = config.baseURL + URL_PREFIX + config.url.substr(config.baseURL.length)
  // config.url = 'http://10.0.14.132:8009/v1.0/jwt-token/'
  // if (localStorage.getItem('token') === null && localStorage.getItem('Authorization')) {
  if (localStorage.getItem('token') === null || localStorage.getItem('Authorization')) {
    console.log('are you ok')
  }
  if (localStorage.getItem('Authorization')) {
    // config.headers.Authorization = 'JWT ' + localStorage.getItem('Authorization')
    config.headers.Authorization = localStorage.getItem('Authorization')
  }
  return config
}, err => {
  return Promise.reject(err)
})

axios.interceptors.response.use(response => {
  return response
}, err => {
  if (err.response) {
    switch (err.response.status) {
      case 401:
        store.dispatch('logout')
        router.push({name: 'LoginLink'})
        break
    }
  }
  return Promise.reject(err.response)
})

export default axios
