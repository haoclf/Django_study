import Vue from 'vue'
import Vuex from 'vuex'
import auth from './auth'
import app from './app'
import actions from './actions'

Vue.use(Vuex)

const debug = process.env.NODE_ENV !== 'production'

export default new Vuex.Store({
  actions,
  modules: {
    auth,
    app
  },
  strict: debug
})
