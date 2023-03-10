from dbase.database import Database
from models import match_model
from views.tournament_view import RoundView
from controllers import main_controller
from controllers.match_controller import ValidateMatchScore, MatchScoreError


db = Database()
players_table = db.players_table


class Round:
    """Creates a round instance"""

    def __init__(self, name=None,
                 start_time=None,
                 end_time=None,
                 list_of_played_matches=None
                 ):
        if list_of_played_matches is None:
            list_of_played_matches = []
        self.name = name
        self.start_time = start_time
        self.end_time = end_time
        self.list_of_played_matches = list_of_played_matches
        self.match_instances = []
        self.match_instance = None
        self.round_view = RoundView()
        self.main_menu_controller = main_controller.MainMenuController()
        self.match_controller = ValidateMatchScore()

    def serialized(self):
        round_data = {'name': self.name,
                      'start_time': self.start_time,
                      'end_time': self.end_time,
                      'list_of_played_matches': self.list_of_played_matches
                      }
        return round_data

    @staticmethod
    def unserialized(serialized_round):
        name = serialized_round['name']
        start_time = serialized_round['start_time']
        end_time = serialized_round['end_time']
        list_of_played_matches = serialized_round['list_of_played_matches']
        return Round(name,
                     start_time,
                     end_time,
                     list_of_played_matches
                     )

    def __repr__(self):
        return f"{self.name} - Started: {self.start_time}. Ended: {self.end_time}."

    def run(self, tournament_object, sorted_players_list):
        self.match_instances = []
        self.list_of_played_matches = []
        self.name = "Round " + str(len(tournament_object.round_ids) + 1)

        while len(sorted_players_list) > 0:
            match_instance = match_model.Match(sorted_players_list[0], sorted_players_list[1])
            match_model.Match.MATCH_NUMBER += 1
            self.match_instances.append(match_instance)
            del sorted_players_list[0:2]

        self.round_view.display_round_matches(self.name, self.match_instances)

        self.start_time, self.end_time = self.round_view.display_round_time()

        for match in self.match_instances:

            valid_score_player_1 = False
            while not valid_score_player_1:
                try:
                    score_player_1 = self.match_controller.prompt_for_score(match.player_1)
                    self.match_controller.validate_player_score(score_player_1)
                except MatchScoreError:
                    print(MatchScoreError().messages[0])
                else:
                    valid_score_player_1 = True
                    match.score_player_1 = score_player_1
                    match.player_1.tournament_score += score_player_1

                    players_table.update({"tournament_score": match.player_1.tournament_score},
                                         doc_ids=[int(match.player_1.player_id)]
                                         )

            valid_score_player_2 = False
            while not valid_score_player_2:
                try:
                    score_player_2 = self.match_controller.prompt_for_score(match.player_2)
                    self.match_controller.validate_opponent_score(match.score_player_1, score_player_2)

                except MatchScoreError:
                    print(MatchScoreError().messages[1])
                else:
                    valid_score_player_2 = True
                    match.score_player_2 = score_player_2
                    match.player_2.tournament_score += score_player_2

                    players_table.update({"tournament_score": match.player_2.tournament_score},
                                         doc_ids=[int(match.player_2.player_id)]
                                         )

            match_played = ([match.player_1.player_id, match.score_player_1],
                            [match.player_2.player_id, match.score_player_2]
                            )
            self.list_of_played_matches.append(match_played)

        return Round(self.name,
                     self.start_time,
                     self.end_time,
                     self.list_of_played_matches
                     )
