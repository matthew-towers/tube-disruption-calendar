import requests
import datetime as dt
import ics
import sys

lineid_to_name = {
    "bakerloo": "Bakerloo",
    "central": "Central",
    "circle": "Circle",
    "district": "District",
    "dlr": "DLR",
    "elizabeth": "Elizabeth line",
    "hammersmith-city": "Hammersmith & City",
    "jubilee": "Jubilee",
    "london-overground": "London Overground",
    "metropolitan": "Metropolitan",
    "northern": "Northern",
    "piccadilly": "Piccadilly",
    "victoria": "Victoria",
    "waterloo-city": "Waterloo & City",
}

all_lineids = list(lineid_to_name.keys())


def make_event(name, description, start, end, alarms=None):
    e = ics.Event(description=description, alarms=alarms)
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

    url_base = "https://api.tfl.gov.uk/Line/"
    status_url = f"{url_base}{lineid}/Status/{calendar_start.isoformat()}/to/{calendar_end.isoformat()}"

    try:
        resp = requests.get(url=status_url)
        status_data = resp.json()
    except Exception as e:
        print("Failed to fetch and parse disruption data:", e)
        sys.exit(1)
    return status_data


def make_calendar(lineid, disruption_data):
    """Build an ics.Calendar for the line with id lineid using the
    data from disruption_data"""

    calendar = ics.Calendar()

    for status in disruption_data:
        for disruption in status["lineStatuses"]:
            # event_name = (lineid_to_name[disruption["lineId"]] + ": " + disruption["statusSeverityDescription"])
            # No need for this if we do only one line per calendar
            event_name = (
                lineid_to_name[lineid] + ": " + disruption["statusSeverityDescription"]
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
            # give rise to a calendar event, except that continuous validity
            # periods are split when they go over a date boundary.
            # These should be joined.
            one_minute = dt.timedelta(minutes=1)
            n = len(disruption["validityPeriods"])
            i = 0
            while i < n:
                start = from_date(i)
                while (i < n - 1) and (to_date(i) + one_minute == from_date(i + 1)):
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


for lineid in all_lineids:
    write_ics(lineid, make_calendar(lineid, fetch_disruptions(lineid)))
