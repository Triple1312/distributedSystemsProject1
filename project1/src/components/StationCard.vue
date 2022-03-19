<template>
  <div class="stationCard">
    {{station}}
  </div>
</template>

<script>
export default {
  name: "StationCard",
  props: {
    station: Object,
  }
}
</script>

<style scoped>

.stationCard {
  width: 300px;
  height: 200px;
  -webkit-backdrop-filter: blur(10px);
  backdrop-filter: blur(10px);
  border-radius: 15px;
  margin: 10px auto;

  /*box-shadow: 0 0 40px #999;*/
  background-color: lime;

  /*Flex*/
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
}

</style>