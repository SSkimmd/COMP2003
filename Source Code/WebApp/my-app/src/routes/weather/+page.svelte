<script>
  import { json } from "@sveltejs/kit";
  import { onMount } from "svelte";
  import Navigation from "../../components/navigation.svelte";
  import FluentWeatherFog48Filled from '~icons/fluent/weather-fog-48-filled';
  import IonReturnDownBackSharp from '~icons/ion/return-down-back-sharp';
  import { goto } from '$app/navigation';
  import { GetLocation, UpdateLocation, GetWeather, GetMoon, GetHumidity, GetTemp, GetSunRise, GetSunSet, GetUV, GetWind } from "$lib/weather"

  var currentLocation = '';

  onMount(async () => {
    await GetLocation().then(location => {
      currentLocation = location;
    });
  });

  function backPressed() {
    goto('/home');
  }

  async function updateLocation() {
    await UpdateLocation(currentLocation);
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
      <div id="current-location">
          <p style='font-size: large;'>Current Location</p>
          <input placeholder={currentLocation} bind:value={currentLocation}/>
          <button on:click={updateLocation}>Update</button>
      </div>
      <div id="weather-box">
          <div id="weather"class="border">
            <p>{#await GetWeather()} Loading... {:then temp} {temp} {/await}</p>
            <p>Temperature: {#await GetTemp()} Loading... {:then temp} {temp}°C {/await}</p>
          </div>
      </div>
      <div class="vertical-container">
      <div id="temporary" class="border right-box">
              <p>TEMP</p>
      </div>
      <div id="sunrise-sunset" class="border right-box">
          <p>Sunrise: {#await GetSunRise()} Loading... {:then temp} {temp} {/await}</p>
          <p>Sunset: {#await GetSunSet()} Loading... {:then temp} {temp} {/await}</p>
      </div>
      <div id="moon-phase" class="border right-box">
          <p>Moon Phase: {#await GetMoon()} Loading... {:then temp} {temp} {/await}</p>
      </div>
    </div>
      <div id="extra-info">
          <div id="uv" class="border">
              <p>UV: {#await GetUV()} Loading... {:then temp} {temp} {/await}</p>
          </div>
          <div id="wind" class="border">
              <p>Wind Speed: {#await GetWind()} Loading... {:then temp} {temp} {/await}</p>
          </div>
          <div id="humidity" class="border">
              <p>Humidity: {#await GetHumidity()} Loading... {:then temp} {temp} {/await}</p>
          </div>
      </div>
  </div>
</div>


<style>
  #device-content {
      margin:25px;
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

  #current-location {}

  #weather-box {
    width: 35%;
    height: 475px;
    display: inline-block;
    vertical-align: top;
  }

  #temporary {
    width: 100%;
    display: inline-block;
    vertical-align: top;
    margin-left: 10px;
  }

  #weather {
    margin-bottom: 5px;
     height:288px;
      
  }

  #sunrise-sunset {
      width: 100%;
      display: inline-block;
      vertical-align: top;
      margin-left: 10px;
  }

  #moon-phase {
    margin-bottom: 5px;
    margin-left: 10px;
    width: 100%;
  }

  #extra-info div {
    width: 30%;
    display: inline-block;
    padding: 10px;
    margin-top: 10px;
  }

  .border {
  border: 0.5px solid black;
}

.right-box{
  height: 95px;
}

.vertical-container{
  width: 62%;
  height:95px;
  display: inline-block;
}
</style>
