<script>
    import { goto } from '$app/navigation';
    import FluentWeatherFog48Filled from '~icons/fluent/weather-fog-48-filled';

    function openWeatherPressed() {
        goto("/weather");
    }
</script>

<div>
    <button on:click={openWeatherPressed}/>
    <FluentWeatherFog48Filled style='position: absolute; margin-top: 20px; margin-left: 25px; width: 30px; height: 30px;'/>
    <p style='margin-left: 80px; margin-top: 25px;'>Weather</p>
    <p id="location">Plymouth</p>
    <p id="temperature">10°c</p>
    <p id="weather">Windy</p>
</div>

<style>
    #weather {
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