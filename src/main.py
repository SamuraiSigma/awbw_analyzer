#!/usr/bin/env python3

"""Module from which the program treats arguments and is executed."""

import sys  # Command line arguments
import wars
import output


# Global options
username = ""
profile_name = "http://awbw.amarriner.com/profile.php?username="
game_name = "http://awbw.amarriner.com/game.php?games_id="


def usage():
    """Shows how to use the program."""
    print("Usage:\n\t%s <username> [-a] [-w] [-h]" % sys.argv[0])
    print("username: Your name on the awbw website.")
    print("-a: Show all rooms.")
    print("-w: Show data in a window GUI.")
    print("-h: Shows how to use the program, closing it afterwards.")
    exit(1)

# -------------------------------------------------------------------

all_rooms = False
window = False

# Command line arguments analysis
for arg in sys.argv[1:]:
    if arg == "-a":
        all_rooms = True
    elif arg == "-w":
        window = True
    elif arg == "-h":
        usage()
    else:
        username = arg

if username == "":
    print("No username has been entered!")
    usage()

# Finds rooms in which it is the user's turn
wars = wars.Wars(username, game_name)
if not wars.connect(profile_name + username):
    print("Error when connecting to awbw website!")
    exit(2)
wars.read_current_games()
wars.user_turn()

# Delivers output
output = output.Output(wars, window)
if all_rooms:
    output.show_all_rooms()
output.show_your_turn()
