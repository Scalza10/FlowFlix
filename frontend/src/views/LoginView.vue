<template>
  <div class="login-container">
    <div class="login-card">
      <h1>Login</h1>
      <form @submit.prevent="handleLogin">
        <div class="input-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div class="input-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div class="actions">
          <button type="submit" class="login-button">Login</button>
          <router-link to="/register">
            <button type="button" class="register-button">Register</button>
          </router-link>
        </div>
      </form>
      <p v-if="message" class="message">{{ message }}</p>
      <p class="forgot-password">Forgot your password?</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { mapActions } from 'vuex';

export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
      message: "",
    };
  },
  methods: {
    ...mapActions(["login"]), // Map the 'login' action from Vuex

    async handleLogin() {
      try {
        const response = await axios.post("/api/login", {
          username: this.username,
          password: this.password,
        });

        if (response && response.data) {
          this.message = response.data.message;
          this.$store.dispatch('login', response.data.access_token);
          this.$router.push('/dashboard');
        }
      } catch (error) {
        if (error.response) {
          this.message = error.response.data.message;
        } else {
          this.message = 'An error occurred. Please try again.';
        }
      }
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(to right, #4e4eff, #920092);
}

.login-card {
  background: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  width: 300px;
}

h1 {
  margin-bottom: 20px;
  color: #333;
}

.input-group {
  margin-bottom: 15px;
  text-align: left;
}

.input-group label {
  display: block;
  margin-bottom: 5px;
  color: #333;
}

.input-group input {
  width: 75%; /* Set the width to 75% of the login-card */
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin: 0 auto; /* Center the input */
  display: block; /* Center the input */
}

.actions {
  display: flex;
  justify-content: space-evenly;
  margin-top: 20px;
}

.login-button, .register-button {
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  width: 100px;
}

.login-button:hover, .register-button:hover {
  background-color: #369f6b;
}

.message {
  margin-top: 20px;
  color: #42b983;
}

.forgot-password {
  margin-top: 10px;
  color: #333;
  cursor: pointer;
}
</style>