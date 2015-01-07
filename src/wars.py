"""Module responsible for the Wars class."""

import re            # Regex
import requests      # Read info from an URL
import sys           # exit()
import bs4           # Filter HTML


# Advance Wars by Web URLs
profile_name = "http://awbw.amarriner.com/profile.php?username="
game_name = "http://awbw.amarriner.com/game.php?games_id="


class Wars:
    """Handles data read from the awbw website."""

    def __init__(self, username):
        """Reads some initial data regarding the user and URL."""
        self._username = username
        self._wait_time = 5

    def connect_profile(self):
        """Attempts to connect to the user's profile page."""
        return self.get_response(profile_name + self._username)

    def get_response(self, page):
        """Tries to get a response from a URL."""
        try:
            self._response = requests.get(page, timeout=self._wait_time)
        except:
            return False
        return True

    def read_current_games(self):
        """Creates a dictionary with the rooms and their respective IDs
           that the user is currently playing in."""
        # Search for room names
        text = self._response.text.split("Completed Games")
        text = text[0].split("Current Games")
        try:
            soup = bs4.BeautifulSoup(text[1])
        except IndexError:
            print("Error! Username not found on awbw!")
            sys.exit(3)
        rooms = soup.select('a[href^=game.php?games_id=]')

        # Create the room dictionary
        self._game_dic = {}
        for r in rooms:
            id = re.search('id=\d+', str(r))
            id = id.group(0)
            id = self.format_id(id)
            name = re.search('>.*</a>', str(r))
            name = name.group(0)
            self._game_dic[id] = self.format_name(name)

    def user_turn(self):
        """Checks if it is the user's turn in the rooms."""
        user = "<b>" + self._username + "</b>"

        self._current_rooms = {}
        for d in self._game_dic:
            if self.get_response(game_name + d):
                if re.search(user, self._response.text):
                    self._current_rooms[d] = self._game_dic[d]

    def format_name(self, name):
        """Fixes some html chars that can't be changed with bs4."""
        name = name.replace('>', '')
        name = name.replace('</a', '')
        name = name.replace(u'\xa0', u' ')
        return name

    def format_id(self, id):
        """Removes a tag from the id number."""
        return id.replace('id=', '')

    @property
    def username(self):
        return self._username

    @property
    def game_dic(self):
        return self._game_dic

    @property
    def current_rooms(self):
        return self._current_rooms
