<template>
  <header>
    <h1>{{name}}</h1>
//    <div id="bag" v-bind:class="{burst:picshow}"></div>
    <p>{{age}}</p>
    <table border="0" cellspacing="0" cellpadding="0" role="presentation" width="800">
      <tr>
        <th bgcolor="#E6E6FA" width="100">身高</th>
        <th bgcolor="#E6E6FA" width="100">体重</th>
      </tr>
      <tr v-for="securt in securts" :key="securt.info">
        <td>{{securt.height}}</td><td>{{securt.weight}}</td>
      </tr>
      <tr v-for="info in infos" :key="info.k">
        <td>{{info.height}}</td><td>{{info.weight}}</td>
      </tr>   </table>
    <p>{{securts.height}}</p>
    <ul>
      <li v-for="se in securts" v-bind:key="se.text" v-on:click="se.show = !se.show">
        {{ se }}
        {{ se.height }}
        <p v-show="se.weight">{{ se.weight }}</p>
        <p v-show="se.show">{{ se.height }}{{ se.weight }}</p>
      </li>
    </ul>
  </header>
</template>

<script>
export default {
  name: 'tly',
  data () {
    return {
      name: '佟丽娅',
      age: '35',
      securts: [
        {height: '164.5cm'},
        {weight: '44kg'},
        {show: false}
      ],
      infos: [
        {height: '164.5cm', weight: '44kg', show: false}
      ],
      picshow: false
    }
  }
}
</script>

<style scoped>
header {
  background: lightgreen;
  padding: 10px;
}
h1 {
  color: #222;
  text-align: center;
}
header p{
  background: red;
  color: purple;
  text-align: left;
}
.securts{
  width: 100%;
  max-width: 1200px;
  margin: 40px auto;
  padding: 0 20px;
  box-sizing: border-box;
  color: yellow;
}
/*display: flex;属性表示所有li都摆放在同一行
ul{
  display: flex;
  flex-wrap: wrap;
  list-style-type: none;
  padding: 0;
}
flex-grow: 1;表示占满整行,无论1个元素还是2个元素
li{
  flex-grow: 1;
  flex-basis: 200px;
  text-align: center;
  padding: 30px;
  border: 1px solid #222;
}
*/
/*
burst{
  background: url('./assets/tly12.jpg') no-repeat;
} */
</style>
