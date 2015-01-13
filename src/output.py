"""Module responsible for giving room info to the user."""

import easygui  # Window GUI


class Output:
    """Handles the output of the program."""

    def __init__(self, wars):
        """Reads dictionaries related to the rooms the user is
           in on the awbw website."""
        self._wars = wars
        self._title = "Advance Wars by Web Analyzer"

    def show_all_rooms(self):
        """Shows all rooms the user is currently playing in."""
        if self._wars.game_dic:
            string = self.create_string(self._wars.game_dic)
            string = self._wars.username + ", you are in rooms:" + string
            easygui.msgbox(string, title=self._title)

    def show_your_turn(self):
        """Shows rooms in which it is the user's turn to play."""
        if self._wars.current_rooms:
            string = self.create_string(self._wars.current_rooms)
            string = self._wars.username + ", it's your turn on rooms:" \
                + string
            easygui.msgbox(string, title=self._title)

    def create_string(self, dic):
        """Creates a string with the values in the given dictionary."""
        string = ""
        for d in dic:
            string += "\n- " + dic[d]
        return string
