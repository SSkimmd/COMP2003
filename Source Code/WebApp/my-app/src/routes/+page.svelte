<script>
    import { goto } from "$app/navigation";

    var username = '';

    function loginPressed() {
        console.log(username)
        goto('/home');
    }
</script>

<div id="login">
    <input bind:value={username} placeholder="Enter Username..."/>
    <button on:click={loginPressed}>Login</button>
</div>

<style>
    #login {
        width: 100%;
        height: 100%;
    }
</style>