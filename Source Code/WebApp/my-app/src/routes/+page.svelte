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

<div id="fieldbox">
    <div id="fieldbox-content">
        <div id = "heading">
            <h2>Login/Register User</h2>
        </div>
        <div id="login">
            <input bind:value={username} placeholder="Enter Username..."/>
            <button on:click={loginPressed}>Login</button>
        </div>
        
        <div id="register">
            <input bind:value={username} placeholder="Enter Username..."/>
            <button on:click={registerPressed}>Register</button>
        </div>
    </div>
</div>



<style>
    #fieldbox {
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 25vh;
        height: 50vh;
        background-color: #EDEDED;
        border-radius: 8px;
        font-family: 'Franklin Gothic Light';
    }
    #fieldbox-content{
        text-align: center;
    }
    #heading {
        width: 100%;
        height: 100%;
        text-align: center;
    }
    #login {
        width: 100%;
        height: 100%;
        text-align: center;
    }
    #register {
        width: 100%;
        height: 100%;
        text-align: center;
    }
</style>