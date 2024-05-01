<script>
    import { json } from "@sveltejs/kit";
    import { onMount } from "svelte";
    import Navigation from "../../components/navigation.svelte";
    import AkarIconsEdit from '~icons/akar-icons/edit';
    import IonReturnDownBackSharp from '~icons/ion/return-down-back-sharp';
    import { goto } from '$app/navigation';
  
    function backPressed() {
      goto('/home')
    }
  </script>

<div>
  <Navigation/>
</div>

<div id="device">
  <button on:click={backPressed}>
    <IonReturnDownBackSharp style='width: 30px; height: 30px;'/>
  </button>
  
  <AkarIconsEdit style='position: absolute; margin-top: 20px; margin-left: 70px; width: 30px; height: 30px;'/>
  
  <p style='margin-left: 120px; margin-top: 20px; font-size: 24px;'><b>Customisation Settings</b></p>

  <div id="device-content">
  </div>
</div>

<style>
  #device {
      position: absolute;
      margin-top: 35px;
      margin-bottom: 35px;
      min-width: 50px;
      width: 99%;
      height: 80%;
      background-color: #EDEDED;
      border-radius: 8px;
      box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
      font-family: 'Century751-Roman';
  }

  button {
        position: absolute;
        width: 40px;
        height: 40px;
        top: 20px;
        left: 20px;
        background-color: transparent;
        border: none;
        cursor: pointer;
        overflow: hidden;
        border-radius: 50%;
        transition: border-color 0.3s ease;
        border: 2px solid transparent;
        padding: 0; 
        margin: 0; 
    }

    button:hover {
        border-color: #000;
    }
</style>