<script>
  import { json } from "@sveltejs/kit";
  import { onMount } from "svelte";

  const endpoint = "http://192.168.0.19:5000/login";

  let message = '';
  let returnData = 'Offline';

  async function Send() {
    const user = {
      "username": "testusername",
      "data": message
    };

    const userdata = JSON.stringify(user)

    const response = await fetch(endpoint, {
        method: 'POST',
        mode: 'cors',
        body: userdata
    })

    const json = await response.json()
    returnData = json["ID"]  
  }
</script>

<input bind:value={message}/>
<button on:click={Send}>Send</button>
<button>{returnData}</button>