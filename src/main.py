#!/usr/bin/env python3

"""Module from which the program is executed."""

import sys   # exit()
import time  # time()

import scheduler
import user


# -------------------------------------------------------------------

dummy_file = ".instance.txt"
room_file = ".rooms.txt"
epoch_time = time.time()

try:
    # Update instance file with current time
    with open(dummy_file, 'w') as f:
        f.write(str(epoch_time))

    # Erase old rooms file
    with open(room_file, 'w') as f:
        pass

    # Collects initial data from the user
    user = user.User()

    # Run schedule
    scheduler = scheduler.Scheduler(user.data, dummy_file, epoch_time)

except KeyboardInterrupt:
    print()
    sys.exit(-1)
