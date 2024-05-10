<script>
    import { goto } from "$app/navigation";
    import { Register, Login } from "$lib/index"

    var username = ''; //Switch away from these variables when backend authentication worked out
    var password = '';

    //Switch to the below variables once authentication is sorted
    var loginUsername = '';
    var loginPassword = '';
    var regUsername = '';
    var regPassword = '';


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
        <div id = "login-heading">
            <h2>Login</h2>
        </div>
        <div id="login">
            <input bind:value={username} placeholder="Enter Username..."/>
            <br>
            <input bind:value={password} placeholder="Enter Password..."/>
            <br>
            <button on:click={loginPressed}>Login</button>
        </div>
        <div id = "reg-heading">
            <h2>Register</h2>
        </div>
        <div id="register">
            <input bind:value={username} placeholder="Enter Username..."/>
            <br>
            <input bind:value={password} placeholder="Enter Password..."/>
            <br>
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
        width: 25vw;
        height: 40vh;
        background-color: #EDEDED;
        border-radius: 8px;
        font-family: 'Franklin Gothic Light';
        min-width: fit-content;
        min-height: fit-content;
        
    }
    #fieldbox-content{
        min-height: fit-content;
        min-width: fit-content;
        text-align: center;
        text-justify: center;
    }
    #login-heading {
        width: 100%;
        height: 100%;
        text-align: center;
    }
    #reg-heading {
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
    input{
        width: 30vh;
        height: 2.5vh;
        margin: 10px;
    }
    button {
        width: 10vh;
        height: 2.5vh;
        background-color: #444444;
        color: #FFFFFF;
    }
</style>