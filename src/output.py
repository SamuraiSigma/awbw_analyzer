"""Module responsible for giving room info to the user."""

import easygui  # Window GUI
import sys      # exit


class Output:
    """Handles the output of the program."""

    def __init__(self, wars, no_room_message):
        """Reads dictionaries related to the rooms the user is
           in on the awbw website."""
        self._username = wars.username
        self._rooms = wars.current_rooms
        self._no_room = no_room_message
        self._title = "Advance Wars by Web Analyzer"

    def show_your_turn(self):
        """Shows rooms in which it is the user's turn to play."""
        if self._rooms:
            string = self.create_string(self._rooms)
            string = self._username + ", it's your turn on rooms:" \
                + string
            if not easygui.ccbox(string, self._title):
                sys.exit(0)
        elif self._no_room:
            string = self._username + ", it isn't your turn in any room!"
            if not easygui.ccbox(string, self._title):
                sys.exit(0)

    def create_string(self, lst):
        """Creates a string with the values in the given list."""
        string = ""
        for l in lst:
            string += "\n- " + l
        return string
