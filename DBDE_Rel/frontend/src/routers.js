import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App'
import Login from './components/Login'

Vue.use(VueRouter)

export const routes = [
  {path: '/', name: 'RootLink', component: Login},
  {path: '/login', name: 'LoginLink', component: Login}
]
