<script>
  import { onMount } from "svelte";
  import ClarityCalendarLine from '~icons/clarity/calendar-line';
  import IonReturnDownBackSharp from '~icons/ion/return-down-back-sharp';
  import { goto } from '$app/navigation';
  import { writable } from 'svelte/store';

  let events = [];
  const upcomingEvents = writable([]);

  async function fetchICal() {
    const url = 'https://corsproxy.io/?' + encodeURIComponent('https://calendar.google.com/calendar/ical/plymgroup28%40gmail.com/private-200aa8ee58a7ff3a5047b75d4392458d/basic.ics');
    const response = await fetch(url);
    const data = await response.text();
    parseICal(data);
  }

  fetchICal();

  function parseICal(data) 
  {
    const lines = data.split('\n');
    let event = {};
    for (let line of lines) 
    {
      if (line.startsWith('BEGIN:VEVENT')){event = {};} 
      else if (line.startsWith('DTSTART')) 
      {
        const datePart = line.substring(8, 16);
        const timePart = line.substring(17, 23);
        const year = datePart.substring(0, 4);
        const month = datePart.substring(4, 6);
        const day = datePart.substring(6, 8);
        const hours = timePart.substring(0, 2);
        const mins = timePart.substring(2, 4);
        event.start = new Date(year, month - 1, day, hours, mins);
      } 
      else if (line.startsWith('DTEND')) 
      {
        const datePart = line.substring(6, 14);
        const timePart = line.substring(15, 21);
        const year = datePart.substring(0, 4);
        const month = datePart.substring(4, 6);
        const day = datePart.substring(6, 8);
        const hours = timePart.substring(0, 2);
        const mins = timePart.substring(2, 4);
        event.end = new Date(year, month - 1, day, hours, mins);
      } 
        else if (line.startsWith('SUMMARY')) {event.summary = line.substring(8);} 
        else if (line.startsWith('LOCATION')) {event.location = line.substring(9);}
        else if (line.startsWith('DESCRIPTION')) {event.description = line.substring(12);}
        else if (line.startsWith('END:VEVENT')) {events.push(event);}
    }
    upcomingEvents.set(getNextEvents());
  }

  function backPressed() {goto('/home');}

  function getNextEvents() 
  {
    const currentTime = new Date();
    const upcomingEvents = [];

    events.forEach(event => {
      const eventStart = event.start;
      if (eventStart > currentTime) 
      {
        upcomingEvents.push(
          {
          ...event,
          start: eventStart
          });
      }
    });

    return upcomingEvents.sort((a, b) => a.start - b.start).slice(0, 5);
  }

  function formatTime(date) {
    const hours = ('0' + date.getHours()).slice(-2);
    const minutes = ('0' + date.getMinutes()).slice(-2);
    return `${hours}:${minutes}`;
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
        {#each $upcomingEvents as event}
          <li>
            <div class="date-box">{event.start.getDate()} <br>
              {(event.start.toLocaleString('default', { month: 'short' })).toUpperCase()}
               
            </div>
            <div class="event-details">
              <strong>{event.summary}</strong><br>
              {formatTime(event.start)} - {formatTime(event.end)}<br>
              {event.location.replace(/\\/g, '')}<br>
            </div>
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
    text-align: left;
    margin-bottom: 25px;
    margin-right: 25px;
  }

  #device-content li {
    list-style: none;
    border: 1px solid #ccc; 
    border-radius: 5px; 
    padding: 10px; 
    margin-bottom: 10px; 
  }

  .date-box {
    display: grid;
    align-items: center;
    width: 60px;
    float: left;
    clear: both;
    min-height: 50px;
    border-right: 10px solid #ccc;
    padding-right: 10px; 
    margin-right: 10px;
    border-radius: 10px;
    margin-top: -10px;
    padding-top: 12px;
    padding-bottom: 11px;
    text-align: center;
  }

  #device-content ul {
    padding-right: 40px;
  }

  #device {
    position: absolute;
    margin-left: 456px;
    width: 1000px;
    height: 550px;
    background-color: #EDEDED;
    border-radius: 8px;
    list-style-type: none;
    font-family: 'Franklin Gothic Light';
  }
</style>
