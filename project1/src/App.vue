<template>
  <div>
    <div style="width: 100%; height: 100%">
    <HereMap/>
  </div>
  <DirectionBar/>
  </div>
</template>

<script>
import HereMap from "@/components/Map";
import axios from "axios";
import DirectionBar from "@/components/DirectionBar";
export default {
  name: 'App',
  components: {
    DirectionBar,
    HereMap,
  },
  mounted() {
    console.log("app mount")
    axios({
      method: "get",
      url: 'http://localhost:80/stations'
    })
    .then((response)=> {
      this.$store.commit('setStations', response.data.station);
    })
    .catch((er) => {
      console.assert(true, er);
    })
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
}
</style>
