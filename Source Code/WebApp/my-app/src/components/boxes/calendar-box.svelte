<script>
    import { goto } from '$app/navigation';
    import ClarityCalendarLine from '~icons/clarity/calendar-line';

    function openCalendarPressed() {
        goto("/calendar");
    }
</script>

<div>
    <button on:click={openCalendarPressed}/>
    <ClarityCalendarLine style='position: absolute; margin-top: 20px; margin-left: 25px; width: 30px; height: 30px;'/>
    <p style='margin-left: 80px; margin-top: 25px;'>Calendar</p>
</div>

<style>
    div {
        width: 450px;
        height: 250px;
        border-radius: 10px;
        background-color: #EDEDED;
        cursor: pointer;
        border: none;
        font-family:'Franklin Gothic Light';
    }

    p {
        font-size: large;
        margin-left: 20px;
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