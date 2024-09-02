<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png">
    <HomeDashboard/>
  </div>
</template>

<script>
import HomeDashboard from '../components/HomeDashboard.vue';

export default {
  name: 'HomeView',
  components: {
    HomeDashboard,
  },
};
</script>
