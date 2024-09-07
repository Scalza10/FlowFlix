<template>
  <div class="register">
    <h1>Register</h1>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Register</button>
    </form>
    <p v-if="message">{{ message }}</p>
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
.register {
  padding: 20px;
}

.register h1 {
  color: #2c3e50;
}

.register form {
  display: flex;
  flex-direction: column;
}

.register form div {
  margin-bottom: 10px;
}

.register form label {
  margin-right: 10px;
}

.register form input {
  padding: 5px;
  font-size: 16px;
}

.register form button {
  padding: 10px;
  font-size: 16px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}

.register form button:hover {
  background-color: #369f6b;
}
</style>
