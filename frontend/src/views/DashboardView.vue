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
          <button class="action-button" @click="showModal = true">Action 1</button>
          <button class="action-button">Action 2</button>
        </div>
      </div>
      <button @click="handleLogout" class="logout-button">Logout</button>
    </div>

    <!-- Modal -->
    <div v-if="showModal" class="modal-overlay">
      <div class="modal">
        <h2>Send Email</h2>
        <p>Enter the email address you would like to send the mail to:</p>
        <input type="email" v-model="email" placeholder="Email address" />
        <div class="modal-actions">
          <button @click="sendEmail" class="modal-button">Send</button>
          <button @click="showModal = false" class="modal-button">Cancel</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { mapGetters, mapActions } from 'vuex';

export default {
  name: 'DashboardView',
  data() {
    return {
      showModal: false,
      email: ''
    };
  },
  computed: {
    ...mapGetters(['username'])
  },
  methods: {
    ...mapActions(['logout']),
    handleLogout() {
      this.logout();
      this.$router.push('/login');
    },
    async sendEmail() {
      if (this.username === 'admin') {
        try {
          const response = await axios.get(`api/sendEmailCode?email=${this.email}`);
          alert('Email sent successfully', response.data);
        } catch (error) {
          alert('Error sending email', error);
        }
      } else {
        alert('Only admin can send email');
      }
      this.showModal = false;
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

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  max-width: 400px;
  width: 100%;
  text-align: center;
}

.modal-actions {
  margin-top: 20px;
  display: flex;
  justify-content: space-between;
}

.modal-button {
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.modal-button:hover {
  background-color: #369f6b;
}
</style>