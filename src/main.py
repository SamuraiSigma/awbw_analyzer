#!/usr/bin/env python3

"""Module from which the program is executed."""

import sys   # exit()
import time  # time()

import scheduler
import user


# -------------------------------------------------------------------

dummy_file = ".instance.txt"
epoch_time = time.time()

try:
    # Erases old instance file
    with open(dummy_file, 'w') as f:
        f.write(str(epoch_time))

    # Collects initial data from the user
    user = user.User()

    # Run schedule
    scheduler = scheduler.Scheduler(user.data, dummy_file, epoch_time)

except KeyboardInterrupt:
    print()
    sys.exit(-1)
