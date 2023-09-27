<script setup>
import axios from 'axios';
import {onMounted, ref} from 'vue'

const articles = ref([])
async function fetchArticles() {
    const response = await axios.get('http://127.0.0.1:8000/api/article')
    return response.data
}

onMounted(async() => {
    const fetchedArticles = await fetchArticles()
    articles.value = fetchedArticles
    console.log(articles)
} ) 

</script>

<template>
    <main>
        <h1>Here are some data</h1>
        <div class="container">
            <p v-for="article in articles" :key="article.id">{{ article.article}}</p> 
    
        </div>
        </main>
</template>

<style scoped>

.container {
     display: flex;
     flex-direction: column;
     align-items: center;
}
h1 { 
    text-align: center;
}

p {
    border: 1px solid;
    width: 50px;
    height: 50px; 
    text-align: center;
}
</style>