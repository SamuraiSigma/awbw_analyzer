#!/usr/bin/env python3

"""Module from which the program treats arguments and is executed."""

import sys     # Command line arguments
import wars
import output


# Global options
username = "Cyrus095"
profile_name = "http://awbw.amarriner.com/profile.php?username="
game_name = "http://awbw.amarriner.com/game.php?games_id="


def usage():
    """Shows how to use the program."""
    print("Usage:\n\t%s [-h] [-w]" % sys.argv[0])
    print("-h: Shows how to use the program, closing it afterwards.")
    exit(1)

# -------------------------------------------------------------------

# Command line arguments analysis
for arg in sys.argv[1:]:
    if arg == "-h":
        usage()
    else:
        print("Error: Argument '" + arg + "' not recognized!")
        usage()

# Finds rooms in which it is the user's turn
wars = wars.Wars(username, game_name)
if not wars.connect(profile_name + username):
    print("Error when connecting to awbw website!")
    exit(2)
wars.read_current_games()
wars.user_turn()

# Delivers output
output = output.Output(wars.game_dic, wars.current_rooms)
output.show_all_rooms()
output.show_your_turn()