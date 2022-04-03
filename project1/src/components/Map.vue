<template>
  <div id="map"/>
</template>

<script>
/* eslint-disable */
import 'mapbox-gl/dist/mapbox-gl.css'
import mapboxgl from 'mapbox-gl'

export default {
  name: "Here",
  props: {
    center: Object
  },
  data() {
    return {
      token: null,
      map: null,
    };
  },
  async mounted() {
    mapboxgl.accessToken = 'pk.eyJ1IjoicHBwYzEzMTIiLCJhIjoiY2wxNTk0dGR0MHl6NzNkczBxNzRxbTczNSJ9.qFzM1Q2oov0E6rFbDodAdQ';
    this.$store.commit('setMap',new mapboxgl.Map({
      container: 'map',
      style: 'mapbox://styles/mapbox/streets-v11',
      center: [4.402580, 51.217616],
      zoom: 9,
    }));
    this.map = this.$store.state.map;
    // await this.addMarkers();

  },
  methods: {
    addMarker(pos) {
      const marker = new mapboxgl.Marker().setLngLat(pos).addTo(this.map);
    },
  },
  computed: {
    getStations() {
      return this.$store.state.stations;
    },
  }
};
</script>

<style scoped>
#map {
  width: 100vw;
  text-align: center;
  position: fixed;
  background-color: #ccc;
  height: 100vh;
}
</style>