import sys
from models import menu_model
from controllers import menu_controller
from controllers import player_controller
from controllers import tournament_controller
from views import main_view
from views import player_view
from views import tournament_view


class MainMenuController:
    """Display the main menu"""

    def __init__(self):
        self.make_menu = menu_controller.MakeMenu()
        self.menu_list = menu_model.MenuList()
        self.clear = main_view.ClearScreen()
        self.main_menu_view = main_view.MainMenuView()

    def __call__(self):
        self.clear()
        self.main_menu_view()
        self.player_menu_controller = PlayerMenuController()
        self.tournament_menu_controller = TournamentMenuController()
        self.quit_app_controller = QuitAppController()

        entry = self.make_menu(self.menu_list.main_menu)
        match entry:
            case "1":
                self.player_menu_controller()
            case "2":
                self.tournament_menu_controller()
            case "3":
                self.quit_app_controller()


class PlayerMenuController(MainMenuController):
    """Display the player menu"""
    def __init__(self):
        super().__init__()
        self.player_menu_view = player_view.PlayerMenuView()
        self.main_menu_controller = MainMenuController()
        self.add_player_controller = player_controller.AddPlayer()
        self.update_player_rating_controller = player_controller.UpdatePlayerRating()
        self.players_report_controller = player_controller.PlayerReport()

    def __call__(self):
        self.clear()
        self.player_menu_view()
        entry = self.make_menu(self.menu_list.player_menu)
        match entry:
            case "1":
                self.add_player_controller()
            case "2":
                self.update_player_rating_controller()
            case "3":
                self.players_report_controller()
            case "4":
                self.main_menu_controller()


class TournamentMenuController(MainMenuController):
    """Display the tournament menu"""
    def __init__(self):
        super().__init__()
        self.tournament_menu_view = tournament_view.TournamentMenuView()
        self.create_tournament_controller = tournament_controller.CreateTournament()
        self.start_tournament_controller = tournament_controller.StartTournament()
        self.resume_tournament_controller = tournament_controller.ResumeTournament()
        self.tournament_report_controller = tournament_controller.TournamentReport()
        self.main_menu_controller = MainMenuController()

    def __call__(self):
        self.clear()
        self.tournament_menu_view()
        entry = self.make_menu(self.menu_list.tournament_menu)
        match entry:
            case "1":
                self.create_tournament_controller()
            case "2":
                self.start_tournament_controller()
            case "3":
                self.resume_tournament_controller()
            case "4":
                self.tournament_report_controller()
            case "5":
                self.main_menu_controller()


class QuitAppController:

    def __call__(self):
        sys.exit()
