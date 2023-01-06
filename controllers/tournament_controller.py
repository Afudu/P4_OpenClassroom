from datetime import datetime
from controllers import main_controller
from controllers import player_controller
from models import tournament_model
from models import round_model
from views import main_view
from views import tournament_view
from views import player_view
import time
from operator import attrgetter


class MainTournamentController:
    def __init__(self):
        self.database = tournament_model.Database()
        self.tournaments_table = self.database.tournaments_table
        self.players_table = self.database.players_table
        self.rounds_table = self.database.rounds_table
        self.player_model = player_controller.player_model.Player()
        self.tournament_model = tournament_model.Tournament()
        self.round_model = round_model.Round()
        self.clear = main_view.ClearScreen()
        self.table_view = main_view.TableView()

    @staticmethod
    def go_to_tournament_menu_controller():
        tournament_menu_controller = main_controller.TournamentMenuController()
        return tournament_menu_controller()


class CreateTournament(MainTournamentController):
    """Prompt for the details then add them into the tournament database"""

    def __init__(self):
        super().__init__()
        self.tournament_object = None
        self.tournament_values = []
        self.player_ids = []
        self.players_unserialized = []
        self.add_tournament_view = tournament_view.AddTournamentView()
        self.make_menu = main_controller.menu_controller.MakeMenu()
        self.display_player = player_view.DisplayPlayer()
        self.headers = main_view.MainMenuView().tournament_headers_by_name

    def __call__(self):
        self.tournament_values.append(self.prompt_for_name())
        self.tournament_values.append(self.prompt_for_venue())
        self.tournament_values.append(self.prompt_for_start_date())
        self.tournament_values.append(self.prompt_for_number_of_rounds())
        self.tournament_values.append(self.prompt_for_time_control())
        self.tournament_values.append(self.prompt_for_description())
        if self.validate_tournament() == 'save_tournament':
            tournament_id = self.tournament_model.add_to_database(self.tournament_values)
            print('Saving the tournament data...')
            time.sleep(2)
            self.tournament_object = self.tournaments_table.get(doc_id=int(tournament_id))
            unserialized_tournament = self.tournament_model.unserialized(self.tournament_object)
            self.prompt_for_players(unserialized_tournament)

        self.tournament_values.clear()
        self.go_to_tournament_menu_controller()

    @staticmethod
    def prompt_for_name():
        while True:
            tournament_name = input("Enter the tournament name: ")
            if not tournament_name[0].isalpha():
                print("Please enter a valid name.")
                continue
            return tournament_name

    @staticmethod
    def prompt_for_venue():
        while True:
            tournament_name = input("Enter the tournament venue: ")
            if not tournament_name[0].isalpha():
                print("Please enter a valid tournament venue.")
                continue
            return tournament_name

    @staticmethod
    def prompt_for_start_date():
        while True:
            start_date = input("Enter the tournament start date in the form of DD/MM/YYYY: ")
            try:
                datetime.strptime(start_date, '%d/%m/%Y')
                return start_date
            except ValueError:
                print("Please enter a valid date in the form of DD/MM/YYYY")

    @staticmethod
    def prompt_for_number_of_rounds():
        number_of_rounds = 4

        while True:
            entry = input("The default number of rounds is "
                          + str(number_of_rounds) +
                          "\nWould you like to change it? (Y or N): ").lower()
            match entry:
                case 'y':
                    while True:
                        new_number_of_rounds = input("Enter the new number of rounds: ")
                        if not (new_number_of_rounds.isdigit()
                                and int(new_number_of_rounds) > 0
                                and (int(new_number_of_rounds) % 2 == 0)):
                            print("Please enter a positive even number.")
                            continue
                        return new_number_of_rounds
                case 'n':
                    return number_of_rounds
                case _:
                    print("Please enter Y (for Yes) or N (for No)")

    def prompt_for_time_control(self):
        print('Please select a time control')
        entry = self.make_menu(self.make_menu.time_control_menu)
        match entry:
            case "1":
                return 'Bullet'
            case "2":
                return 'Blitz'
            case "3":
                return 'Rapid'

    @staticmethod
    def prompt_for_description():
        while True:
            description = input("Enter the tournament description: ")
            if not len(description) > 0:
                print("Please enter a description")
                continue
            return description

    def prompt_for_players(self, tournament_object):
        self.tournament_object = tournament_object
        self.player_ids = self.tournament_object.player_ids
        self.players_unserialized = player_controller.PlayersUnserialized()
        players_unserialized = self.players_unserialized()
        self.add_tournament_view.add_player_view()
        self.display_player.add_player_to_tournament_table(players_unserialized)

        choice = input("Please add an even number of players in the tournament.\n"
                       "\nWould you like to add the player(s) now? (Y or N): ").lower()

        while True:
            if len(self.player_ids) > 0:
                choice = input("\nWould you like to continue adding a player? (Y or N): ").lower()
            match choice:
                case 'y':
                    print('Players in the tournament: ' + str(self.player_ids))
                    player_being_added = int(len(self.player_ids)) + 1
                    print()
                    print('Adding Player ' + str(player_being_added))

                    entry = input("Enter the id of the player to add: ")
                    if not entry.isdigit():
                        print("Please enter a valid player id.")
                        continue
                    if int(entry) in self.player_ids:
                        print("This player has already been added. Please add another.")
                        continue

                    player_to_add = [player for player in players_unserialized if player.player_id == int(entry)]
                    if not player_to_add:
                        print("Your choice is not in the list. Please enter an id in the list.")
                        continue
                    self.player_ids.append(int(entry))
                    self.tournament_model.update_players(self.player_ids, tournament_object.tournament_id)
                case 'n':
                    self.tournament_model.update_players(self.player_ids, tournament_object.tournament_id)
                    self.go_to_tournament_menu_controller()
                case _:
                    print("Please enter Y (for Yes) or N (for No)")

    def validate_tournament(self):
        self.add_tournament_view.validate_tournament_view()
        self.table_view([self.headers, self.tournament_values], [])
        while True:
            entry = input("\nWould you like to save this tournament ? (Y or N): ").lower()
            match entry:
                case 'y':
                    return 'save_tournament'
                case 'n':
                    break
                case _:
                    print("Please enter Y (for Yes) or N (for No)")


class StartTournament(MainTournamentController):
    """Starts a tournament created"""
    MATCHES_PLAYED = []
    ROUNDS_PLAYED = []

    def __init__(self):
        super().__init__()
        self.create_tournament = None
        self.player_ids = []
        self.tournament_status = None
        self.tournament_object = None
        self.sorted_players = None
        self.display_tournament = tournament_view.DisplayTournament()
        self.start_tournament_view = tournament_view.StartTournamentView()
        self.resume_tournament_view = tournament_view.ResumeTournamentView()
        self.end_tournament_view = tournament_view.TournamentResultsView()

    def __call__(self):
        self.clear()

        # tournament_object
        self.tournament_object = self.check_players(self.prompt_for_tournaments_not_started())

        # prompt to start rounds
        while True:
            entry = input("\nWould you like to start the rounds now ? (Y or N): ").lower()
            match entry:
                case 'y':
                    self.generate_rounds(self.tournament_object)
                case 'n':
                    self.go_to_tournament_menu_controller()
                case _:
                    print("Please enter Y (for Yes) or N (for No)")

    def generate_rounds(self, tournament_object):
        self.tournament_object = tournament_object
        self.sorted_players = []

        # run round1
        self.sorted_players = self.sort_players_first_round(self.tournament_object)
        self.tournament_object.round_ids.append(self.round_model.run(self.tournament_object, self.sorted_players))
        self.save_tournament_statement(self.tournament_object)
        self.prompt_to_postpone_tournament()

        # running all the others rounds
        for i in range(2, int(self.tournament_object.number_of_rounds) + 1):
            self.sorted_players.clear()
            self.sorted_players = self.sort_players_other_rounds(self.tournament_object)
            self.tournament_object.round_ids.append(self.round_model.run(self.tournament_object, self.sorted_players))
            self.save_tournament_statement(self.tournament_object)

            # last round excluded from prompt to postpone
            if i < int(self.tournament_object.number_of_rounds):
                self.prompt_to_postpone_tournament()

        # display tournament rounds and matches then prompt to return to menu
        self.end_tournament_view.end_tournament_header()
        self.end_tournament_view(self.tournament_object.round_ids)
        self.go_to_tournament_menu_controller()

    def save_tournament_statement(self, tournament_object):
        self.tournament_object = tournament_object
        round_object = self.tournament_object.round_ids[-1]
        round_serialized = round_object.serialized()

        round_id = self.rounds_table.insert(round_serialized)
        self.ROUNDS_PLAYED.append(round_id)
        self.tournaments_table.update({"round_ids": self.ROUNDS_PLAYED},
                                      doc_ids=[self.tournament_object.tournament_id])

    def prompt_for_tournaments_not_started(self):

        self.start_tournament_view()

        not_started = [tournament for tournament in self.tournaments_table if tournament['round_ids'] == []]
        if not not_started:
            print('\nThere are no tournaments awaiting to be started. Please add a tournament.')
            time.sleep(2)
            self.go_to_tournament_menu_controller()
        unserialized_not_started = [self.tournament_model.unserialized(tournament) for tournament in not_started]
        self.display_tournament.default(unserialized_not_started)

        while True:

            entry = input("Enter the Id of the tournament to start: ")
            if not entry.isdigit():
                print("Please enter a valid tournament id.")
                continue

            selected_tournament = self.tournaments_table.get(doc_id=int(entry))
            if not selected_tournament:
                print("The id you entered is not in the list. Please enter a valid tournament id.")
                continue
            unserialized_selected = self.tournament_model.unserialized(selected_tournament)

            return unserialized_selected

    def prompt_to_postpone_tournament(self):
        while True:
            entry = input("\nWould you like to postpone and resume the tournament later ?"
                          " (Y or N): ").lower()
            match entry:
                case 'y':
                    self.go_to_tournament_menu_controller()
                case 'n':
                    return self
                case _:
                    print("Please enter Y (for Yes) or N (for No)")

    def check_players(self, tournament_object):
        self.tournament_object = tournament_object
        self.create_tournament = CreateTournament()

        players = self.tournament_object.player_ids

        if not players:
            print("\nThere are no players in this tournament.\nPlease add an even number of"
                  " players to start the tournament.")
            time.sleep(2.5)
            self.create_tournament.prompt_for_players(self.tournament_object)

        elif not (len(players) > 0 and len(players) % 2 == 0):
            print(f"\n{len(players)} player(s) in this tournament.\n"
                  f"Please add an even number of players to start the tournament.")
            time.sleep(2.5)
            self.create_tournament.prompt_for_players(self.tournament_object)

        print(f"\nThere are {len(players)} player(s) in this tournament.")

        while True:
            entry = input("\nWould you like to add more players ? (Y or N): ").lower()
            match entry:
                case 'y':
                    self.create_tournament.prompt_for_players(self.tournament_object)
                case 'n':
                    return self.tournament_object
                case _:
                    print("Please enter Y (for Yes) or N (for No)")

    def sort_players_first_round(self, tournament_object):
        """ return a list of players sorted by ranking"""
        player_instances = []

        self.tournament_object = tournament_object
        player_ids = self.tournament_object.player_ids

        for player_id in player_ids:
            player = self.players_table.get(doc_id=player_id)
            player_unserialized = self.player_model.unserialized(player)
            player_instances.append(player_unserialized)

        # sort player instances by ranking
        player_instances.sort(key=attrgetter('rating'), reverse=True)

        for i in range(int(len(player_instances) / 2)):
            player_1 = player_instances[i]
            player_2 = player_instances[i + int(len(player_instances) / 2)]
            self.sorted_players.append(player_1)
            self.sorted_players.append(player_2)
            self.MATCHES_PLAYED.append({player_1.player_id, player_2.player_id})
        return self.sorted_players

    def sort_players_other_rounds(self, tournament_object):
        """ Return a list of players sorted by score; if score are equals, sort by rating."""

        players_sorted_by_score = []
        player_instances = []
        match_to_try = set()

        self.tournament_object = tournament_object
        player_ids = self.tournament_object.player_ids

        for player_id in player_ids:
            player = self.players_table.get(doc_id=player_id)
            player_unserialized = self.player_model.unserialized(player)
            player_instances.append(player_unserialized)

        # Sort players by score; if score are equal, sort by rating.
        player_instances.sort(key=attrgetter('tournament_score', 'rating'), reverse=True)

        for player_1 in player_instances:

            if player_1 in players_sorted_by_score:
                continue
            else:
                try:
                    player_2 = player_instances[player_instances.index(player_1) + 1]
                except IndexError:
                    break

            match_to_try.add(player_1.player_id)
            match_to_try.add(player_2.player_id)

            # compare match_to_try with matches already played
            while match_to_try in self.MATCHES_PLAYED:
                print(f"The match {player_1} Vs {player_2} has already been played.")
                time.sleep(1)
                match_to_try.remove(player_2.player_id)
                try:
                    player_2 = player_instances[player_instances.index(player_2) + 1]
                except IndexError:
                    break
                match_to_try.add(player_2.player_id)
                continue

            else:
                print(f"Adding match {player_1} Vs {player_2}")
                players_sorted_by_score.append(player_1)
                players_sorted_by_score.append(player_2)
                self.MATCHES_PLAYED.append({player_1.player_id, player_2.player_id})
                player_instances.pop(player_instances.index(player_2))
                match_to_try.clear()
                time.sleep(1)

        return players_sorted_by_score


class ResumeTournament(MainTournamentController):
    """Resume a tournament postponed"""

    StartTournament.MATCHES_PLAYED = []
    StartTournament.ROUNDS_PLAYED = []

    def __init__(self):
        super().__init__()
        self.create_tournament = None
        self.tournament_object = None
        self.sorted_players = None
        self.start_tournament = StartTournament()
        self.display_tournament = tournament_view.DisplayTournament()
        self.resume_tournament_view = tournament_view.ResumeTournamentView()
        self.end_tournament_view = tournament_view.TournamentResultsView()

    def __call__(self):
        self.clear()

        # tournament_object
        self.tournament_object = self.prompt_for_tournaments_in_progress()

        # prompt to start
        while True:
            entry = input("\nWould you like to start the remaining round(s) now ? (Y or N):").lower()
            match entry:
                case 'y':
                    self.generate_remaining_rounds(self.tournament_object)
                case 'n':
                    self.go_to_tournament_menu_controller()
                case _:
                    print("Please enter Y (for Yes) or N (for No)")

    def generate_remaining_rounds(self, tournament_object):
        self.tournament_object = tournament_object
        self.sorted_players = []
        round_instances = []

        # empty line down
        print()

        # get instances of rounds already played
        for round_id in self.tournament_object.round_ids:
            round_serialized = self.rounds_table.get(doc_id=round_id)
            round_unserialized = self.round_model.unserialized(round_serialized)
            round_instances.append(round_unserialized)
            StartTournament.ROUNDS_PLAYED.append(round_id)

        # get matches already played
        for round_instance in round_instances:
            for match in round_instance.list_of_played_matches:
                player_1 = match[0][0]
                player_2 = match[1][0]
                StartTournament.MATCHES_PLAYED.append({player_1, player_2})
        round_model.match_model.Match.MATCH_NUMBER = len(StartTournament.MATCHES_PLAYED) + 1

        # run remaining rounds
        for i in range(int(self.tournament_object.number_of_rounds - len(self.tournament_object.round_ids))):
            self.sorted_players.clear()
            self.sorted_players = self.start_tournament.sort_players_other_rounds(self.tournament_object)
            self.tournament_object.round_ids.append(self.round_model.run(self.tournament_object,
                                                                         self.sorted_players))
            self.start_tournament.save_tournament_statement(self.tournament_object)

            # prompt to postpone if not last round
            if len(self.tournament_object.round_ids) < int(self.tournament_object.number_of_rounds):
                self.start_tournament.prompt_to_postpone_tournament()

        # when all rounds played, get instances of all rounds in tournament
        round_instances.clear()
        for round_id in StartTournament.ROUNDS_PLAYED:
            round_serialized = self.rounds_table.get(doc_id=round_id)
            round_unserialized = self.round_model.unserialized(round_serialized)
            round_instances.append(round_unserialized)

        # display tournament rounds and matches then prompt to return to menu
        self.end_tournament_view.end_tournament_header()
        self.end_tournament_view(round_instances)
        self.go_to_tournament_menu_controller()

    def prompt_for_tournaments_in_progress(self):
        self.resume_tournament_view()
        in_progress = [tournament for tournament in self.tournaments_table
                       if 0 < len(tournament['round_ids']) < tournament['number_of_rounds']]
        if not in_progress:
            print('\nThere are no tournaments in progress.')
            time.sleep(2)
            self.go_to_tournament_menu_controller()
        unserialized_in_progress = [self.tournament_model.unserialized(tournament) for tournament in in_progress]
        self.display_tournament.in_progress(unserialized_in_progress)

        while True:
            entry = input("Enter the Id of the tournament to continue: ")
            if not entry.isdigit():
                print("Please enter a valid tournament id.")
                continue
            selected_tournament = self.tournaments_table.get(doc_id=int(entry))
            if not selected_tournament:
                print("The id you entered is not in the list. Please enter a valid tournament id.")
                continue
            unserialized_selected = self.tournament_model.unserialized(selected_tournament)
            return unserialized_selected


class TournamentReport(MainTournamentController):
    """Display Players list alphabetically and by rating"""

    def __init__(self):
        super().__init__()
        self.make_menu = main_controller.menu_controller.MakeMenu()
        self.display_tournament = tournament_view.DisplayTournament()
        self.tournament_report_view = tournament_view.TournamentReportView()
        self.display_player = player_view.DisplayPlayer()
        self.player_report_view = player_view.PlayerReportView()
        self.round_view = tournament_view.RoundView()
        self.end_tournament_view = tournament_view.TournamentResultsView()

    def __call__(self):
        self.clear()
        self.tournament_report_view()
        self.prompt_for_report_menu(self.prompt_for_tournament())

    def prompt_for_tournament(self):
        tournaments = [tournament for tournament in self.tournaments_table]
        unserialized_tournament = [self.tournament_model.unserialized(tournament)
                                   for tournament in tournaments]

        if not tournaments:
            print('\nThere are no tournaments created.')
            time.sleep(2)
            self.go_to_tournament_menu_controller()
        self.display_tournament.default(unserialized_tournament)

        while True:
            entry = input("Enter the Id of the tournament to display the report: ")
            if not entry.isdigit():
                print("Please enter a valid tournament id.")
                continue
            selected_tournament = self.tournaments_table.get(doc_id=int(entry))
            if not selected_tournament:
                print("The id you entered is not in the list. Please enter a valid tournament id.")
                continue
            unserialized_selected = self.tournament_model.unserialized(selected_tournament)
            return unserialized_selected

    def prompt_for_report_menu(self, tournament_object):
        while True:
            entry = self.make_menu(self.make_menu.tournaments_report_menu)
            match entry:
                case "1":
                    self.tournament_players(tournament_object)
                case "2":
                    self.tournament_rounds(tournament_object)
                case "3":
                    self.go_to_tournament_menu_controller()

    def tournament_players(self, tournament_object):
        tournament_players = []

        if not tournament_object.player_ids:
            print('\nThere are no players in this tournament.')
            time.sleep(2)
            self.prompt_for_report_menu(tournament_object)

        for player_id in tournament_object.player_ids:
            player_serialized = self.players_table.get(doc_id=player_id)
            player_unserialized = self.player_model.unserialized(player_serialized)
            tournament_players.append(player_unserialized)

        while True:
            entry = self.make_menu(self.make_menu.tournament_players_report_menu)
            match entry:
                case "1":
                    self.player_report_view.display_title_alphabetically()
                    tournament_players.sort(key=attrgetter('first_name'))
                    self.display_player.full_table(tournament_players)
                case "2":
                    self.player_report_view.display_title_by_rating()
                    tournament_players.sort(key=attrgetter('rating'), reverse=True)
                    self.display_player.full_table(tournament_players)
                case "3":
                    self.prompt_for_report_menu(tournament_object)

    def tournament_rounds(self, tournament_object):
        tournament_rounds = []

        if not tournament_object.round_ids:
            print('\nThere are no rounds played in this tournament.')
            time.sleep(2)
            self.prompt_for_report_menu(tournament_object)

        for round_id in tournament_object.round_ids:
            round_serialized = self.rounds_table.get(doc_id=round_id)
            round_unserialized = self.round_model.unserialized(round_serialized)
            tournament_rounds.append(round_unserialized)

        while True:
            entry = self.make_menu(self.make_menu.tournament_rounds_report_menu)
            match entry:
                case "1":
                    self.round_view.display_rounds(tournament_rounds)
                case "2":
                    self.end_tournament_view.round_report_header()
                    self.end_tournament_view(tournament_rounds)
                case "3":
                    self.prompt_for_report_menu(tournament_object)
