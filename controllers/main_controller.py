import sys
from controllers import menu_controller
from controllers import player_controller
from controllers import tournament_controller
from views import main_view
from views import player_view
from views import tournament_view


class MainMenuController:
    """Display the title and leads to the main menu"""

    def __init__(self):
        self.make_menu = menu_controller.MakeMenu()
        self.main_menu_view = main_view.MainMenuView()
        self.player_menu_view = player_view.PlayerMenuView()
        self.tournament_menu_view = tournament_view.TournamentMenuView()
        self.clear = main_view.ClearScreen()
        self.chosen_controller = None

    def __call__(self):
        self.clear()
        self.main_menu_view()
        entry = self.make_menu(self.make_menu.main_menu)
        match entry:
            case "1":
                self.go_to_player_menu_controller()
            case "2":
                self.go_to_tournament_menu_controller()
            case "3":
                self.go_to_quit_app_controller()

    def go_to_player_menu_controller(self):
        self.chosen_controller = PlayerMenuController()
        return self.chosen_controller()

    def go_to_tournament_menu_controller(self):
        self.chosen_controller = TournamentMenuController()
        return self.chosen_controller()

    def go_to_quit_app_controller(self):
        self.chosen_controller = QuitAppController()
        return self.chosen_controller()


class PlayerMenuController(MainMenuController):

    def __init__(self):
        super().__init__()
        self.add_player = player_controller.AddPlayer()
        self.update_player_rating = player_controller.UpdatePlayerRating()
        self.players_report = player_controller.PlayerReport()
        self.main_menu = MainMenuController()

    def __call__(self):
        self.clear()
        self.player_menu_view()
        entry = self.make_menu(self.make_menu.player_menu)
        match entry:
            case "1":
                self.add_player()
            case "2":
                self.update_player_rating()
            case "3":
                self.players_report()
            case "4":
                self.main_menu()


class TournamentMenuController(MainMenuController):

    def __init__(self):
        super().__init__()
        self.add_tournament = tournament_controller.CreateTournament()
        self.start_tournament = tournament_controller.StartTournament()
        self.tournament_report = tournament_controller.TournamentReport()
        self.main_menu = MainMenuController()

    def __call__(self):
        self.clear()
        self.tournament_menu_view()
        entry = self.make_menu(self.make_menu.tournament_menu)
        match entry:
            case "1":
                self.add_tournament()
            case "2":
                self.start_tournament()
            case "3":
                self.start_tournament.load_tournament_statement()
            case "4":
                self.tournament_report()
            case "5":
                self.main_menu()


class QuitAppController:

    def __call__(self):
        sys.exit()
