<script>
    import { goto } from "$app/navigation";
    import { Register, Login } from "$lib/index"

    var username = '';

    async function registerPressed() {
        await Register().then((data) => {
            console.log(data)
        }) 
    }

    async function loginPressed() {
        const loggedIn = await Login()

        if(loggedIn) {
            goto("/home")
        }
    }
</script>

<div id="register">
    <input bind:value={username} placeholder="Enter Username..."/>
    <button on:click={registerPressed}>Register</button>
</div>

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