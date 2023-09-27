<script setup>
import navbar from './components/navbar.vue'
import { RouterView } from 'vue-router';

</script>

<template>
  <main>
    <navbar/>
    <RouterView/>
  </main>
</template>

<style scoped>
main { 
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
</style>