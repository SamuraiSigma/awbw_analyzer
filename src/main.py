#!/usr/bin/env python3

"""Module from which the program is executed."""

import sys

import scheduler
import user


# -------------------------------------------------------------------

try:
    # Collects initial data from the user
    user = user.User()

    # Run schedule
    scheduler = scheduler.Scheduler(user.data)

except KeyboardInterrupt:
    print()
    sys.exit(-1)
