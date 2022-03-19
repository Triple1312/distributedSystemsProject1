<template>
<!--  <<Navbar/>-->
<!--  <div style="width:100%; height:100% ">-->

<!--  </div>>-->
  <Stations/>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
// import NavBar from "@/components/NavBar";
import Stations from "@/components/Stations";
export default {
  name: 'App',
  components: {
    Stations,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
