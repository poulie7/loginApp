<script setup>
import axios from 'axios'
import {ref, onMounted} from 'vue'

const firstName = ref("Pavel");
const lastName = ref("Lexmaul");
const email = ref("pavel@gmail.cz");
const username = ref("poulie");
const password = ref("1234");


function register() { 
    axios.post('http://127.0.0.1:8000/api/register', { 
        first_name: firstName.value,
        last_name: lastName.value,
        email: email.value,
        username: username.value,
        password: password.value,
  
    })
}

</script>

<template>
    <main>
        <h1>Sign Up</h1>
    <div class="formContainer">
        <form>
            <div class="form-group">
                <label for="first-name">First Name:</label>
                <input type="text" id="first-name" name="first-name" v-model="firstName" required>
            </div>
            <div class="form-group">
                <label for="last-name">Last Name:</label>
                <input type="text" id="last-name" name="last-name" v-model="lastName" required>
            </div>
            <div class="form-group">
                <label for="email">email:</label>
                <input type="text" id="email" name="email" v-model="email" required>
            </div>
            <div class="form-group">
                <label for="username">Username:</label>
                <input type="text" id="username" name="username" v-model="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password:</label>
                <input type="password" id="password1" name="password1" v-model="password" required>
            </div>
          
        </form>
        <div class="form-group">
                <button type="submit" @click="register">Sign Up</button>
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

.formContainer {
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