<script setup>
import { RouterLink } from "vue-router"
import axios from "axios";


function logout() { 
    axios.get('http://127.0.0.1:8000/api/logout/' )
}

</script>

<template>
    <main>
        <div class="viewData">
           <RouterLink to="/">Home</RouterLink> 
           <RouterLink to="data">View Data</RouterLink> 
       </div>

        <div class="authentication">
            <RouterLink to="register">Register</RouterLink>
            <RouterLink to="login">Login</RouterLink>
            <RouterLink to="logout" @click="logout">Logout</RouterLink>
        </div>
    </main>
</template>

<style scoped>

main {
    height: 100px;
    background-color: black;
    min-width: 100%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0;
    box-sizing: border-box;
}

main a { 
    color: white;
    text-decoration: none;
}

.viewData a{
    margin: 1em;
}



.authentication a{
    margin: 1em;
}

</style>