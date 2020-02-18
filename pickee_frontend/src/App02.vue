<template>
  <div id="app02">
    <img alt="Vue logo" src="./assets/logo.png">
    <HelloWorld msg="Welcome to Your SECOND Vue.js App02"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App Two',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app02 {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
