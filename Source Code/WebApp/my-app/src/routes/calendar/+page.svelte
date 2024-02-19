<script>
  import Navigation from "../../components/navigation.svelte";
  import ClarityCalendarLine from '~icons/clarity/calendar-line';
  import IonReturnDownBackSharp from '~icons/ion/return-down-back-sharp';
  import { goto } from '$app/navigation';

  function backPressed() {
    goto('/home');
  }
</script>

<div style='margin-top: 15vh;'>
  <Navigation/>
</div>

<div id="device">
  <button on:click={backPressed} style='position:absolute; width: 40px; 
  height: 40px; margin-top: 20px; margin-left: 20px; 
  background-color: transparent; border: none; cursor: pointer;'>
    <IonReturnDownBackSharp style='width: 30px; height: 30px;'/>
  </button>
  
  <ClarityCalendarLine style='position: absolute; margin-top: 20px; margin-left: 70px; width: 30px; height: 30px;'/>
  <p style='margin-left: 120px; margin-top: 25px;'>Calendar</p>

  <div id="device-content">
    <iframe src="https://calendar.google.com/calendar/embed?src=plymgroup28%40gmail.com&ctz=Europe%2FLondon&key=AIzaSyDdCZh-NSkq5Vxamy3vez7nCUcEyY9-Ii0" style="border:solid 1px #777; width: 800px; height: 600px;" frameborder="0" scrolling="no"></iframe>
  </div>
</div>

<style>
  #device-content {
    margin-left: 25px;
    margin-top: 25px;
    text-align: center;
  }

  #device {
    position: absolute;
    margin-left: 456px;
    width: 1000px;
    height: 550px;
    background-color: #EDEDED;
    border-radius: 8px;
    font-family: 'Franklin Gothic Light';
  }
</style>
