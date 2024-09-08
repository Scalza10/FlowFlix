<template>
  <div class="dashboard">
    <h1>Dashboard</h1>
    <p>Welcome, {{ username }}! Welcome to your dashboard!</p>
    <!-- Add more dashboard content here -->
    <button @click="handleLogout">Logout</button>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'DashboardView',
  computed: {
    ...mapGetters(['username'])
  },
  methods: {
    ...mapActions(['logout']),
    handleLogout() {
      this.logout();
      this.$router.push('/login');
    }
  }
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
}

.dashboard h1 {
  color: #2c3e50;
}

.dashboard p {
  font-size: 16px;
}

.dashboard button {
  margin-top: 20px;
  padding: 10px;
  font-size: 16px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}

.dashboard button:hover {
  background-color: #369f6b;
}
</style>