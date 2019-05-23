import Vue from 'vue'
import VueRouter from 'vue-router'
import App from '../App'
import axios from 'axios'
import Login from '../components/auth/Login'
import HelloWorld from '../components/HelloWorld'
import Home from '../components/app/opRDS/Home'
import mysqlRe from '../components/app/opRDS/mysql'
// import postgresqlRe from '../components/app/opRDS/postgresql'
import ErrorLink500 from '../components/common/error-page/500'

Vue.use(VueRouter)

export const routes = [
  {path: '/', name: 'RootLink', component: Login},
  {path: '/login', name: 'LoginLink', component: Login},
  {path: '/home', name: 'HomeLink', component: Home, meta:{requireAuth: true}, 
   children: [
     {path: 'postgresql', name: 'homePostgresqlreLink', component: resolve => {require(['@/components/app/opRDS/postgresql.vue'], resolve)}}
  ]},
  {path: '/dashboard', name: 'DashBoardLink', component: HelloWorld},
    {     
    path: '/dashboard/error500',
    name: 'ErrorLink500',
    menu: false,
    component: resolve => {
      require(['@/components/common/error-page/500.vue'], resolve)
    }
  },
  {path: '/tongliya', name: 'settingLink', component: resolve => {
    require(['@/components/app/TongLiYa.vue'], resolve)
    }
  },
  {path: '/mysqlResource', name: 'mysqlreLink', component: mysqlRe},
  {path: '/postgresql', name: 'postgresqlreLink', component: resolve => {require(['@/components/app/opRDS/postgresql.vue'], resolve)}}
]

export const router = new VueRouter({
  routes: routes,
  mode: 'history',
  base: __dirname
})

router.beforeEach((to, from, next) => {
    if (to.meta.requireAuth) {  // 判断该路由是否需要登录权限
        if (localStorage.getItem('Authorization')) {  // 通过vuex state获取当前的token是否存在
            next();
        }
        else {
            next({
                path: '/login',
                query: {redirect: to.fullPath}  // 将跳转的路由path作为参数，登录成功后跳转到该路由
            })
        }
    }
    else {
        next();
    }
})
