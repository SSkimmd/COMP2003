<script>
    // @ts-ignore
    import { goto } from '$app/navigation';
    import ClarityCalendarLine from '~icons/clarity/calendar-line';
    import { writable } from 'svelte/store';
    import { GetEvents, FetchICal } from '$lib/calendar';
    import { formatTime } from '$lib/util'
    import { onMount } from "svelte";

    // @ts-ignore
    const upcomingEvents = writable([]);

    function openCalendarPressed() {
        goto("/calendar");
    }

    /**
    * @param {any[]} events 
    */
    async function getNextEvents(events) {
        const currentTime = new Date();
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
        return upcomingEvents.sort((a, b) => a.start - b.start).slice(0, 3);
    }


    onMount(() => {
      // @ts-ignore
      FetchICal().then((data) => {
        GetEvents(data).then((events) => {
          // @ts-ignore
          getNextEvents(events).then(upcoming => upcomingEvents.set(upcoming))
        })
      })
  })

  /**
     * Function to prevent the button click event from bubbling up to the parent div
     * and triggering its click event.
     * @param {Event} event The click event
     */
     function stopPropagation(event) {
        event.stopPropagation();
    }
  
</script>

<!-- svelte-ignore a11y-click-events-have-key-events -->
<!-- svelte-ignore a11y-no-static-element-interactions -->
<div style='border-radius: 8px; background-color: #EDEDED; cursor: pointer; position: relative;'>
    <button on:click={openCalendarPressed} on:click|preventDefault={stopPropagation} />
    <ClarityCalendarLine style='position: absolute; margin-top: 15px; margin-left: 20px; width: 24px; height: 24px;'/>
    <p style='margin-left: 60px; margin-top: 18px; font-family: "Franklin Gothic Light"; font-size: 18px;'>Calendar</p>
    
    <div id="device-content">
        <ul>
            {#each $upcomingEvents as event}
            <li style="font-size: 14px; border: 1px solid #ccc; border-radius: 4px; padding: 4px; margin-bottom: 8px;">
                <div class="date-box">{event.start.getDate()}<br>{(event.start.toLocaleString('default', { month: 'short' })).toUpperCase()}</div>
                <div class="event-details">
                    <strong style="font-size: 16px;">{event.summary}</strong><br>
                    {formatTime(event.start)} - {formatTime(event.end)}<br>
                </div>
            </li>
            {/each}
        </ul>
    </div>
    
</div> 

<style>
    #device-content {
        margin-top: 18px;
        text-align: left;
        margin-bottom: 18px;
        margin-right: 18px;
        overflow-y: auto;
        font-family:'Franklin Gothic Light'
    }

    #device-content ul {
        padding-left: 15px;
        margin: 0;
    }

    #device-content li {
        list-style: none;
        padding: 4px; 
    }

    .date-box {
        display: grid;
        align-items: center;
        width: 30px; 
        float: left;
        clear: both;
        min-height: 30px; 
        border-right: 6px solid #ccc; 
        padding-right: 6px; 
        margin-right: 6px; 
        border-radius: 6px; 
        margin-top: -6px; 
        padding-top: 6px;
        padding-bottom: 6px;
        text-align: center;
        font-size: 14px;
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
