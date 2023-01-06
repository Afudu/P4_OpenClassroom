class MatchLostError(Exception):
    """Exception raised when the match is lost and the score input is not 0"""
    pass


class MatchWonError(Exception):
    """Exception raised when the match is won and the score input is not 1"""
    pass


class MatchTiedError(Exception):
    """Exception raised when the match is a tie and the score input is not 0.5"""
    pass
