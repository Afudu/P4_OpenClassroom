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
        self.add_player_controller = player_controller.AddPlayer()
        self.update_player_rating_controller = player_controller.UpdatePlayerRating()
        self.players_report_controller = player_controller.DisplayPlayerReport()
        self.main_menu_controller = MainMenuController()

    def __call__(self):
        self.clear()
        self.player_menu_view()
        entry = self.make_menu(self.make_menu.player_menu)
        match entry:
            case "1":
                self.chosen_controller = self.add_player_controller()
            case "2":
                self.chosen_controller = self.update_player_rating_controller()
            case "3":
                self.chosen_controller = self.players_report_controller()
            case "4":
                self.chosen_controller = self.main_menu_controller()


class TournamentMenuController(MainMenuController):

    def __init__(self):
        super().__init__()
        self.add_tournament_controller = tournament_controller.AddTournamentController()
        self.start_tournament_controller = tournament_controller.StartTournamentController()
        self.tournament_report_controller = tournament_controller.TournamentReport()
        self.main_menu_controller = MainMenuController()

    def __call__(self):
        self.clear()
        self.tournament_menu_view()
        entry = self.make_menu(self.make_menu.tournament_menu)
        match entry:
            case "1":
                self.chosen_controller = self.add_tournament_controller()
            case "2":
                self.chosen_controller = self.start_tournament_controller()
            case "3":
                self.chosen_controller = self.start_tournament_controller.load_tournament_statement()
            case "4":
                self.chosen_controller = self.tournament_report_controller()
            case "5":
                self.main_menu_controller()


class QuitAppController:

    def __call__(self):
        sys.exit()
