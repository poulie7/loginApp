<script setup>

import axios from 'axios'
import {ref, onMounted} from 'vue'
import Cookies from 'js-cookie';

const email = ref("poulie");
const password = ref("1234");
axios.defaults.withCredentials = true



function login() {
    axios.post('http://127.0.0.1:8000/api/login/', {
        username: email.value,
        password: password.value,
    })
}
</script>

<template>
    <main>
        <h1>Login</h1>
    <div class="container">
        <form>
        
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" v-model="email" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password" name="password" v-model="password" required>
            </div>
        
        </form>
             <div class="form-group">
                <button type="submit" @click="login">Login</button>
            </div>
    </div>
        
    </main>
</template>

<style scoped>
h1{
    margin-top: 2em;
    margin-bottom: 1em;
}
main { 
    text-align: center;
}

.container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 2px solid #000000;
    border-radius: 10px;
    background-color: #ffffff;
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    font-weight: bold;
    margin-bottom: 5px;
}

.form-group input {
    width: 100%;
    padding: 10px;
    border: 1px solid #000000;
    border-radius: 5px;
}

.form-group button {
    background-color: #000000;
    color: #ffffff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

.form-group button:hover {
    background-color: #333333;
}

</style>