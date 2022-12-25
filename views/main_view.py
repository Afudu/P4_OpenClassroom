import os
from tabulate import tabulate


class ClearScreen:
    """Clear the terminal"""

    def __call__(self):
        # for windows
        if os.name == 'nt':
            _ = os.system('cls')
        # for mac and linux
        else:
            _ = os.system('clear')


class TableView:
    """Display a list of items in a tabular format"""

    def __init__(self):
        self.list_to_display = None
        self.headers = None

    def __call__(self, list_to_display, headers):
        self.list_to_display = list_to_display
        self.headers = headers
        print(tabulate(self.list_to_display, self.headers, tablefmt="simple_grid"))


class MainMenuView:
    """Create the views"""

    def __init__(self):
        self.welcome_message = "Welcome to"
        self.app_name = "Tournament Manager"
        self.menu_titles = ["Main Menu", "Player Menu", "Tournament Menu"]
        self.menu_options = ["Add Player", "Update Player Rating", "Players Report",
                             "Add Tournament", "Start Tournament", "Resume Tournament", "Tournament Report"]
        self.text = None
        self.player_headers_by_id = ['Id', 'First Name', 'Last Name', 'Rating']
        self.player_headers_by_name = ['First Name', 'Last Name', 'Gender', 'Date of Birth', 'Rating']
        self.player_headers_by_dob = ['Id', 'First Name', 'Last Name', 'Date of Birth']
        self.player_references = ["Summary of Player Details", "Player List", "Player to update",
                                  "Player List by First Name", "Player List by Rating"]
        self.tournament_headers_by_name = ['Name', 'Venue', 'Start Date', 'Number of Rounds', 'Time Control',
                                           'Description', 'Players']
        self.tournament_headers_by_id = ['Id', 'Tournament Name', 'Venue', 'Start Date']
        self.tournaments_in_progress_headers = ['Id', 'Tournament Name', 'Venue', 'Rounds played']
        self.tournament_references = ["Summary of Tournament Details", "Tournaments not yet started",
                                      "Tournaments in progress", "Tournament list", "Rounds Played",
                                      "Matches per Round"]

    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.app_name)
        self.display_filled_line()
        self.display_text_surrounded(self.menu_titles[0])
        self.display_filled_line()

    @staticmethod
    def display_text_surrounded(text):
        print(f'{text:+^50}')

    @staticmethod
    def display_empty_line():
        print()

    @staticmethod
    def display_filled_line():
        print(f'{"":+>50}')

# headers = ['Id', 'First Name', 'Last Name', 'Gender', 'Date of Birth', 'Rating']
# nl = headers[1:]
# print(nl.pop(2))
# print(nl)
