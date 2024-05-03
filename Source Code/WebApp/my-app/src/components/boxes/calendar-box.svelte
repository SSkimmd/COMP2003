<script>
    // @ts-ignore
    import { goto } from '$app/navigation';
    import ClarityCalendarLine from '~icons/clarity/calendar-line';
    import { writable } from 'svelte/store';
    import { onMount } from 'svelte';
    import { GetEvents } from '$lib/calendar';
 
    /**
     * @type {{ start: Date; end: Date; summary: any; location: any; description: any; }[]}
     */
    let events = [];
    // @ts-ignore
    const upcomingEvents = writable([]);

    async function fetchICal() {
        const url = 'https://corsproxy.io/?' + encodeURIComponent('https://calendar.google.com/calendar/ical/plymgroup28%40gmail.com/private-200aa8ee58a7ff3a5047b75d4392458d/basic.ics');
        const response = await fetch(url);
        const data = await response.text();
        parseICal(data);
    }

    fetchICal();

    /**
     * @param {string} data
     */
    function parseICal(data) {
        const lines = data.split('\n');
        let event = {};
        for (let line of lines) {
            // @ts-ignore
            if (line.startsWith('BEGIN:VEVENT')) { event = {}; }
            else if (line.startsWith('DTSTART')) {
                const datePart = line.substring(8, 16);
                const timePart = line.substring(17, 23);
                const year = datePart.substring(0, 4);
                const month = datePart.substring(4, 6);
                const day = datePart.substring(6, 8);
                const hours = timePart.substring(0, 2);
                const mins = timePart.substring(2, 4);
                // @ts-ignore
                event.start = new Date(year, month - 1, day, hours, mins);
            }
            else if (line.startsWith('DTEND')) {
                const datePart = line.substring(6, 14);
                const timePart = line.substring(15, 21);
                const year = datePart.substring(0, 4);
                const month = datePart.substring(4, 6);
                const day = datePart.substring(6, 8);
                const hours = timePart.substring(0, 2);
                const mins = timePart.substring(2, 4);
                // @ts-ignore
                event.end = new Date(year, month - 1, day, hours, mins);
            }
            else if (line.startsWith('SUMMARY')) { event.summary = line.substring(8); }
            else if (line.startsWith('DESCRIPTION')) { event.description = line.substring(12); }
            // @ts-ignore
            else if (line.startsWith('END:VEVENT')) { events.push(event); }
        }
        console.log(events)
        // @ts-ignore
        upcomingEvents.set(getNextEvents());
    }

    function getNextEvents() {
        const currentTime = new Date();

        /**
         * @type {{ start: Date; end: Date; summary: any; location: any; description: any; }[]}
         */
        // @ts-ignore
        // @ts-ignore
        const upcomingEvents = [];

        events.forEach(event => {
            const eventStart = event.start;
            if (eventStart > currentTime) {
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

    /**
     * @param {{ getHours: () => string; getMinutes: () => string; }} date
     */
    function formatTime(date) {
        const hours = ('0' + date.getHours()).slice(-2);
        const minutes = ('0' + date.getMinutes()).slice(-2);
        return `${hours}:${minutes}`;
    }
    function openCalendarPressed() {
        goto("/calendar");
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
<div style='border-radius: 8px; background-color: #EDEDED; cursor: pointer; position: relative; box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px; transition: filter 0.7s ease;'>
    <button on:click={openCalendarPressed} on:click|preventDefault={stopPropagation} />
    <ClarityCalendarLine style='position: absolute; margin-top: 15px; margin-left: 20px; width: 24px; height: 24px; '/>
    <p style='margin-left: 60px; margin-top: 15px; font-family: "Century751-Roman"; font-size: 18px; font-size: 24px;'><b>Calendar</b></p>    
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
        font-family:'Century751-Roman'
        
    }

    #device-content ul {
        padding-left: 15px;
        margin: 0;
        

    }

    #device-content li {
        list-style: none;
        padding: 4px; 
        
        
        
    }

    div:hover {
        filter: brightness(90%);
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
