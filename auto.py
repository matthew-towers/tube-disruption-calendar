#!/usr/bin/python
import git
import disruption_calendar
import os
import sys
import pathlib
import datetime as dt
# Set up a Repo object for the repository storing the tube disruption calendar.
# Pull the latest files. If the latest commit was more than 12 hours ago,
# update the calendars, add and commit the new calendar files, then push to the
# remote repo.
#
# gitpython docs: https://gitpython.readthedocs.io/en/stable/index.html

args = sys.argv
this_dir = pathlib.Path(__file__).parent.resolve()
os.chdir(this_dir)

try:
    repo = git.Repo(this_dir)
    o = repo.remotes.origin
except:
    os.system("notify-send -a 'Tube disruption calendar' 'Error setting up repo'")
    sys.exit(0)

print("pulling...")
try:
    o.pull()
except:
    os.system("notify-send -a 'Tube disruption calendar' 'Error pulling'")
    repo.close()
    sys.exit(0)

latest_commit_date = repo.head.commit.authored_datetime
local_tz = dt.datetime.now(dt.timezone.utc).astimezone().tzinfo
current_date = dt.datetime.now(local_tz)

force = len(args) == 2 and args[1] == "force"
if force or current_date - latest_commit_date > dt.timedelta(hours=12):
    disruption_calendar.make_all_calendars()
else:
    os.system("notify-send -a 'Tube disruption calendar' 'Not updating, too recent'")
    repo.close()
    sys.exit(0)

repo.git.add(all=True)
repo.index.commit("update calendars")

print("pushing...")

try:
    o.push()
    os.system("notify-send -a 'Tube disruption calendar' 'calendars updated'")
except:
    os.system("notify-send -a 'Tube disruption calendar' 'Error pushing'")

repo.close()
