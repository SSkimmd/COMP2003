<script>
  import { json } from "@sveltejs/kit";
  import { onMount } from "svelte";

  const endpoint = "http://192.168.0.19:5000/login";

  let username = '';
  let userID = 'Offline';
  let loggedIn = false;

  async function Login() {
    const user = {
      "username": username
    };

    const userdata = JSON.stringify(user)

    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    userID = json["ID"]  

    loggedIn = (userID !== "Offline")
  }
</script>

<input placeholder="Enter Username..." bind:value={username}/>
<button on:click={Login}>Login</button>
<button>{userID}</button>