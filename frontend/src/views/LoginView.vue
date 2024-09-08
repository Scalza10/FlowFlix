<template>
  <div class="login">
    <h1>Login</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Login</button>
    </form>
    <p v-if="message">{{ message }}</p>
    <router-link to="/register">
      <button>Go to Register</button>
    </router-link>
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
          this.message = response.data.message || "Login successful!";
          if (response.data.access_token) {
            // Use the Vuex 'login' action mapped earlier
            await this.login(response.data.access_token);
            this.$router.push("/dashboard");
          } else {
            throw new Error("Access token not found");
          }
        } else {
          this.message = "Invalid response from the server.";
        }
      } catch (error) {
        console.log(error);
        if (error.response && error.response.data) {
          this.message = error.response.data.message || "Login failed.";
        } else if (error.message) {
          this.message = error.message;
        } else {
          this.message = "An error occurred. Please try again.";
        }
      }
    },
  },
};
</script>

<style scoped>
.login {
  padding: 20px;
}

.login h1 {
  color: #2c3e50;
}

.login form {
  display: flex;
  flex-direction: column;
}

.login form div {
  margin-bottom: 10px;
}

.login form label {
  margin-right: 10px;
}

.login form input {
  padding: 5px;
  font-size: 16px;
}

.login form button {
  padding: 10px;
  font-size: 16px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}

.login form button:hover {
  background-color: #369f6b;
}

.login p {
  margin-top: 20px;
  color: #42b983;
}

.router-link button {
  margin-top: 10px;
  padding: 10px;
  font-size: 16px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}

.router-link button:hover {
  background-color: #369f6b;
}
</style>
