#!/usr/bin/python
import git
import disruption_calendar
import os
import sys
import pathlib
# Set up a Repo object for the repository storing the tube disruption calendar. Pull the latest files. Update the calendars, add and commit the new calendar files, then push to the remote repo.
# gitpython docs: https://gitpython.readthedocs.io/en/stable/index.html
print(__file__)

try:
    # cwd = os.getcwd()
    this_file = __file__
    this_dir = pathlib.Path(__file__).parent.resolve()
    repo = git.Repo(this_dir)
    o = repo.remotes.origin
except:
    os.system("notify-send 'Error setting up repo'")
    sys.exit(0)

print("pulling...")
try:
    o.pull()
except:
    os.system("notify-send 'Error pulling'")
    sys.exit(0)

disruption_calendar.make_all_calendars()

repo.git.add(all=True)
repo.index.commit("update calendars")

print("pushing...")

try:
    o.push()
    os.system("notify-send 'calendars updated'")
except:
    os.system("notify-send 'Error pushing'")
