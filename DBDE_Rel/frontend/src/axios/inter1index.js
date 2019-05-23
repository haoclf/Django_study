import axios from 'axios'
import store from '@/store'
// import {router} from '@/routers'

axios.defaults.timeout = process.env.TIMEOUT
axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded'
axios.defaults.baseURL = process.env.BASE_URL
// axios.defaults.baseURL = 'http://10.0.14.132:8009'
const URL_PREFIX = '/v1.0'

/*
axios.interceptors.request.use(config => {
  config.url = config.baseURL + URL_PREFIX + config.url.substr(config.baseURL.length)
  if (localStorage.getItem('token')) {
    // config.headers.Authorization = 'Token ' + localStorage.getItem('token')
    config.headers.Authorization = 'JWT ' + localStorage.getItem('token')
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
        router.push({name: 'Login'})
        break
    }
  }
  return Promise.reject(err.response)
})
*/
export default axios
