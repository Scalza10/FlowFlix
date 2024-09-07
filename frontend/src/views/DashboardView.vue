<template>
  <div class="dashboard">
    <h1>Dashboard</h1>
    <p>Welcome, {{ username }}! Welcome to your dashboard!</p>
    <!-- Add more dashboard content here -->
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
export default {
  name: 'DashboardView',
  props: {
    username: {
      type: String,
      required: true
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('access_token');
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