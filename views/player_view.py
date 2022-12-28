from views import main_view


class PlayerMenuView(main_view.MainMenuView):
    """Creates the player main menu header"""
    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.app_name)
        self.display_filled_line()
        self.display_text_surrounded(self.menu_titles[1])
        self.display_filled_line()


class AddPlayerView(main_view.MainMenuView):
    """Creates the Add Player menu header"""
    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.app_name)
        self.display_filled_line()
        self.display_text_surrounded(self.menu_titles[2])
        self.display_filled_line()

    def validate_player_view(self):
        self.display_empty_line()
        self.display_text_surrounded(self.player_references[0])


class UpdateRatingView(main_view.MainMenuView):
    """Creates the Update Player Rating menu header"""

    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.menu_options[1])
        self.display_filled_line()
        self.display_empty_line()
        self.display_text_surrounded(self.player_references[1])

    def player_to_update_title_view(self):
        self.display_empty_line()
        self.display_text_surrounded(self.player_references[2])


class DisplayPlayer(main_view.MainMenuView):
    """Displays the players in the database"""

    def __init__(self):
        super().__init__()
        self.table_view = main_view.TableView()
        self.line = None
        self.lines = []

    def full_table(self, player_list):
        for player in player_list:
            self.line = player.first_name, \
                        player.last_name, \
                        player.gender, \
                        player.date_of_birth, \
                        player.rating
            self.lines.append(self.line)
        self.table_view(self.lines, self.player_headers_by_name)
        self.lines.clear()

    def reduced_table(self, player_list):
        for player in player_list:
            self.line = player.player_id, \
                        player.first_name, \
                        player.last_name, \
                        player.rating
            self.lines.append(self.line)
        self.table_view(self.lines, self.player_headers_by_id)
        self.lines.clear()

    def add_player_to_tournament_table(self, player_list):
        for player in player_list:
            self.line = player.player_id, \
                        player.first_name, \
                        player.last_name, \
                        player.date_of_birth
            self.lines.append(self.line)
        self.table_view(self.lines, self.player_headers_by_dob)
        self.lines.clear()


class PlayerReportView(main_view.MainMenuView):
    """Creates the Update Player Report menu header"""
    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.menu_options[2])
        self.display_filled_line()
        self.display_empty_line()

    def display_title_alphabetically(self):
        self.display_text_surrounded(self.player_references[3])

    def display_title_rating(self):
        self.display_text_surrounded(self.player_references[4])
