import * as authTypes from './auth/types'
import * as appTypes from './app/types'

export default {
  storeToken ({ commit }, token) {
    commit(authTypes.STORE_TOKEN, {
      token: token
    })
  },
  storeUsername ({ commit }, username) {
    commit(authTypes.STORE_USERNAME, {
      username: username
    })
  },
  logout ({ commit }) {
    commit(authTypes.LOGOUT)
  },
  updateMenulist ({ commit }) {
    commit(appTypes.UPDATE_MENULIST)
  },
  setOpenedSubmenu ({ commit }, menuName) {
    commit(appTypes.SET_OPENED_SUBMENU_NAME, menuName)
  }
}
