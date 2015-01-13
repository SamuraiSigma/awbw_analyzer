"""Module responsible for receiving info from the user."""

import easygui  # Window GUI
import re       # Regex
import sys      # exit()


class User:
    """Handles the input of the program."""

    def __init__(self):
        self._file = ".user.txt"
        self._data = []
        self.read_from_user()

    def read_file(self):
        """Reads previously collected user data from a file."""
        data = []
        try:
            with open(self._file, 'r') as _file:
                for line in _file:
                    data.append(line.rstrip('\n'))
        except FileNotFoundError:
            pass
        return data

    def write_file(self):
        """Writes collected user data on a file for later access."""
        with open(self._file, 'w') as _file:
            for data in self._data:
                _file.write(str(data) + '\n')

    def read_from_user(self):
        """Collects username and preferences directly from user input."""
        msg = "Please type in your username and preferred options."
        title = "Advance Wars by Web Analyzer"
        options = ["Username",
                   "Show all rooms? (Yes=1, No=0)",
                   "Minutes to run program again"]
        values = self.read_file()

        while True:
            self._data = easygui.multenterbox(msg, title, options, values)
            if self._data is None:
                sys.exit(1)
            if self.process_data():
                break
        self.write_file()

    def process_data(self):
        """Checks if information given by the user is valid."""
        name = self._data[0]
        if name == "":
            return False

        all_rooms = self._data[1]
        if all_rooms == "" or all_rooms.upper() == "0":
            self._data[1] = 0
        else:
            self._data[1] = 1

        time = self._data[2]
        if time == "":
            self._data = "120"
        elif not re.search('(\d*\.)?\d+', time):
            return False

        return True

    @property
    def data(self):
        return self._data
