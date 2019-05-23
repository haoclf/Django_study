import * as types from './types'

export default {
  [types.STORE_TOKEN] (state, { token }) {
    state.token = token
    state.Authorization = 'JWT ' + token,
    localStorage.setItem('token', token),
    localStorage.setItem('Authorization', 'JWT ' + token)
  },
  [types.STORE_USERNAME] (state, { username }) {
    state.username = username
    localStorage.setItem('username', username)
  },
  [types.LOGOUT] (state) {
    state.token = null
    state.username = null
    state.Authorization = null
    localStorage.removeItem('token')
    localStorage.removeItem('username')
    localStorage.removeItem('Authorization')
  }
}
