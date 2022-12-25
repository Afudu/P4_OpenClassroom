# from controllers import player_controller


class Match:
    """
     Each match consists of a pair of players with a results field for each player.
     The winner receives 1 point, the loser 0 points. If a game ends in a tie, each player gets 1/2 a point.
     A single match should be stored as a tuple containing two lists, with each one holding two elements:
     a reference to a player instance, and a score.
     Multiple matches should be stored as a list on the round instance.
    """

    MATCH_NUMBER = 1

    def __init__(self, player_1, player_2, score_player_1=0, score_player_2=0):
        self.match_name = "Match " + str(Match.MATCH_NUMBER)
        self.player_1 = player_1
        self.player_2 = player_2
        self.score_player_1 = score_player_1
        self.score_player_2 = score_player_2

    def __str__(self):
        return f"{self.match_name} : {self.player_1} --Vs-- {self.player_2}."
