<script>
// @ts-nocheck


  import { json } from "@sveltejs/kit";
  import { onMount } from "svelte";
  import Navigation from "../../components/navigation.svelte";
  import RiDeviceFill from '~icons/ri/device-fill';
  import IonReturnDownBackSharp from '~icons/ion/return-down-back-sharp';
  import { goto } from '$app/navigation';
  import { GetDevices } from "$lib/device"

  function backPressed() {
    goto('/home')
  }
</script>

<div>
  <Navigation/>
</div>

<div id="device">
  <button on:click={backPressed}>
    <IonReturnDownBackSharp style='width: 30px; height: 30px;'/>
  </button>
  
  <RiDeviceFill style='position: absolute; margin-top: 20px; margin-left: 70px; width: 30px; height: 30px;'/>
  <p style='margin-left: 120px; margin-top: 20px; font-size: 24px;'><b>Device</b></p>

  <div id="device-content">
      <p style='font-size: x-large; text-align: center; font-size: 24px;'><b>Device Information</b></p>
      {#await GetDevices()}
        <p>Loading...</p>
      {:then devices}
          {#each devices as device}
            <p>{device.name}</p>
          {/each}
      {/await}
  </div>
</div>

<style>
  #device-content {
    margin-left: 25px;
    margin-top: 25px;
    text-align: center;
  }

  #device {
    position: absolute;
      margin-top: 35px;
      margin-bottom: 35px;
      min-width: 50px;
      width: 99%;
      height: 80%;
      background-color: #EDEDED;
      border-radius: 8px;
      box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;

    font-family: 'Century751-Roman';
  }

  button {
        position: absolute;
        width: 40px;
        height: 40px;
        top: 20px;
        left: 20px;
        background-color: transparent;
        border: none;
        cursor: pointer;
        overflow: hidden;
        border-radius: 50%;
        transition: border-color 0.3s ease;
        border: 2px solid transparent;
        padding: 0; 
        margin: 0; 
    }

    button:hover {
        border-color: #000;
    }

</style>