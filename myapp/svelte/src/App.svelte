<script>
    export let dict;
    console.log(dict);
    let count = 0;
</script>

<main>
    {dict.message}
    <p>The value is  {count}</p>
    <button on:click={()=>count++}>Add</button>
    <button on:click={()=>count--}>SUBRACT</button>
    <button on:click={()=>count*=100}>Multiply</button>
    <button on:click={()=>count/=100}>Divide</button>
</main>

<style>
    p{
        color: red;
    }
</style>