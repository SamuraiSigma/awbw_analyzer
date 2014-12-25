"""Module responsible for the Output class."""


class Output:
    """Handles the output of the program."""

    def __init__(self, rooms, your_turn):
        """Reads dictionaries related to the rooms the user is
           in on the awbw website."""
        self._rooms = rooms
        self._your_turn = your_turn

    def show_all_rooms(self):
        """Shows all rooms the user is currently playing in."""
        if self._rooms:
            print("Rooms you are currently in:")
            for r in self._rooms:
                print("-", self._rooms[r])

    def show_your_turn(self):
        """Shows rooms in which it is the user's turn to play."""
        if self._your_turn:
            print("It is your turn on the following rooms:")
            for y in self._your_turn:
                print("-", self._your_turn[y])
