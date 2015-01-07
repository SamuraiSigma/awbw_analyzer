#!/usr/bin/env python3

"""Module from which the program treats arguments and is executed."""

import sys  # Command line arguments
import wars
import output


def read_args():
    """Reads and treats command line arguments."""
    username = ""
    all_rooms = False
    window = False

    for arg in sys.argv[1:]:
        if arg == "-a":
            all_rooms = True
        elif arg == "-w":
            window = True
        elif arg == "-h":
            usage()
        else:
            username += arg + " "

    if username == "":
        print("No username has been entered!")
        usage()

    return (username.rstrip(" "), all_rooms, window)


def usage():
    """Shows how to use the program."""
    print("Usage:\n\t%s <username> [-a] [-w] [-h]" % sys.argv[0])
    print("username: Your name on the awbw website.")
    print("-a: Show all rooms.")
    print("-w: Show data in a window GUI.")
    print("-h: Shows how to use the program, closing it afterwards.")
    sys.exit(1)

# -------------------------------------------------------------------


# Command line arguments analysis
username, all_rooms, window = read_args()

# Finds rooms in which it is the user's turn
wars = wars.Wars(username)
if not wars.connect_profile():
    print("Error when connecting to awbw website!")
    sys.exit(2)
wars.read_current_games()
wars.user_turn()

# Delivers output
output = output.Output(wars, window)
if all_rooms:
    output.show_all_rooms()
output.show_your_turn()
