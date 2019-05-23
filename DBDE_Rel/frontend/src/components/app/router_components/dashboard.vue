<template>
  <div class='dba-div-donese'>
  <title>智融集团 | DBCO数据库平台</title>
  <h1>dashboard</h1>
  </div>
</template>

<script>
export default {
  name: 'dba-donese',
  data () {
    return {
      isSelect: 'DBA管理',
      jsonplacelist: []
    }
  },
  methods: {
    selectMapNav (ti) {
      this.isSelect = ti
    }
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
ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    width: 200px;
    background-color: #f1f1f1;
}
li a {
    display: block;
    color: #000;
    padding: 8px 16px;
    text-decoration: none;
}
/* 鼠标移动到选项上修改背景颜色 */
li a:hover {
    background-color: #555;
    color: white;
}
li span:hover {
    background-color: #555;
    color: white;
}
nav {
  color: green;
}
</style>
