<template>
  <div class="register-container">
    <div class="register-card">
      <h1>Register</h1>
      <form @submit.prevent="register">
        <div class="input-group">
          <label for="username">Username:</label>
          <input type="text" id="username" v-model="username" required />
        </div>
        <div class="input-group">
          <label for="email">Email:</label>
          <input type="email" id="email" v-model="email" required />
        </div>
        <div class="input-group">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" required />
        </div>
        <div class="actions">
          <button type="submit" class="register-button">Register</button>
          <router-link to="/login">
            <button type="button" class="login-button">Login</button>
          </router-link>
        </div>
      </form>
      <p v-if="message" class="message">{{ message }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "RegisterView",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      message: ''
    };
  },
  methods: {
    async register() {
      try {
        const response = await fetch("/api/register", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: this.username,
            email: this.email,
            password: this.password,
          }),
        });

        if (response.ok) {
          const data = await response.json();
          this.message = data.message;
          await new Promise((resolve) => setTimeout(resolve, 5000));
          this.$store.dispatch('login', data.access_token);
          this.$router.push('/dashboard');
        } else {
          const errorData = await response.json();
          this.message = errorData.message;
        }
      } catch (error) {
        this.message = "An error occurred. Please try again.";
      }
    },
  },
};
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(to right, #4e4eff, #920092);
}

.register-card {
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
  width: 75%; /* Set the width to 75% of the register-card */
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

.register-button, .login-button {
  width: 75px;
  padding: 10px;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.register-button:hover, .login-button:hover {
  background-color: #369f6b;
}

.message {
  margin-top: 20px;
  color: #42b983;
}
</style>