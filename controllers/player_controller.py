from datetime import datetime
from controllers import main_controller
from models import player_model
from views import player_view
import time
from operator import attrgetter


class MainPlayerController:
    def __init__(self):
        self.database = player_model.Database()
        self.players_table = self.database.players_table
        self.player_model = player_model.Player()
        self.clear = player_view.main_view.ClearScreen()


class AddPlayer(MainPlayerController):
    """Enter all the player's details, then add them into the player database"""

    def __init__(self):
        super().__init__()
        self.player_values = []
        self.main_menu_controller = main_controller.MainMenuController()
        self.table_view = player_view.main_view.TableView()
        self.player_headers = player_view.main_view.MainMenuView().player_headers_by_name
        self.add_player_view = player_view.AddPlayerView()

    def __call__(self):
        self.player_values.append(self.prompt_for_first_name())
        self.player_values.append(self.prompt_for_last_name())
        self.player_values.append(self.prompt_for_birthdate())
        self.player_values.append(self.prompt_for_gender())
        self.player_values.append(self.prompt_for_ranking())
        if self.validate_player() == 'save_player':
            self.player_model.add_to_database(self.player_values)
            print('The player has been added to the database')

        self.player_values.clear()
        self.main_menu_controller.go_to_player_menu_controller()

    @staticmethod
    def prompt_for_first_name():
        while True:
            first_name = input("Enter the player's the first name: ")
            if not first_name[0].isalpha():
                print("Please enter a valid first name")
                continue
            return first_name

    @staticmethod
    def prompt_for_last_name():
        while True:
            last_name = input("Enter the player's last name: ")
            if not last_name[0].isalpha():
                print("Please enter a valid last name")
                continue
            return last_name

    @staticmethod
    def prompt_for_birthdate():
        while True:
            birthdate = input("Enter the player's birthdate in the form of DD/MM/YYYY: ")
            try:
                datetime.strptime(birthdate, '%d/%m/%Y')
                return birthdate
            except ValueError:
                print("Please enter a valid birthdate in the form of DD/MM/YYYY")

    @staticmethod
    def prompt_for_gender():
        while True:
            gender = input("Enter the player's gender (W or M): ").lower()
            match gender:
                case 'w':
                    return 'W'
                case 'm':
                    return 'M'
                case _:
                    print("Please enter a valid gender (W or M)")

    @staticmethod
    def prompt_for_ranking():
        while True:
            ranking = input("Enter the player's ranking: ")
            if not ranking.isnumeric():
                print("Please enter a positive whole number")
                continue
            return ranking

    def validate_player(self):
        self.add_player_view.validate_player_view()
        self.table_view([self.player_headers, self.player_values], [])
        while True:
            entry = input("Would you like to save this player? (Y or N): ").lower()
            match entry:
                case 'y':
                    return 'save_player'
                case 'n':
                    return
                case _:
                    print("Please enter Y (for Yes) or N (for No)")


class UpdatePlayerRating(MainPlayerController):
    """Update the player's rating"""

    def __init__(self):
        super().__init__()
        self.main_menu_controller = main_controller.MainMenuController()
        self.update_player_rating_view = player_view.UpdateRatingView()
        self.display_player = player_view.DisplayPlayer()

    def __call__(self):
        self.clear()
        self.update_player_rating_view()
        players_unserialized = [self.player_model.unserialized(player) for player in self.players_table]
        self.display_player.reduced_table(players_unserialized)

        while True:
            player_id = input("Enter the Id of the player to update: ")

            if not player_id.isdigit():
                print("Please enter a valid player id.")
                continue
            # player_to_update = self.players_table.get(doc_id=int(player_id))
            player_to_update = [player for player in players_unserialized if player.player_id == int(player_id)]
            if not player_to_update:
                print("The id you entered is not in the list. Please enter a player id in the list.")
                continue

            new_rating = input("Enter the new rating: ")
            if not new_rating.isdigit() > 0:
                print("Please enter a positive number.")
                continue
            self.update_player_rating_view.player_to_update_title_view()
            # self.display_player_view.display_single_player(int(player_id))
            self.display_player.reduced_table(player_to_update)
            print('The new rating:', new_rating)
            self.players_table.update({"rating": new_rating}, doc_ids=[int(player_id)])
            time.sleep(2.5)
            self.main_menu_controller.go_to_player_menu_controller()


class DisplayPlayerReport(MainPlayerController):
    """Display Players list alphabetically and by rating"""

    def __init__(self):
        super().__init__()
        self.make_menu = main_controller.menu_controller.MakeMenu()
        self.player_report_view = player_view.PlayerReportView()
        self.player_menu_view = player_view.PlayerMenuView()
        self.main_menu_controller = main_controller.MainMenuController()
        self.display_player = player_view.DisplayPlayer()

    def __call__(self):
        self.clear()
        self.player_report_view()
        players_unserialized = [self.player_model.unserialized(player) for player in self.players_table]
        # self.display_player.full_table(players_unserialized)

        while True:
            entry = self.make_menu(self.make_menu.players_report_menu)
            match entry:
                case "1":
                    self.clear()
                    self.player_report_view()
                    self.player_report_view.display_title_alphabetically()
                    players_unserialized.sort(key=attrgetter('first_name'))
                    self.display_player.full_table(players_unserialized)
                case "2":
                    self.clear()
                    self.player_report_view()
                    self.player_report_view.display_title_rating()
                    players_unserialized.sort(key=attrgetter('rating'), reverse=True)
                    self.display_player.full_table(players_unserialized)
                case "3":
                    self.main_menu_controller.go_to_player_menu_controller()

# print(f'list is: {add_player.player_values}')
# if any(map(str.isdigit, 'nnnn')):
#     print('number included')
# def validate(date_text):
#     try:
#         datetime.strptime(date_text, '%d-%m-%Y')
#         return True
#     except ValueError:
#         raise ValueError("Incorrect data format, should be DD-MM-YYYY")


# datetime.strptime(date_string, format)
# date.strftime(format)

# validate('13-12-2000')
# print(str.casefold('N'))

# today = datetime.date.today()
# now = datetime.now().strftime('%d-%m-%Y')
# strf = datetime.today().strftime('%d-%m-%Y')
# strp = datetime.strptime(strf, '%d-%m-%Y')
# print(datetime.datetime.strptime(str(td), '%d-%m-%Y'))
# print(dir(datetime))
# print(help(datetime))
# print(now)
# db = MainPlayerController()
# tb = db.players_table
# print(db.all())
# help(db)
# player_keys = ["Last Name", "First Name", "Date of birth", "Gender", "Ranking"]
# player_values = ['Doe', 'John', '13/08/1970', 'M', '200']
# print(f'{"Summary of Player Details":+^60}')
# print(tabulate([player_keys, player_values], tablefmt="simple_grid"))
# print(tb)
