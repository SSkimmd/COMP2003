<script>
    import { goto } from '$app/navigation';
    import FluentWeatherFog48Filled from '~icons/fluent/weather-fog-48-filled';
    import { GetLocation, UpdateLocation, GetWeather, GetMoon, GetHumidity, GetTemp, GetSunRise, GetSunSet, GetUV, GetWind, GetKind2, GetKind1,GetKind3,GetKind4 } from "$lib/weather"


    function openWeatherPressed() {
        goto("/weather");
    }
</script>

<div>
    <button on:click={openWeatherPressed}/>
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
        width: 450px;
        height: 250px;
        border-radius: 10px;
        background-color: #EDEDED;
        cursor: pointer;
        border: none;
        font-family:'Franklin Gothic Light';
    }

    div button {
        position: absolute;
        width: 400px;
        height: 225px;
        border-radius: 10px;
        background-color: transparent;
        cursor: pointer;
        border: none;    
    }
</style>