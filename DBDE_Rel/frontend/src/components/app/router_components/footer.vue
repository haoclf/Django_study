<template>
  <div class='dba-div-donese'>
  <title>智融集团 | DBCO数据库平台 | 导航栏</title>
  <nav>
  <ul>
    <li v-for='ti in DBItems' :key='ti.info' v-on:click="ti.show = !ti.show">
    <span class='tii'>{{ti.name}}</span>
    <img :src="ti.pic" v-show="ti.show" width="40%">
    </li>
  </ul>
  <ul>
    <li><a href='/DBInfo' >DB概况</a></li>
    <li><a href='/dashboard'>大盘展示</a></li>
    <li><router-link to='/resourceManage' id='resourcemanInfo1'>资源管理</router-link></li>
  </ul>
  <ul>
    <!-- isshow传值给子组件DBInfo.vue  -->
    <li><span><a href='/DBInfo' id='DBInfo' v-on:click="showBu()" v-bind:isshow="show">DB概况</a></span></li>
    <li><router-link to='/dashboard' id='dashInfo'>大盘展示</router-link></li>
    <li><button @click="showBu()" id='resourcemanInfo2'>资源管理</button></li>
  </ul>
  </nav>
  </div>
</template>

<script>
export default {
  name: 'dba-donese',
  data () {
    return {
      show: false,
      isSelect: 'DBA管理',
      jsonplacelist: [],
      DBItems: [
        {name: 'DB概况'},
        {name: '大盘展示'},
        {name: '资源管理'}
      ]
    }
  },
  methods: {
    selectMapNav (ti) {
      this.isSelect = ti
    },
    showBu: function () {
      this.show = true
    }
  },
  arrowDown: function () {
    this.isshow = !this.isshow
  },
  select: function (item, index) {
    this.isshow = false
    console.log(item)
    console.log(index)
    this.unitModel = index
    this.unitName = item.name
  },
  created () {
    /* 打开页面 */
    this.$http.get('http://jsonplaceholder.typicode.com/users')
      // 传值给data
      .then((data) => {
        console.log(data)
        this.jsonplacelist = data.body
      })
  }
}
</script>

<style scoped>
/* 导航栏 .dba-div-donese ul{
  width: 100%;
  height: 50px;
  padding: 5px;
  position: fixed;
  bottom: 0;
  z-index: 1;
  background-color: #fff;
  display: flex;
  li{
    text-align: center;
    flex: 1;
    img{height: 23px;width: 23px;margin-top: 5px;}
    p{font-size: 0.1rem;height: 15px;line-height: 10px;}
  }
}
.dba-div-donese{
  width: 100%;
  max-width: 1200px;
  margin: 40px auto;
  bos-sizing: border-box;
  text-align: left;
  ul{
    display: flex;
    flex-wrap: wrap;
    list-style-type: none;
    padding: 0;
    li{
      flex-grow: 1;
      flex-basis: 200px;
      text-align: center;
      padding: 30px;
      border: 1px solid #222;
      margin: 10px;
    }
  }
}  */
span {
  flex-grow: 1;
  flex-basis: 200px;
  text-align: center;
  padding: 30px;
  border: 1px solid #222;
  margin: 10px;
  display: block;
}
nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    width: 200px;
    background-color: #4f4f4f;
}
li a {
    display: block;
    color: #00A2E9;
    padding: 8px 16px;
    text-decoration: none;
}
/* 鼠标移动到选项上修改背景颜色 */
li a:hover {
    background-color: #666;
    color: white;
}
li span:hover {
    background-color: #00A2E9;
    padding: 4px 16px;
    color: white;
}
span {
    background-color: #666;
    padding: 4px 16px;
    color: white;
}
div.dba-div-donese {
  position: relative;
  display: inline-block;
}
span.ti {
  display: none;
  position: absolute;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  background-color: #666;
  padding: 4px 16px;
  color: white;
  cursor: pointer;
}
#DBInfo {
  display: white;
  background-color: #666;
  padding: 4px 16px;
  color: white;
}
#dashInfo {
  display: red;
  background-color: #666;
  padding: 4px 16px;
  color: white;
}
#dashInfo:hover {
    background-color: #00A2E9;
    padding: 4px 16px;
    color: white;
}
</style>
