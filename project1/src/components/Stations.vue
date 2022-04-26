/* eslint-disable */

<template>
  <div class="station-wrap">
<!--  <div v-for="station in stations" :key="station.name" style="background-color: red;">-->
<!--    <p>{{station}}</p>-->
<!--  </div>-->
  <StationCard v-for="station in stations" :key="station.name" :station="station"/>
  </div>
</template>

<script>
import axios from "axios";
import StationCard from "@/components/StationCard";
/* eslint-disable */
export default {
  name: "Stations",
  components: {StationCard},
  data() {
    return {
      stations: [],
    }
  },
  mounted(){
    axios({
      method: "get",
      url: 'http://localhost:80/stations'
    })
    .then((response)=> {
      this.stations = response.data.station;
      console.log("got request")
    })
    .catch((er) => {
      console.assert(true, er);
    })
  }
}
</script>

<style scoped>

.station-wrap{
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
}

</style>