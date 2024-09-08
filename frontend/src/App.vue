<template>
  <div id="app">
    <nav>
      <div class="nav-container">
        <router-link to="/" class="nav-link" active-class="active-link">Home</router-link>
        <router-link to="/about" class="nav-link" active-class="active-link">About</router-link>
        <router-link to="/dashboard" class="nav-link" active-class="active-link">Dashboard</router-link>
      </div>
    </nav>
    <router-view :username="username"/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  name: 'App',
  computed: {
    ...mapGetters(['username'])
  },
  created() {
    this.$store.dispatch('initialize');
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: linear-gradient(to right, #4e4eff, #920092); /* Background gradient */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

nav {
  padding: 20px;
}

.nav-container {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.nav-link {
  padding: 10px 20px;
  border-radius: 20px;
  background-color: #ffffff;
  color: #2c3e50;
  text-decoration: none;
  font-weight: bold;
  transition: background-color 0.3s, color 0.3s;
}

.nav-link:hover {
  background-color: #42b983;
  color: white;
}

.active-link {
  background-color: #42b983;
  color: white;
}
</style>