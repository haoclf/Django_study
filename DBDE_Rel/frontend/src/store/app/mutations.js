import * as types from './types'
// import {routes} from '@/router'
import {routes} from '@/routers'

export default {
  [types.UPDATE_MENULIST] (state) {
    let menuList = []
    routes.forEach((item, index) => {
      if (item.menu === undefined || item.menu === true) {
        item.children = item.children.filter(
          child => child.menu === undefined || child.menu === true
        )
        menuList.push(item)
      }
    })
    state.menuList = menuList
  },
  [types.SET_OPENED_SUBMENU_NAME] (state, menuName) {
    state.openedSubmenu = menuName
  }
}
