import {createStore} from "vuex";
import mapboxgl from 'mapbox-gl';

const store = createStore({
  state() {
    return {
      stations: [],
      points: {
        from: {
          station: {},
          marker: {},
          coord: [],
        },
        to: {
          station: {},
          marker: {},
          coord: [],
        },
      },
      map: {},
    };
  },
  mutations: {
    setStations(state, values) {
      state.stations = values;
    },
    setPoints(state, from, to) {
      state.points.from.station = from;
      state.points.to.station = to;
      state.points.from.coord = [ state.points.from.station.locationX, state.points.from.station.locationY]
      state.points.to.coord = [ state.points.to.station.locationX, state.points.to.station.locationY]
      state.points.from.marker.remove();
      state.points.to.marker.remove();
      state.points.from.marker = new mapboxgl.Marker().setLngLat(state.points.from.coord).addTo(state.map)
      state.points.to.marker = new mapboxgl.Marker().setLngLat(state.points.to.coord).addTo(state.map)
    },
    setMap(state, map) {
      state.map = map;
    },
    setMarkers(state, markers) {
      state.markers.to.remove();
      state.markers.from.remove();
      state.markers = markers;
    },
    setFrom_name(state, name) {
      try {
        state.points.from.marker.remove();
      } catch {console.log()}
      state.stations.map((station) => {
        if (station.name === name) {
          state.points.from.station = station;
          state.points.from.coord = [station.locationX, station.locationY];
          state.points.from.marker = new mapboxgl.Marker().setLngLat(state.points.from.coord).addTo(state.map);
        }
      });
    },
    setTo_name(state, name) {
      try {
        state.points.to.marker.remove();
      } catch {console.log()}
      state.stations.map((station) => {
        if (station.name === name) {
          state.points.to.station = station;
          state.points.to.coord = [station.locationX, station.locationY];
          state.points.to.marker = new mapboxgl.Marker().setLngLat(state.points.to.coord).addTo(state.map);
        }
      });
    },
    setPoints_name(state, from, to) {
      state.setFrom_name(state,from);
      state.setTo_name(state, to);
    }
  }
})

export default store