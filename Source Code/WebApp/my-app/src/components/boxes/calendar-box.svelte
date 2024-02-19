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
    <hr style="border: 1px solid black; margin-top: 20px; margin-bottom: 20px;">
    <p id="todayCal">Today: meeting</p>
    <hr style="border: 1px solid black; margin-top: 20px; margin-bottom: 20px;">
    <p id="tomorrowCal">Saturday: shopping</p>
    <hr style="border: 1px solid black; margin-top: 20px; margin-bottom: 20px;">
    <p id="dayAfterCal">Sunday:</p>
    <hr style="border: 1px solid black; margin-top: 20px; margin-bottom: 00px;">
</div>

<style>
    #todayCal {
        margin-left: 20px;
        font-size: medium;       
    }
    #tomorrowCal {
        margin-left: 20px;
        font-size: medium;       
    }
    #dayAfterCal {
        margin-left: 20px;
        font-size: medium;       
    }

    div {
        width: 450px;
        height: 250px; 
        border-radius: 10px;
        background-color: #EDEDED;
        cursor: pointer;
        border: none;
        font-family:'Franklin Gothic Light';
        position: relative; 
    }

    p {
        font-size: large;
    }

    div button {
        position: absolute;
        width: 430px;
        height: 225px; 
        border-radius: 10px;
        background-color: transparent;
        cursor: pointer;
        border: none;    
    }
</style>
