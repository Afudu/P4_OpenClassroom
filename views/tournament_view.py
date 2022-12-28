from views import main_view
import time
from controllers import player_controller


class TournamentMenuView(main_view.MainMenuView):
    """Creates the Tournament main menu view"""

    def __init__(self):
        super().__init__()

    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.app_name)
        self.display_filled_line()
        self.display_text_surrounded(self.menu_titles[2])
        self.display_filled_line()


class DisplayTournament(main_view.MainMenuView):
    """Display all the tournaments in the database"""

    def __init__(self):
        super().__init__()
        self.table_view = main_view.TableView()
        self.line = None
        self.lines = []

    def default(self, tournament_list):
        for tournament in tournament_list:
            self.line = tournament.tournament_id, \
                        tournament.name, \
                        tournament.venue
            self.lines.append(self.line)
        self.table_view(self.lines, self.tournament_headers_by_id)
        self.lines.clear()

    def in_progress(self, tournament_list):
        for tournament in tournament_list:
            self.line = tournament.tournament_id, \
                        tournament.name, \
                        tournament.venue, \
                        tournament.round_ids
            self.lines.append(self.line)
        self.table_view(self.lines, self.tournaments_in_progress_headers)
        self.lines.clear()


class AddTournamentView(main_view.MainMenuView):
    """Creates the Add Tournament menu headers"""

    def __init__(self):
        super().__init__()

    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.app_name)
        self.display_filled_line()
        self.display_text_surrounded(self.menu_titles[2])
        self.display_filled_line()

    def add_player_view(self):
        self.display_empty_line()
        self.display_text_surrounded(self.player_references[1])

    def validate_tournament_view(self):
        self.display_empty_line()
        self.display_text_surrounded(self.tournament_references[0])


class StartTournamentView(main_view.MainMenuView):
    """Creates the Start Tournament menu headers"""

    def __init__(self):
        super().__init__()

    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.menu_options[4])
        self.display_filled_line()
        self.display_empty_line()
        self.display_text_surrounded(self.tournament_references[1])


class ResumeTournamentView(main_view.MainMenuView):
    """View handling resuming a tournament in progress"""

    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.menu_options[5])
        self.display_filled_line()
        self.display_empty_line()
        self.display_text_surrounded(self.tournament_references[2])


class RoundView(main_view.MainMenuView):
    """Displays the Tournament rounds and matches"""

    def __init__(self):
        super().__init__()
        self.end_time = None
        self.start_time = None
        self.table_view = main_view.TableView()
        self.line = None
        self.lines = []

    def display_round_matches(self, round_name, match_instances):
        self.display_empty_line()
        self.display_text_surrounded(round_name)

        for match in match_instances:
            self.line = match.match_name, \
                        str(match.player_1) + " Vs " + str(match.player_2)
            self.lines.append(self.line)
        self.table_view(self.lines, [])
        self.lines.clear()

    def display_round_time(self):
        print()
        input("Press Enter key to start the round.")
        print()
        self.start_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f"Round Start Date: {self.start_time}")
        print()
        input("Press Enter key when the round ended.")
        print()
        self.end_time = time.strftime(format("%d/%m/%Y - %Hh%Mm%Ss"))
        print(f"Round End Date: {self.end_time}")
        print()
        return self.start_time, self.end_time

    def display_rounds(self, round_instances):

        print()
        self.display_text_surrounded(self.tournament_references[4])
        print()

        for round_instance in round_instances:
            print(round_instance)
            print()


class TournamentResultsView(main_view.MainMenuView):
    """Displays the final score at the end of the tournament"""
    def __call__(self, round_objects=None):

        self.players_table = player_controller.player_model.players_table

        for round_object in round_objects:
            print(round_object)
            print()
            for match in round_object.list_of_played_matches:
                player_1 = self.players_table.get(doc_id=match[0][0])
                score_player_1 = match[0][1]
                player_2 = self.players_table.get(doc_id=match[1][0])
                score_player_2 = match[1][1]

                print(f"{player_1['first_name']} {player_1['last_name']} Vs "
                      f"{player_2['first_name']} {player_2['last_name']}\n"
                      f"Score : {score_player_1} - {score_player_2}\n")

        input("Press Enter key to go to Tournament menu")

    def end_tournament_header(self):
        print()
        self.display_filled_line()
        self.display_text_surrounded('Enf of Tournament')
        self.display_text_surrounded('Results')
        self.display_filled_line()
        print()

    def round_report_header(self):
        print()
        self.display_text_surrounded('Matches Played per Round')
        print()


class TournamentReportView(main_view.MainMenuView):
    """Display all the Tournament report headers """

    def __call__(self):
        self.display_filled_line()
        self.display_text_surrounded(self.menu_options[6])
        self.display_filled_line()
        self.display_empty_line()
        self.display_text_surrounded(self.tournament_references[3])

    def display_title_alphabetically(self):
        self.display_text_surrounded(self.player_references[3])

    def display_title_rating(self):
        self.display_text_surrounded(self.player_references[4])
