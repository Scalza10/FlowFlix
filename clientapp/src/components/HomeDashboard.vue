<template>
    <div class="home-dashboard">
        <h1>Home Dashboard</h1>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomeDashboard',
  data() {
    return {
      msg: 'Welcome to the Home Dashboard',
    };
  },

  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://localhost:5000/api/msg');
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    },
  },
  mounted() {
    this.fetchData();
  },
};
</script>
