<script>
    import RiDeviceFill from '~icons/ri/device-fill';
    import MaterialSymbolsCircle from '~icons/material-symbols/circle';
    import { goto } from '$app/navigation';

    function openDevicePressed() {
        goto("/device");
    }
</script>

<div>
    <button on:click={openDevicePressed}/>
    <RiDeviceFill style='position: absolute; margin-top: 20px; margin-left: 25px; width: 30px; height: 30px;'/>
    <p style='margin-left: 80px; margin-top: 25px;'>Device</p>
    <MaterialSymbolsCircle style='position: absolute; margin-left: 30px; margin-top: 20px; color: green;'/>
    <p id="device-connected">Device Connected</p>
</div>

<style>
    #device-connected {
        margin-top: 36px;
        margin-left: 70px;
    }

    div {
        
        border-radius: 8px;
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