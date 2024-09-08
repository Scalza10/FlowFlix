<template>
  <div class="dashboard-container">
    <div class="dashboard-card">
      <h1>Dashboard</h1>
      <p>Welcome, {{ username }}! Welcome to your dashboard!</p>
      <div class="dashboard-content">
        <div class="dashboard-section">
          <h2>Overview</h2>
          <p>
            Here you can find an overview of your activities and statistics.
          </p>
        </div>
        <div class="dashboard-section">
          <h2>Recent Activities</h2>
          <ul>
            <li>Activity 1</li>
            <li>Activity 2</li>
            <li>Activity 3</li>
          </ul>
        </div>
        <div class="dashboard-section">
          <h2>Quick Actions</h2>
          <button class="action-button">Action 1</button>
          <button class="action-button">Action 2</button>
        </div>
      </div>
      <button @click="handleLogout" class="logout-button">Logout</button>
    </div>
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
.dashboard-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background: linear-gradient(to right, #4e4eff, #920092);
  min-height: 100vh;
}

.dashboard-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 800px;
  width: 100%;
  text-align: center;
}

h1 {
  margin-bottom: 20px;
  color: #333;
}

.dashboard-content {
  text-align: left;
}

.dashboard-section {
  margin-bottom: 20px;
}

.dashboard-section h2 {
  color: #42b983;
  margin-bottom: 10px;
}

.dashboard-section p,
.dashboard-section ul {
  color: #333;
}

.dashboard-section ul {
  list-style-type: none;
  padding: 0;
}

.dashboard-section ul li {
  margin-bottom: 5px;
}

.action-button {
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-right: 10px;
}

.action-button:hover {
  background-color: #369f6b;
}

.logout-button {
  width: 100%;
  padding: 10px;
  background-color: #ff4e4e;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-top: 20px;
}

.logout-button:hover {
  background-color: #d43f3f;
}
</style>