export async function FetchICal() {
    const url = 'https://corsproxy.io/?' + encodeURIComponent('https://calendar.google.com/calendar/ical/plymgroup28%40gmail.com/private-200aa8ee58a7ff3a5047b75d4392458d/basic.ics');
    const response = await fetch(url);
    const data = await response.text();

    return data;
}

/**
* @param {string} data
**/
export async function GetEvents(data) 
{
  const lines = data.split('\n');
  let event = {};
  let events = []
  for (let line of lines) 
  {
    // @ts-ignore
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
      // @ts-ignore
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
      // @ts-ignore
      event.end = new Date(year, month - 1, day, hours, mins);
    } 
      else if (line.startsWith('SUMMARY')) {event.summary = line.substring(8);} 
      else if (line.startsWith('LOCATION')) {event.location = line.substring(9);}
      if (event.location == null){event.location = ' Location Not Specified'}
      else if (line.startsWith('DESCRIPTION')) {event.description = line.substring(12);}
      else if (line.startsWith('END:VEVENT')) {events.push(event);}
  }

  // @ts-ignore
  return events;
}