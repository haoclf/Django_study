<template>
  <div id="app" class="app-main">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
  background-image: url('/assets/佟丽娅2.jpg');
  background-size: cover;
}

.app-main {
  background-image: url('/assets/佟丽娅2.jpg');
  background-size: cover;
}
</style>
