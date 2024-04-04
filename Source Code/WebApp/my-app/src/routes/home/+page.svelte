<script>
    import FaUserCircle from '~icons/fa/user-circle';
    import Navigation from "../../components/navigation.svelte";
    import WeatherBox from "../../components/boxes/weather-box.svelte";
    import DeviceBox from "../../components/boxes/device-box.svelte";
    import CalendarBox from "../../components/boxes/calendar-box.svelte";
    import CustomiseBox from "../../components/boxes/customise-box.svelte";
</script>

<div id="app">
    <Navigation/>

    <div id="content">
        <div id="grid">
            <WeatherBox/>
            <DeviceBox/>
            <CalendarBox/>
            <CustomiseBox/>
        </div>
    </div>
</div>

<style>
    #app {
        display: flex;
        flex-direction: row;
    }

    #content {
        margin-left: 400px; /* Adjust this as needed */
        margin-right: 35px;
        margin-bottom: 15vh;
    }

    #grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(250px, 800px)); /* Set 2 columns with flexible width */
        grid-template-rows: auto;
        column-gap: 25px;
        row-gap: 25px;
        margin-top: 35px;
        margin-bottom: 35px;
    }

    /* Control overflow for grid items */
    #grid > * {
        max-height: 400px; /* Set maximum height for each box */
        overflow: auto; /* Add scrollbar if content exceeds the maximum height */
    }
</style>