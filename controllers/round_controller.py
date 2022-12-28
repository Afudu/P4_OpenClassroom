from controllers import main_controller
from models import round_model
from views import tournament_view
from models import match_model


class AddRound:
    """Adds a round instance"""

    def __init__(self):
        self.round_name = None
        self.end_time = None
        self.start_time = None
        self.list_of_played_matches = []
        self.match_instances = []
        self.round_view = tournament_view.RoundView()
        self.round_model = round_model.Round()
        self.main_menu_controller = main_controller.MainMenuController()

    def run(self, tournament_object, pairings):

        self.round_name = "Round " + str(len(tournament_object.round_ids) + 1)

        for pairing in pairings:
            match_instance = match_model.Match(pairing[0], pairing[1])
            match_model.Match.MATCH_NUMBER += 1
            self.match_instances.append(match_instance)

        self.round_view.display_round_matches(self.round_name,
                                              self.match_instances)

        self.start_time, self.end_time = self.round_view.display_round_time()

        for match in self.match_instances:
            valid_score_player_1 = False
            while not valid_score_player_1:
                try:
                    score_player_1 = float(input(f"Enter the score"
                                                 f" of {match.player_1}:"))
                    if not (score_player_1 == 0 or score_player_1 == 0.5
                            or score_player_1 == 1):
                        raise ValueError
                except ValueError:
                    print("Invalid score. Please enter 0 for lost, "
                          "0.5 for tie, or 1 for win")
                else:
                    valid_score_player_1 = True
                    match.score_player_1 = float(score_player_1)
                    match.player_1.tournament_score += float(score_player_1)
                    print(f"Running score of {match.player_1} = "
                          f"{match.player_1.tournament_score}")

            valid_score_player_2 = False
            while not valid_score_player_2:
                try:
                    score_player_2 = float(input(f"Enter the score of "
                                                 f"{match.player_2} :"))
                    if not (score_player_2 == 0 or score_player_2 == 0.5
                            or score_player_2 == 1):
                        raise ValueError
                except ValueError:
                    print("Invalid score. Please enter 0 for lost, "
                          "0.5 for tie, or 1 for win")
                else:
                    valid_score_player_2 = True
                    match.score_player_2 = float(score_player_2)
                    match.player_2.tournament_score += float(score_player_2)
                    print(f"Running score of {match.player_2} = "
                          f"{match.player_2.tournament_score}")

            self.list_of_played_matches.append(([match.player_1.player_id,
                                                 match.score_player_1],
                                                [match.player_2.player_id,
                                                 match.score_player_2]
                                                ))

        return round_model.Round(self.round_name,
                                 self.start_time,
                                 self.end_time,
                                 self.list_of_played_matches
                                 )
