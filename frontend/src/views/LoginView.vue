<template>
    <div>
        <h1>Login</h1>
            <label for="username">Username:</label><br>
            <input type="text" id="username" name="username" v-model="username"><br>
            <label for="password">Password:</label><br>
            <input type="password" id="password" name="password" v-model="password"><br><br>
            <button @click="login">Login</button>
    </div>
</template>

<script>

export default {
    name: 'LoginView',
    data() {
        return {
            username: '',
            password: ''
        }
    },
    methods: {
        login() {
            console.log('login')
        }
    }
}

</script>