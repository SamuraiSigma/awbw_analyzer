"""Contains the Scheduler class to run the program periodically."""

import easygui   # Window GUI
import os        # path.isfile()
import re        # Regex
import schedule  # Execute the program periodically
import sys       # exit()
import time      # sleep()

import output
import wars


class Scheduler:
    """Runs program from time to time."""

    def __init__(self, user_data, dummy_file, epoch_time):
        """Reads some data and begins the loop."""
        self._username = user_data[0]
        self._all_rooms = user_data[1]
        self._file = dummy_file
        self._epoch = epoch_time
        self.execute_program()
        self.run(user_data[2])

    def run(self, loop_time):
        """Loops the program according to a time specified by the user."""
        # Prepares schedule
        loop_time = float(loop_time)
        schedule.every(loop_time).minutes.do(self.execute_program)

        while True:
            # Checks if a new instance hasn't been created
            try:
                with open(self._file, 'r') as f:
                    f_time = float(f.readline())
                    if f_time != self._epoch:
                        sys.exit(0)
            except FileNotFoundError:
                easygui.msgbox("Error! Program terminated unexpectedly!")
                sys.exit(5)

            # Runs schedule
            schedule.run_pending()
            time.sleep(1)

    def execute_program(self):
        """Searches for rooms and displays them to the user."""
        # Finds rooms in which it is the user's turn
        war = wars.Wars(self._username)
        war.connect_profile()
        war.read_current_games()
        war.user_turn()

        # Delivers output
        out = output.Output(war)
        if self._all_rooms:
            out.show_all_rooms()
        out.show_your_turn()
