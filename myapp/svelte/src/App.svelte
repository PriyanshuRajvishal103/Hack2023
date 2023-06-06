<script>
    let count = 0;
</script>

<main>
    <p>Its an app !</p>
    <p>You have clicked {count} time</p>
    <button on:click={()=>count++}>Add</button>
    <button on:click={()=>count--}>SUBRACT</button>
</main>

<style>
    p{
        color: red;
    }
</style>