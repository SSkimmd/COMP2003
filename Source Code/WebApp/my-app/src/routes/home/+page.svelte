<script>
    import Navigation from "../../components/navigation.svelte";
    import WeatherBox from "../../components/boxes/weather-box.svelte";
    import DeviceBox from "../../components/boxes/device-box.svelte";
    import CalendarBox from "../../components/boxes/calendar-box.svelte";
    import CustomiseBox from "../../components/boxes/customise-box.svelte";
</script>


<Navigation/>
<div id="grid">
    <WeatherBox/>
    <DeviceBox/>
    <CalendarBox/>
    <CustomiseBox/>
</div>


<style>
    #grid {
        margin-left: 30%;
        margin-top: 15vh;

        display: grid;
        grid-template-columns: 450px 250px;
        grid-template-rows: auto;
        column-gap: 100px;
        row-gap: 50px;
    }
</style>