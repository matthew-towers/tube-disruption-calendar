# Tube disruption calendar

A Python script that uses the TFL API  to produce an `ics` calendar of planned disruption on specified tube or Overground lines, suitable for importing into Google Calendar or similar.

According to [this Medium post from 2016](https://medium.com/@ed.sparkes/a-tube-planned-works-calendar-91c7a483c3c4) there used to be a similar service available at [tubecal.uk](http://tubecal.uk/) but it is gone now.

Unless you know the lines well, it can be difficult to figure out which stations are affected by a disruption given only the start and end point. For that reason calendar events include a link to the TFL disruption map for their date and time where you can see the affected area on the tube map.

The last six lines in the table below are the new London Overground lines.

I have made these available as shared Google Calendars.  You'll want to set the colour of the calendar to the official TFL colour for the line, so I've provided the hex codes. The calendars go 60 days into the future and are updated daily.

| Line | Google Calendar link | ics file link | Colour |
|------|----------------------|---------------|--------|
|Bakerloo | [link](https://calendar.google.com/calendar/embed?src=gnt5g8brdnc7l9freu5r5vmclgededj1%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/gnt5g8brdnc7l9freu5r5vmclgededj1%40import.calendar.google.com/public/basic.ics) |<span style="background-color:#B36305;color:#FFFFFF">#B36305</span>|
|Central | [link](https://calendar.google.com/calendar/embed?src=o9r9dt6m652nqr692h8s63h26u0l2ed3%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/o9r9dt6m652nqr692h8s63h26u0l2ed3%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#E32017;color:#FFFFFF">#E32017</span>|
|Circle | [link](https://calendar.google.com/calendar/embed?src=eqc1jb37bhmbcvg25q2ku851emh1jb66%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/eqc1jb37bhmbcvg25q2ku851emh1jb66%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#FFD300;color:#000000">#FFD300</span>|
|District | [link](https://calendar.google.com/calendar/embed?src=n6a46kfeabira9l2ahq5366tl8ps5mu1%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/n6a46kfeabira9l2ahq5366tl8ps5mu1%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#00782A;color:#FFFFFF">#00782A</span>|
|Elizabeth | [link](https://calendar.google.com/calendar/embed?src=29gkv9eni198cj8dvek57t48uk7sblvt%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/29gkv9eni198cj8dvek57t48uk7sblvt%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#6950A1;color:#FFFFFF">#6950A1</span>|
|Hammersmith & City | [link](https://calendar.google.com/calendar/embed?src=cdq9mocgqdn6ck4892a6m2k7g16i9o4n%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/cdq9mocgqdn6ck4892a6m2k7g16i9o4n%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#F3A9BB;color:#000000">#F3A9BB</span>|
|Jubilee | [link](https://calendar.google.com/calendar/embed?src=i5mbufo1cjhipv0km1uftebtbojl2oe6%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/i5mbufo1cjhipv0km1uftebtbojl2oe6%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#A0A5A9;color:#FFFFFF">#A0A5A9</span>|
|Metropolitan | [link](https://calendar.google.com/calendar/embed?src=v5gvci2mlcsubqm2iljuk3de3u3b049f%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/v5gvci2mlcsubqm2iljuk3de3u3b049f%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#9B0056;color:#FFFFFF">#9B0056</span>|
|Northern | [link](https://calendar.google.com/calendar/embed?src=eb2sfe0f1j2hl160ec0a79gr8os7t6nf%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/eb2sfe0f1j2hl160ec0a79gr8os7t6nf%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#000000;color:#FFFFFF">#000000</span>|
|Piccadilly | [link](https://calendar.google.com/calendar/embed?src=sgcsqljtasaf8e9qcmr7d0d8isk5mhem%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/sgcsqljtasaf8e9qcmr7d0d8isk5mhem%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#003688;color:#FFFFFF">#003688</span>|
|Victoria | [link](https://calendar.google.com/calendar/embed?src=mp5aaggh5ec57bks9q3bcgv860l9i54i%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/mp5aaggh5ec57bks9q3bcgv860l9i54i%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#0098D4;color:#FFFFFF">#0098D4</span>|
|Waterloo & City | [link](https://calendar.google.com/calendar/embed?src=c2g9vtp4l001ojqc472om3vnini4f91i%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/c2g9vtp4l001ojqc472om3vnini4f91i%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#95CDBA;color:#000000">#95CDBA</span>|
|DLR | [link](https://calendar.google.com/calendar/embed?src=6dqrlv848s6rgitrucnp93k672u4cg89%40import.calendar.google.com&ctz=Europe%2FLondon) | [link](https://calendar.google.com/calendar/ical/6dqrlv848s6rgitrucnp93k672u4cg89%40import.calendar.google.com/public/basic.ics) | <span style="background-color:#00A4A7;color:#FFFFFF">#00A4A7</span>|
|Liberty line | [link]() | [link]() | <span style="background-color:#5F696F;color:#FFFFFF">#5F696F</span>|
|Lioness line | [link]() | [link]() | <span style="background-color:#FDB931;color:#000000">#FDB931</span>|
|Mildmay line | [link]() | [link]() | <span style="background-color:#328CCB;color:#000000">#328CCB</span>|
|Suffragette line | [link]() | [link]() | <span style="background-color:#36B560;color:#000000">#36B560</span>|
|Weaver line | [link]() | [link]() | <span style="background-color:#CB4D8F;color:#000000">#CB4D8F</span>|
|Windrush line | [link]() | [link]() | <span style="background-color:#EE2E2C;color:#000000">#EE2E2C</span>|
