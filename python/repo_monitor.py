#!/usr/bin/python

import subprocess, sys
import time
from datetime import datetime

path_to_repo = "" # ADD HERE TARGET REPO FULL PATH (WITHOUT THE END .git) LIKE: "/home/user/repos/foo"
if path_to_repo == "":
  prompt = "Enter full path to target repo (without .git suffix), ie: /home/user/repos/foo:\n"
  path_to_repo = output(prompt)

command_pull = f"cd {path_to_repo} && git pull"

print(f"Listening to repository {path_to_repo}.git, changes will be notified.")

while True:
    output = subprocess.getoutput(command_pull)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if output == 'Already up to date.':
        print(f"[{now}]: {output}")
    elif "error" in output or "denied" in output:
        msg = f"[{now}]: ERROR pulling {path_to_repo}.git repository:\n\n{output}"
        print(msg)
        command_notify = f"notify-send '{msg}'"
        subprocess.run(command_notify, shell = True, executable="/bin/bash")
    else:
        print(f"[{now}]: NEW COMMITS RECIEVED:\n{output}")

        command_notify = f"notify-send '[{now}]: Recieved changes to {path_to_repo}.git repository:\n\n{output}'"
        subprocess.run(command_notify, shell = True, executable="/bin/bash")

    start = 60 # CUSTOMISE THE REFRESH RATE

    while start > 0:
        msg = "Waiting for {} seconds before running next 'git pull' ...".format(start)
        print(msg, '\r', end="")
        time.sleep(1)
        remove_msg = ' ' * len(msg)
        print( remove_msg, '\r', end="")
        # decrement timer by one second
        start -= 1
