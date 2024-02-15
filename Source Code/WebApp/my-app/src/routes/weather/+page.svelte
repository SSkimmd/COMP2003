<script>
    import { json } from "@sveltejs/kit";
    import { onMount } from "svelte";
    import Navigation from "../../components/navigation.svelte";
    import FluentWeatherFog48Filled from '~icons/fluent/weather-fog-48-filled';
    import IonReturnDownBackSharp from '~icons/ion/return-down-back-sharp';
    import { goto } from '$app/navigation';
    import { GetLocation, UpdateLocation } from "$lib/weather"
  
    var currentLocation = ''

    onMount(async () => {
      await GetLocation().then(location => {
        currentLocation = location
      })
    })

    function backPressed() {
      goto('/home')
    }

    async function updateLocation() {
      await UpdateLocation(currentLocation)
    }
  </script>


<div style='margin-top: 15vh;'>
    <Navigation/>
  </div>
  
  <div id="device">
    <button on:click={backPressed} style='position:absolute; width: 40px; 
    height: 40px; margin-top: 20px; margin-left: 20px; 
    background-color: transparent; border: none; cursor: pointer;'>
      <IonReturnDownBackSharp style='width: 30px; height: 30px;'/>
    </button>
    
    <FluentWeatherFog48Filled style='position: absolute; margin-top: 20px; margin-left: 70px; width: 30px; height: 30px;'/>
    <p style='margin-left: 120px; margin-top: 25px;'>Weather Settings</p>
  
    <div id="device-content">
      <p style='font-size: large;'>Current Location</p>
      <input placeholder={currentLocation} bind:value={currentLocation}/>
      <button on:click={updateLocation}>Update</button>
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
      margin-left: 456px;
      width: 1000px;
      height: 550px;
      background-color: #EDEDED;
      border-radius: 8px;
  
      font-family: 'Franklin Gothic Light';
    }
  </style>