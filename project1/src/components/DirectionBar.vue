<template>
  <div id="directionBar">
    <div id="inputBar">
      <label for="directrionBarInputFrom">
        From:
      </label>
      <input type="search" id="directrionBarInputFrom" class="barInput" list="stationList" :onchange="setFrom_name"/>

      <label for="directrionBarInputTo">
        To:
      </label>
      <input type="search" id="directrionBarInputTo" class="barInput"  list="stationList" :onchange="setTo_name"/>

      <datalist id="stationList" >
        <option v-for="station in getStations" :value="station.name" :key="station.name"/>
      </datalist>
<!--      <div v-for="station in getStations" :key="station.name">-->
<!--        <p>{{station}}</p>-->
<!--      </div>-->

      <div class="barButton" @click="drawRoute" style="border: black 2px solid; margin: 10px; width: 20%; height: 3%; background-color: transparent; text-align-all: center">
        Submit
      </div>

      <div style=" height: 20px; width: 50px; position: relative; margin: auto" v-if="found">
        <hr/>
        <label>
          Train:
        </label>
        duration: {{this.train_route.duration/60}} mins
      </div>
      <div style=" height: 20px; width: 50px; top: 500px; margin: auto" v-if="found">
        <hr/>
        <label>
          Car:
        </label>
        duration: {{Math.floor(this.car_route.duration/60)}} mins
      </div>

    </div>
    <div id="directionBarHandle">
      <div class="barHandle"/>
    </div>

  </div>
</template>

<script>
/* eslint-disable */
import axios from "axios";

export default {
  name: "DirectionBar",
  data() {
    return {
      found: Boolean,
      train_route: {},
      car_route: {}
    }
  },
  mounted() {
    this.found = false;
  },
  methods: {
    submitStations() {
      const from = document.getElementById('directrionBarInputFrom').getAttribute('value');
      const to = document.getElementById('directrionBarInputTo').getAttribute('value');
      this.$store.commit('setPoints', from, to);
    },
    drawRoutet() {
      this.getRoute_train();
      this.getRoute_car();
      this.found = true;
    },
    async drawRoute() {
      let query = await axios({
        method: "get",
        url: `http://localhost:80/direction/${this.$store.state.points.from.station.name}/${this.$store.state.points.to.station.name}`
      }).then((resp)=> {
        return resp.data
      })
      let resp = await query;
      this.drawRouteCar(resp.car);
      this.drawRouteTrain(resp.train);
      this.found = true;

    },
    drawRouteTrain(route) {
      let map = this.$store.state.map;
      this.train_route = route;
      if (map.getSource('route_train')) {
        map.getSource('route_train').setData(route.geojson);
      }
      else {
        map.addLayer({
          id: 'route_train',
          type: 'line',
          source: {
            type: 'geojson',
            data: route.geojson,
          },
          layout: {
            'line-join': 'round',
            'line-cap': 'round'
          },
          paint: {
            'line-color': '#0000ff',
            'line-width': 5,
            'line-opacity': 0.75
          }
        });
      }
    },
    drawRouteCar(route){
      let map = this.$store.state.map;
      this.car_route = route;
      if (map.getSource('route_car')) {
        map.getSource('route_car').setData(route.geojson);
      }
      else {
        map.addLayer({
          id: 'route_car',
          type: 'line',
          source: {
            type: 'geojson',
            data: route.geojson
          },
          layout: {
            'line-join': 'round',
            'line-cap': 'round'
          },
          paint: {
            'line-color': '#000000',
            'line-width': 5,
            'line-opacity': 0.75
          }
        });
      }
    },
    async getRoute_train(){
      let points = this.$store.state.points;
      let date = new Date();
      console.log(this.$store.state.points.from.station.name, this.$store.state.points.to.station.name)
      let hour = date.getHours(); if(hour < 10) {hour = "0" + hour}
      let minutes = date.getMinutes(); if(minutes < 10){ minutes = "0" + minutes}
      let day = date.getDate(); if (day < 10) {day = "0" + day}
      let month = date.getMonth() + 1; if (month < 10) {month = "0" + month}
      let year = "" + date.getFullYear(); year = year.slice(2, 4);
      let query = await axios({
        method: 'get',
        url: `https://api.irail.be/connections?from=${this.$store.state.points.from.station.name}&to=${this.$store.state.points.to.station.name}&format=json&lang=en&results=2`
      }).then((response) => {
        console.log("getroute_train", response.data);
        return response.data;
      }).catch((e)=> {console.warn(e)});
      let resp = await query
      console.log("trying train now", resp.connection[0]);
      let vias = [];
      this.train_route = resp.connection[0];
      try{
        vias = resp.connection[0].vias.via;
      } catch (e){}
      let route = [points.from.coord];
      vias.map((via) => {
        route.push([via.stationinfo.locationX, via.stationinfo.locationY]);
      })
      const geojson = {
        type: 'Feature',
        properties: {},
        geometry: {
          type: 'LineString',
          coordinates: route,
        }
      }
      route.push(points.to.coord)
      let map = this.$store.state.map;
      if (map.getSource('route_train')) {
        map.getSource('route_train').setData(geojson);
      }
      else {
        map.addLayer({
          id: 'route_train',
          type: 'line',
          source: {
            type: 'geojson',
            data: geojson,
          },
          layout: {
            'line-join': 'round',
            'line-cap': 'round'
          },
          paint: {
            'line-color': '#0000ff',
            'line-width': 5,
            'line-opacity': 0.75
          }
        });
      }
      console.log("train should work")
    },
    async getRoute_car() {
      let points = this.$store.state.points;
      let query = await axios({
        method: 'get',
        url: `https://api.mapbox.com/directions/v5/mapbox/driving/${points.from.coord[0]},${points.from.coord[1]};${points.to.coord[0]},${points.to.coord[1]}?alternatives=false&geometries=geojson&overview=full&steps=false&access_token=pk.eyJ1IjoicHBwYzEzMTIiLCJhIjoiY2wxNTk0dGR0MHl6NzNkczBxNzRxbTczNSJ9.qFzM1Q2oov0E6rFbDodAdQ`,
      }).then((response)=> {
        return response.data;
      }).catch((e) =>{console.warn(e)});
      console.log("got directions from mapbox")
      const json = await query;
      const data = json.routes[0];
      this.car_route = data;
      const route = data.geometry.coordinates;
      console.log("route", route, data)
      const geojson = {
        type: 'Feature',
        properties: {},
        geometry: {
          type: 'LineString',
          coordinates: route,
        }
      };
      let map = this.$store.state.map;
      if (map.getSource('route_car')) {
        map.getSource('route_car').setData(geojson);
      }
      else {
        map.addLayer({
          id: 'route_car',
          type: 'line',
          source: {
            type: 'geojson',
            data: geojson
          },
          layout: {
            'line-join': 'round',
            'line-cap': 'round'
          },
          paint: {
            'line-color': '#000000',
            'line-width': 5,
            'line-opacity': 0.75
          }
        });
      }
    },
    setFrom_name() {
      console.log("frojm")
      this.clearDirections()
      this.$store.commit("setFrom_name", document.getElementById("directrionBarInputFrom").value);
    },
    setTo_name() {
      this.clearDirections()
      this.$store.commit("setTo_name", document.getElementById("directrionBarInputTo").value);
    },
    clearDirections() {
      this.found= false;
      let map = this.$store.state.map;
      if (map.getSource('route_car')) {
        map.getSource('route_car').setData({
          type: 'Feature',
          properties: {},
          geometry: {
            type: 'LineString',
            coordinates: [],
          }
        });
      }
      if (map.getSource('route_train')) {
        map.getSource('route_train').setData({
          type: 'Feature',
          properties: {},
          geometry: {
            type: 'LineString',
            coordinates: [],
          }
        });
      }
    },
  },
  computed: {
    getStations() {
      return this.$store.state.stations;
    },
    getMap() {
      console.log("map?")
      return this.$store.state.map;
    }
  }
}

</script>

<style scoped lang="scss">



#inputBar {
  width: 20vw;
  height: 100%;
  background-color: transparent;
  margin-top: 8px;
  overflow: scroll;
  display: flex;
  flex-direction: column;
  align-items: center;

  -ms-overflow-style: none;
  scrollbar-width: none;
}

#inputBar::-webkit-scrollbar {
  display: none;
}

#directionBarHandle {
  display: flex;
  flex-direction: column;
  border-radius: 0 15px 15px 0;
}

#directionBar {
  border-radius: 0 25px 25px 0;
  position: absolute;
  display: flex;
  flex-direction: row;
  height: 95%;
  width: 20%;
  top: 2.5%;
  background-color: #fff9;
  backdrop-filter: blur(8px)
}

.barHandle {
  background-color: dimgray;
  width: 3px;
  height: 10vh;
  margin: auto;
  border-radius: 25px;
}

.barButton {
  background-color: red;
  width: 20px;
  height:5px
}

.barInput {

}

</style>