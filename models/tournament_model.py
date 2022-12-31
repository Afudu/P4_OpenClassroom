from dbase.database import Database

db = Database()
tournaments_table = db.tournaments_table


class Tournament:
    """Creates an instance of a tournament"""

    def __init__(self, name=None,
                 venue=None,
                 start_date=None,
                 number_of_rounds=4,
                 time_control=None,
                 description=None,
                 player_ids=None,
                 round_ids=None,
                 tournament_id=None,
                 ):
        if round_ids is None:
            round_ids = []
        if player_ids is None:
            player_ids = []
        self.name = name
        self.venue = venue
        self.start_date = start_date
        self.number_of_rounds = number_of_rounds
        self.time_control = time_control
        self.description = description
        self.player_ids = player_ids
        self.round_ids = round_ids
        self.tournament_id = tournament_id

    def __repr__(self):
        return f"{self.name} - {self.venue}\n\n {self.round_ids}\n"

    def serialized(self):
        tournament_data = {'tournament_name': self.name,
                           'venue': self.venue,
                           'start_date': self.start_date,
                           'number_of_rounds': self.number_of_rounds,
                           'time_control': self.time_control,
                           'description': self.description,
                           'player_ids': self.player_ids,
                           'round_ids': self.round_ids,
                           'tournament_id': self.tournament_id
                           }

        return tournament_data

    @staticmethod
    def unserialized(serialized_tournament):
        name = serialized_tournament['tournament_name']
        venue = serialized_tournament['venue']
        start_date = serialized_tournament['start_date']
        number_of_rounds = serialized_tournament['number_of_rounds']
        time_control = serialized_tournament['time_control']
        description = serialized_tournament['description']
        player_ids = serialized_tournament['player_ids']
        round_ids = serialized_tournament['round_ids']
        tournament_id = serialized_tournament['tournament_id']

        return Tournament(name,
                          venue,
                          start_date,
                          number_of_rounds,
                          time_control,
                          description,
                          player_ids,
                          round_ids,
                          tournament_id
                          )

    @staticmethod
    def add_to_database(tournament_values):
        tournament = Tournament(tournament_values[0],
                                tournament_values[1],
                                tournament_values[2],
                                tournament_values[3],
                                tournament_values[4],
                                tournament_values[5]
                                )
        tournament_id = tournaments_table.insert(tournament.serialized())
        tournaments_table.update(
            {"tournament_id": tournament_id},
            doc_ids=[tournament_id]
                                )
        return tournament_id

    @staticmethod
    def update_players(player_list, tournament_id):

        tournaments_table.update({"player_ids": player_list}, doc_ids=[tournament_id])
