class MatchScoreController:
    """Controller handling the validation of match scores"""

    @staticmethod
    def prompt_for_score(player):
        score_player = float(input(f"Enter the score of {player}:"))
        return score_player

    @staticmethod
    def validate_player_score(score):
        if not (score == 0 or score == 0.5 or score == 1):
            raise MatchScoreError

    @staticmethod
    def validate_opponent_score(score_player, score_opponent):
        if (score_player == 0 and score_opponent != 1) | (score_player == 1 and score_opponent != 0) \
                | (score_player == 0.5 and score_opponent != 0.5):
            raise MatchScoreError


class MatchScoreError(Exception):
    """Exception raised when there is player's score error"""

    def __init__(self):
        self.messages = ["Invalid score. Please enter 0 for a lost, 0.5 for a tie, or 1 for a win",
                         "Invalid opponent score. Please check again the score."]
