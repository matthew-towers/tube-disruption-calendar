import git
import disruption_calendar
import os
# Set up a Repo object for the repository storing the tube disruption calendar. Pull the latest files. Update the calendars, add and commit the new calendar files, then push to the remote repo.
# gitpython docs: https://gitpython.readthedocs.io/en/stable/index.html

cwd = os.getcwd()
repo = git.Repo(cwd)
o = repo.remotes.origin

print("pulling...")
o.pull()

disruption_calendar.make_all_calendars()

repo.git.add(all=True)
repo.index.commit("update calendars")

print("pushing...")
o.push()
