<script>    


</script>

<template>
    <main>
        <div class="container">
            <h1>You are succesfuly logged out!</h1>
            <RouterLink to='/' class="redirect">Home</RouterLink>
        </div>
    </main>
</template>

<style scoped>

main {
    text-align: center;

}

.container { 
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

}

.redirect { 
    text-decoration: none;
    color: black;
    margin: 2em;
    border-style: solid 1px black;
}
</style>
