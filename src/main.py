#!/usr/bin/env python3

"""Module from which the program treats arguments and is executed."""

import sys  # Command line arguments
import user
import wars
import output


# -------------------------------------------------------------------

# Collects initial data from the user
user = user.User()
username = user.data[0]
all_rooms = user.data[1]

# Finds rooms in which it is the user's turn
wars = wars.Wars(username)
if not wars.connect_profile():
    print("Error when connecting to awbw website!")
    sys.exit(2)
wars.read_current_games()
wars.user_turn()

# Delivers output
output = output.Output(wars)
if all_rooms:
    output.show_all_rooms()
output.show_your_turn()
