from views import main_view


# from controllers import player_controller


class PlayerMenuView(main_view.MainMenuView):
    """Display all the players in the database"""

    def __init__(self):
        super().__init__()

    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.app_name)
        self.display_filled_line()
        self.display_text_surrounded(self.menu_titles[1])
        self.display_filled_line()


class AddPlayerView(main_view.MainMenuView):
    """Display all the players in the database"""

    def __init__(self):
        super().__init__()

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
    """Display all the players in the database"""

    def __init__(self):
        super().__init__()

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
    """Display all the players in the database"""

    def __init__(self):
        super().__init__()
        self.table_view = main_view.TableView()
        # self.players_table = player_controller.MainPlayerController().players_table
        self.line = None
        self.lines = []
        # self.player_doc_id = None

    # def display_all_players(self):
    #     for player in self.players_table:
    #         self.line = player['player_id'], player['first_name'], player['last_name'], player['rating']
    #         self.lines.append(self.line)
    #     self.table_view(self.lines, self.player_headers_by_id)
    #
    # def display_single_player(self, player_doc_id):
    #     self.lines.clear()
    #     player = self.players_table.get(doc_id=int(player_doc_id))
    #     self.line = player['player_id'], player['first_name'], player['last_name'], player['rating']
    #     self.lines.append(self.line)
    #     self.table_view(self.lines, self.player_headers_by_id)

    # def display_table(self, player_list, view_table):
    #     for player in player_list:
    #         match view_table:
    #             case 'add_player_view':
    #                self.line = player.first_name, player.last_name, player.gender, player.date_of_birth, player.rating
    #             case 'update_rating_view':
    #                self.line = player.first_name, player.last_name, player.gender, player.date_of_birth, player.rating
    #             case 'add_tournament_view':
    #                 self.line = player.player_id, player.first_name, player.last_name, player.date_of_birth
    #         self.lines.append(self.line)
    #     self.table_view(self.lines, self.player_headers_by_name)
    #     self.lines.clear()

    def full_table(self, player_list):
        for player in player_list:
            self.line = player.first_name, player.last_name, player.gender, player.date_of_birth, player.rating
            self.lines.append(self.line)
        self.table_view(self.lines, self.player_headers_by_name)
        self.lines.clear()

    # def table_by_dob(self, player_list):
    #     for player in player_list:
    #         self.line = player.player_id, player.first_name, player.last_name, player.date_of_birth
    #         self.lines.append(self.line)
    #     self.table_view(self.lines, self.player_headers_by_id)
    #     self.lines.clear()

    def reduced_table(self, player_list):
        for player in player_list:
            self.line = player.player_id, player.first_name, player.last_name, player.rating
            self.lines.append(self.line)
        self.table_view(self.lines, self.player_headers_by_id)
        self.lines.clear()

    def add_player_to_tournament_table(self, player_list):
        for player in player_list:
            self.line = player.player_id, player.first_name, player.last_name, player.date_of_birth
            self.lines.append(self.line)
        self.table_view(self.lines, self.player_headers_by_dob)
        self.lines.clear()


class PlayerReportView(main_view.MainMenuView):
    """Display all the players in the database"""

    def __init__(self):
        super().__init__()
        # self.table_view = main_view.TableView()
        # self.line = None
        # self.lines = []

    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.menu_options[2])
        self.display_filled_line()
        self.display_empty_line()

    # def display_player_report(self, sorted_list):
    #     for player in sorted_list:
    #         self.line = player.first_name, player.last_name, player.gender, player.date_of_birth, player.rating
    #         self.lines.append(self.line)
    #     self.table_view(self.lines, self.player_headers_by_name)
    #     self.lines.clear()

    def display_title_alphabetically(self):
        self.display_text_surrounded(self.player_references[3])

    def display_title_rating(self):
        self.display_text_surrounded(self.player_references[4])
