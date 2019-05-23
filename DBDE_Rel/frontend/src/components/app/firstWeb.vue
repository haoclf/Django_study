<template>
  <div class='dba-div-done'>
  <title>智融集团 | DBCO数据库平台</title>
  <ul>
    <li v-for="item in projectItems" :key="item.info" @click="selectMapNav(item.title)">
      <img :src="isSelect === item.title ? item.pic : item.pic" alt="">
      <p><span>{{item.title}}</span></p><br>
    </li>
  </ul>
  </div>
</template>

<script>
export default {
  name: 'dba-done',
  data () {
    return {
      isSelect: 'DBA管理',
      projectItems: [
        {title: '大盘', pic: '../assets/佟丽娅1.jpg'},
        {title: '资源', pic: '../assets/佟丽娅2.jpg'},
        {title: '日志', pic: '../assets/佟丽娅3.jpg'}
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
.dba-div-done ul{
  width: 100%;
  height: 50px;
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

</style>
