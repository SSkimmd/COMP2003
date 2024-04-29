<script>
    import RiDeviceFill from '~icons/ri/device-fill';
    import MaterialSymbolsCircle from '~icons/material-symbols/circle';
    import { goto } from '$app/navigation';

    function openDevicePressed() {
        goto("/device");
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

<div style='border-radius: 8px; background-color: #EDEDED; cursor: pointer; position: relative;'>
    <button on:click={openDevicePressed} on:click|preventDefault={stopPropagation} />
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
        cursor: pointer;
        border: none;
        font-family:'Franklin Gothic Light';
        position: relative;
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
