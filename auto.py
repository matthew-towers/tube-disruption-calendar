#!/usr/bin/python
import datetime as dt
import disruption_calendar
import git
import logging
import os
import sys
import pathlib

file_log = logging.FileHandler(filename="tdc.log")
print_log = logging.StreamHandler(stream=sys.stdout)
handlers = [file_log, print_log]
logging.basicConfig(
        level=logging.INFO,
        handlers=handlers,
        format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s'
        )
logger = logging.getLogger(__name__)

# Set up a Repo object for the repository storing the tube disruption calendar.
# Pull the latest files. If the latest commit was more than 12 hours ago, or if
# the command line option "force" was used, update the calendars, add and commit
# the new calendar files, then push to the remote repo.
#
# gitpython docs: https://gitpython.readthedocs.io/en/stable/index.html

this_dir = pathlib.Path(__file__).parent.resolve()
os.chdir(this_dir)

try:
    repo = git.Repo(this_dir)
    o = repo.remotes.origin
except:
    os.system("notify-send -a 'Tube disruption calendar' 'Error setting up repo'")
    logger.exception("Error setting up repo.")
    sys.exit(1)

logger.info("pulling")

try:
    o.pull()
except:
    os.system("notify-send -a 'Tube disruption calendar' 'Error pulling'")
    logger.exception("Error pulling.")
    repo.close()
    sys.exit(1)

latest_commit_date = repo.head.commit.authored_datetime
local_tz = dt.datetime.now(dt.timezone.utc).astimezone().tzinfo
current_date = dt.datetime.now(local_tz)
time_since_last_commit = current_date - latest_commit_date

args = sys.argv
force = len(args) == 2 and args[1] == "force"

if force or time_since_last_commit > dt.timedelta(hours=12):
    logger.info(f"Last commit was this long ago: {time_since_last_commit}.")
    disruption_calendar.make_all_calendars()
else:
    os.system("notify-send -a 'Tube disruption calendar' 'Not updating, too recent'")
    logger.info("Not updating - latest commit was too recent.")
    repo.close()
    sys.exit(1)

repo.git.add(all=True)
repo.index.commit("update calendars")

logger.info("pushing...")

try:
    o.push()
except:
    os.system("notify-send -a 'Tube disruption calendar' 'Error pushing'")
    logger.exception("Error pushing.")
    repo.close()
    sys.exit(1)

os.system("notify-send -a 'Tube disruption calendar' 'calendars updated'")
logger.info("Push successful.")
repo.close()
