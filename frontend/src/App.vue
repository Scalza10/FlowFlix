<template>
  <div id="app">
    <nav>
      <div class="nav-container">
        <!-- Logo -->
        <div class="logo">
          <router-link to="/">
            <img src="@/assets/logo.png" alt="Logo" class="logo-img" />
          </router-link>
        </div>

        <!-- Navigation Links -->
        <div class="nav-links">
          <router-link to="/" class="nav-link" active-class="active-link">Home</router-link>
          <router-link to="/about" class="nav-link" active-class="active-link">About</router-link>
          <router-link to="/dashboard" class="nav-link" active-class="active-link">Dashboard</router-link>
          <!-- <router-link to="/faqs" class="nav-link" active-class="active-link">FAQs</router-link> -->
        </div>

        <!-- Join Waitlist Button -->
        <div class="join-btn-container">
          <button class="join-btn">Join the Waitlist</button>
        </div>
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
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background: linear-gradient(to right, #4e4eff, #920092); /* Background gradient */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

nav {
  background-color: #ff6c00; /* Matches the orange in the image */
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.nav-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 1200px;
}

.logo {
  display: flex;
  align-items: center;
}

.logo-img {
  height: 40px; /* Adjust height for the logo */
}

.nav-links {
  display: flex;
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
  white-space: nowrap; /* Prevent ellipsis by ensuring text doesn't wrap */
}

.nav-link:hover {
  background-color: #42b983;
  color: white;
}

.active-link {
  text-decoration: underline; /* Underline for active link */
}

.join-btn-container {
  display: flex;
  justify-content: flex-end;
}

.join-btn {
  background-color: white;
  color: #ff6c00;
  border: 2px solid white;
  padding: 10px 20px;
  border-radius: 20px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.join-btn:hover {
  background-color: #ff914d;
  color: white;
}
</style>
