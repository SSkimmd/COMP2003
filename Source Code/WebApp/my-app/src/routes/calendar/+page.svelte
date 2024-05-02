<script>
  // @ts-ignore
  import { onMount } from "svelte";
  import ClarityCalendarLine from '~icons/clarity/calendar-line';
  import IonReturnDownBackSharp from '~icons/ion/return-down-back-sharp';
  import { goto } from '$app/navigation';
  import Navigation from "../../components/navigation.svelte";
  import { writable } from 'svelte/store';
  import { GetEvents, FetchICal } from '$lib/calendar'
  import { formatTime } from '$lib/util'

  function backPressed() {goto('/home');}

  /**
     * @param {any[]} events 
     */
  async function getNextEvents(events) 
  {
    const currentTime = new Date();
    
    /**
       * @type {{ start: Date; end: Date; summary: any; location: any; description: any; }[]}
       */
    // @ts-ignore
    // @ts-ignore
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

    // @ts-ignore
    return upcomingEvents.sort((a, b) => a.start - b.start).slice(0, 5);
  }


  // @ts-ignore
  const upcomingEvents = writable([]);

  onMount(() => {
      // @ts-ignore
      FetchICal().then((data) => {
        GetEvents(data).then((events) => {
          // @ts-ignore
          getNextEvents(events).then(upcoming => upcomingEvents.set(upcoming))
        })
      })
  })
</script>

<div>
  <Navigation/>
</div>

<div>
  <div id="device">
    <button on:click={backPressed}>
      <IonReturnDownBackSharp style='width: 30px; height: 30px;'/>
    </button>
    
    <ClarityCalendarLine style='position: absolute; margin-top: 20px; margin-left: 70px; width: 30px; height: 30px;'/>
    <p style='margin-left: 120px; margin-top: 20px; font-size: 24px;'><b>Calendar</b></p>

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
      margin-top: 35px;
      margin-bottom: 35px;
      min-width: 50px;
      width: 99%;
      height: 80%;
      background-color: #EDEDED;
      border-radius: 8px;
      box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;

    list-style-type: none;
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
