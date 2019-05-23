<template>
  <div class='dba-div-donese'>
  <title>智融集团 | DBCO数据库平台</title>
  <ul>
    <li v-for='ti in projectItems' :key='ti.info' v-on:click="ti.show = !ti.show">
    <span>{{ti.title}}</span>
    <img :src="ti.pic" v-show="ti.show" width="40%">
    </li>
  </ul>
  </div>
</template>

<script>
export default {
  name: 'dba-donese',
  data () {
    return {
      isSelect: 'DBA管理',
      projectItems: [
        {title: '大盘', pic: '../assets/dota2.jpg', show: false},
        {title: '资源费用', pic: '../assets/vue-study1.jpg', show: false},
        {title: '日志', pic: '../assets/vue-study1.jpg', show: false}
      ]
    }
  },
  methods: {
    selectMapNav (ti) {
      this.isSelect = ti
    }
  }
}
</script>

<style>
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
}   */
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
}
span {
  flex-grow: 1;
  flex-basis: 200px;
  text-align: center;
  padding: 30px;
  border: 1px solid #222;
  margin: 10px;
}
</style>
