import requests
import datetime as dt
import ics
import sys

lineid_to_name = {
    "bakerloo": "Bakerloo",
    "central": "Central",
    "circle": "Circle",
    "district": "District",
    "elizabeth": "Elizabeth line",
    "hammersmith-city": "Hammersmith & City",
    "jubilee": "Jubilee",
    "metropolitan": "Metropolitan",
    "northern": "Northern",
    "piccadilly": "Piccadilly",
    "victoria": "Victoria",
    "waterloo-city": "Waterloo & City",
    "dlr": "DLR",
    "liberty": "Liberty line",
    "lioness": "Lioness line",
    "mildmay": "Mildmay line",
    "suffragette": "Suffragette line",
    "weaver": "Weaver line",
    "windrush": "Windrush line",
}

lineid_to_colour = {
    "bakerloo": "#B36305",
    "central": "#E32017",
    "circle": "#FFD300",
    "district": "#00782A",
    "elizabeth": "#6950A1",
    "hammersmith-city": "#F3A9BB",
    "jubilee": "#A0A5A9",
    "metropolitan": "#9B0056",
    "northern": "#000000",
    "piccadilly": "#003688",
    "victoria": "#0098D4",
    "waterloo-city": "#95CDBA",
    "dlr": "#00A4A7",
    "liberty": "#5F696F",
    "lioness": "#FDB931",
    "mildmay": "#328CCB",
    "suffragette": "#36B560",
    "weaver": "#CB4D8F",
    "windrush": "#EE2E2C",
}


all_lineids = list(lineid_to_name.keys())


def make_event(name, description, start, end, alarms=None):
    # Create a link to the TFL disruption map page for the time of this event, prepend it to the disruption description
    url_start_time = start.replace(tzinfo=None).isoformat()
    url_end_time = end.replace(tzinfo=None).isoformat()
    map_url = f"https://tfl.gov.uk/tube-dlr-overground/status/?Input=&lineIds=&dateTypeSelect=Future%20date&direction=&startDate={url_start_time}&endDate={url_end_time}"
    link = f'<a href="{map_url}">Disruption map.</a>\n\n'
    e = ics.Event(description=link + description, alarms=alarms)
    e.name = name
    e.begin = start
    e.end = end
    return e


def fetch_disruptions(lineid, n_days=60):
    """Use the TFL API to get planned disruptions for the next n_days days on
    the line with id lineid"""

    calendar_start = dt.date.today()
    calendar_length = dt.timedelta(days=n_days)
    calendar_end = calendar_start + calendar_length

    status_url = f"https://api.tfl.gov.uk/Line/{lineid}/Status/{calendar_start.isoformat()}/to/{calendar_end.isoformat()}"

    try:
        resp = requests.get(url=status_url)
        status_data = resp.json()
    except Exception as e:
        print(f"Failed to fetch and parse disruption data for {lineid}:", e)
        sys.exit(1)

    return status_data


def make_calendar(lineid, disruption_data):
    """Build an ics.Calendar for the line with id lineid using the
    data from disruption_data"""

    calendar = ics.Calendar()

    for status in disruption_data:
        for disruption in status["lineStatuses"]:
            event_name = (
                f'{lineid_to_name[lineid]}: {disruption["statusSeverityDescription"]}'
            )

            def from_date(i):
                return dt.datetime.fromisoformat(
                    disruption["validityPeriods"][i]["fromDate"]
                )

            def to_date(i):
                return dt.datetime.fromisoformat(
                    disruption["validityPeriods"][i]["toDate"]
                )

            # A disruption may have many validity periods each of which should
            # give rise to a calendar event, except that some continuous validity
            # periods are split when they go over a date boundary.
            # These should be joined.
            one_minute = dt.timedelta(minutes=1)
            n = len(disruption["validityPeriods"])
            i = 0
            while i < n:
                start = from_date(i)
                while (
                    (i < n - 1)
                    and (to_date(i).hour == 23)
                    and (to_date(i).minute == 59)
                    and (to_date(i) + one_minute == from_date(i + 1))
                ):
                    i += 1
                end = to_date(i)
                calendar.events.add(
                    make_event(event_name, disruption["reason"], start, end)
                )
                i += 1
    return calendar


def write_ics(lineid, calendar):
    """Write the data in calendar to an ics file, setting a calendar name using
    lineid"""
    filename = f"{lineid}_disruptions.ics"
    # Hack: insert
    # X-WR-CALNAME:<calendar name>
    # at index 3 to set a calendar name.  You can do this in ics if you have
    # the latest version but not with 0.7.2.
    cal_lines = calendar.serialize().splitlines()
    cal_lines.insert(3, f"X-WR-CALNAME:{lineid_to_name[lineid]} disruption")
    with open(filename, "w") as f:
        f.writelines(map(lambda x: x + "\n", cal_lines))


def make_all_calendars():
    for i, lineid in enumerate(all_lineids):
        print(f"making calendar for {lineid} ({i+1}/{len(all_lineids)})...")
        write_ics(lineid, make_calendar(lineid, fetch_disruptions(lineid)))


if __name__ == "__main__":
    make_all_calendars()
