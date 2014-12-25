"""Module responsible for the Wars class."""

import re            # Regex
import requests      # Read info from an URL
import bs4           # Filter HTML


class Wars:
    """Handles data read from the awbw website."""

    def __init__(self, username, game_page):
        """Reads some initial data regarding the user and URL."""
        self._username = username
        self._game_page = game_page
        self._wait_time = 5

    def connect(self, page):
        """Tries to connect to the user's profile page."""
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
        soup = bs4.BeautifulSoup(text[0])
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
            if self.connect(self._game_page + d):
                if re.search("Game.*Updated:" + user, self._response.text):
                    self._current_rooms[d] = dic[d]

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
    def game_dic(self):
        return self._game_dic

    @property
    def current_rooms(self):
        return self._current_rooms
