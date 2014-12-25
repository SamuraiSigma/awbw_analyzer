""" ??? """

import re            # Regex
import requests      # Read info from an URL
import bs4           # Filter HTML


class awbw:
    """ ??? """

    def __init__(username, profile_page, game_page, wait_time):
        """Reads some initial data regarding the user and URL."""
        self.username = username
        self.profile_page = profile_page
        self.game_page = game_page
        self.wait_time = wait_time

    def connect():
        """Tries to connect to the user's profile page."""
        try:
            self.response = requests.get(self.profile_page + self.username,
                                         timeout=wait_time)
        except:
            return False
        return True

    def read_current_games(response):
        """Creates a dictionary with the rooms and their respective IDs
           that the user is currently playing in."""
        # Search for room names
        text = self.response.text.split("Completed Games")
        soup = bs4.BeautifulSoup(text[0])
        rooms = soup.select('a[href^=game.php?games_id=]')

        # Create the room dictionary
        self.game_dic = {}
        for r in rooms:
            id = re.search('id=\d+', str(r))
            id = id.group(0)
            id = self.format_id(id)
            name = re.search('>.*</a>', str(r))
            name = name.group(0)
            self.game_dic[id] = self.format_name(name)

    def format_name(name):
        """Fixes some html chars that can't be changed with bs4."""
        name = name.replace('>', '')
        name = name.replace('</a', '')
        name = name.replace(u'\xa0', u' ')
        return name

    def format_id(id):
        """Removes a tag from the id number."""
        return id.replace('id=', '')
