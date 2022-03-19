<template>
  <ul>
    <li>eeek</li>
  </ul>
</template>

<script lang="ts">
export default {
  name: 'NavBar',
  data () {

  },
  computed: {
    currentRouteName() {
      return this.$route.name;
    }
  },
  props: {
    routes: [],
  }
}


</script>