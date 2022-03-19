<template>
  <div id="directionBar">
    From:
    <input id="directrionBarInputFrom" class="barInput" type="text" />
    To:
    <input id="directrionBarInputTo" class="barInput" type="text" />
    <div class="barButton" @click=""/>
  </div>
  <div id="directionBarHandle">
    <div class="barHandle"/>
  </div>
</template>

<script lang="ts">
export default {
  name: "DirectionBar",
  props: {
    submit: Function,
  }
}
</script>

<style scoped>

#directionBar {
  width: 20vw;
  height: 100%;
  background-color: blue;
  display: flex;
  flex-direction: column;
  align-items: center;
}

#directionBarHandle {
  display: flex;
  flex-direction: column;
  border-radius: 0 15px 15px 0;
}

.barHandle {
  background-color: dimgray;
  width: 2vh;
  height: 10vh;
  margin: auto;
  border-radius: 25px;
}

.barButton {

}

.barInput {

}

</style>