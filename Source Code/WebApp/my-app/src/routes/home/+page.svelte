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
  
  

    #grid {
        display: grid;
        gap: 1rem;
        padding: 1rem;
        grid-template-columns: repeat(auto-fit, minmax(50px, 925px)); 
        grid-template-rows: repeat(auto-fill, minmax(50px, 400px)); 
        
    }

   
</style>