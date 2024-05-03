<script>
    import { goto } from '$app/navigation';
    import FluentWeatherFog48Filled from '~icons/fluent/weather-fog-48-filled';
    import { GetLocation, UpdateLocation, GetWeather, GetMoon, GetHumidity, GetTemp, GetSunRise, GetSunSet, GetUV, GetWind, GetKind2, GetKind1,GetKind3,GetKind4 } from "$lib/weather"


    function openWeatherPressed() {
        goto("/weather");
    }

    /**
     * Function to prevent the button click event from bubbling up to the parent div
     * and triggering its click event.
     * @param {Event} event The click event
     */
     function stopPropagation(event) {
        event.stopPropagation();
    }


</script>

<div style='border-radius: 8px; background-color: #EDEDED; cursor: pointer; position: relative; transition: filter 0.7s ease;'>
    <button on:click={openWeatherPressed} on:click|preventDefault={stopPropagation} />
    <FluentWeatherFog48Filled style='position: absolute; margin-top: 20px; margin-left: 25px; width: 30px; height: 30px;'/>
    <p style='margin-left: 80px; margin-top: 25px;'>Weather</p>
    <p id="location">{#await GetLocation()} Loading... {:then temp} {temp} {/await}</p>
    <p id="temperature">{#await GetTemp()} Loading... {:then temp} {temp}°C {/await}</p>
    <p id="weather">{#await GetWeather()} Loading... {:then temp} {temp} {/await}</p>
    <p id="moon">{#await GetMoon()} Loading... {:then temp} {temp} {/await}</p>
</div>

<style>
    #weather {
        margin-left: 30px;
        font-size: medium;       
    }
    
    #moon {
        margin-left: 30px;
        font-size: medium;       
    }

    #temperature {
        margin-left: 30px;
        font-size: medium;       
    }

    #location {
        margin-left: 30px;
        margin-top: 30px;
        font-size: large;
    }

    div {
       
        border-radius: 8px;
        background-color: #EDEDED;
        cursor: pointer;
        border: none;
        font-family:'Century751-Roman';
        box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
      
    }

    div:hover {
        filter: brightness(90%);
    }

    div button {
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        background-color: transparent;
        border: none;
        cursor: pointer;
        z-index: 1;
        
    }

    
</style>