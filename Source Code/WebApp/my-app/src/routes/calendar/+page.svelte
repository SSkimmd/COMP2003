<script>
  import { onMount } from "svelte";
  import ClarityCalendarLine from '~icons/clarity/calendar-line';
  import IonReturnDownBackSharp from '~icons/ion/return-down-back-sharp';
  import { goto } from '$app/navigation';
  import ical from 'node-ical'

  let events = [];

 
  async function fetchICal() {
    const url = 'https://corsproxy.io/?' + 'https://calendar.google.com/calendar/ical/plymgroup28%40gmail.com/private-200aa8ee58a7ff3a5047b75d4392458d/basic.ics';
    const response = await fetch(url);
    const data = await response.text();
    //console.log(data);
    parseICal(data);
}
fetchICal();

  function parseICal(data) {
    const lines = data.split('\n');
    let event = {};
    for (let line of lines) {
      if (line.startsWith('BEGIN:VEVENT')) {
        event = {};
      } else if (line.startsWith('DTSTART')) {
        event.start = line.substring(8);
      } else if (line.startsWith('DTEND')) {
        event.end = line.substring(6);
      } else if (line.startsWith('SUMMARY')) {
        event.summary = line.substring(8);
      } else if (line.startsWith('LOCATION')) {
        event.location = line.substring(9);
      } else if (line.startsWith('DESCRIPTION')) {
        event.description = line.substring(12);
      } else if (line.startsWith('END:VEVENT')) {
        events.push(event);
      }
      //console.log(event);
    }
    //console.log(events);
    events = events;
  }

  function backPressed() {
    goto('/home')
  }
</script>

<div style='margin-top: 15vh;'>
  <div id="device">
    <button on:click={backPressed} style='position:absolute; width: 40px; 
    height: 40px; margin-top: 20px; margin-left: 20px; 
    background-color: transparent; border: none; cursor: pointer;'>
      <IonReturnDownBackSharp style='width: 30px; height: 30px;'/>
    </button>
    
    <ClarityCalendarLine style='position: absolute; margin-top: 20px; margin-left: 70px; width: 30px; height: 30px;'/>
    <p style='margin-left: 120px; margin-top: 25px;'>Calendar</p>

    <div id="device-content">
      <ul>
        {#each events as event}
          <li>
            <strong>{event.summary}</strong><br>
            {event.location}<br>
            Start: {event.start}<br>
            End: {event.end}<br>
            Description: {event.description}
          </li>
        {/each}
      </ul>
    </div>
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