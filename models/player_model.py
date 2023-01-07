import time
from dbase.database import Database

db = Database()
players_table = db.players_table


class Player:

    def __init__(self,
                 first_name=None,
                 last_name=None,
                 date_of_birth=None,
                 gender=None,
                 rating=None,
                 tournament_score=0,
                 player_id=0
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.rating = rating
        self.tournament_score = tournament_score
        self.player_id = player_id
        self.serialized_player = None

    def serialized(self):
        player_data = {'first_name': self.first_name,
                       'last_name': self.last_name,
                       'date_of_birth': self.date_of_birth,
                       'gender': self.gender,
                       'rating': self.rating,
                       'tournament_score': self.tournament_score,
                       'player_id': self.player_id}
        return player_data

    def unserialized(self, serialized_player):
        self.serialized_player = serialized_player
        first_name = self.serialized_player['first_name']
        last_name = self.serialized_player['last_name']
        date_of_birth = self.serialized_player['date_of_birth']
        gender = self.serialized_player['gender']
        rating = self.serialized_player['rating']
        tournament_score = self.serialized_player['tournament_score']
        player_id = self.serialized_player['player_id']
        return Player(
                      first_name,
                      last_name,
                      date_of_birth,
                      gender,
                      rating,
                      tournament_score,
                      player_id
                     )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'{self.first_name} {self.last_name}, Rating : {self.rating}'

    @staticmethod
    def add_to_database(player_values):
        player = Player(player_values[0],
                        player_values[1],
                        player_values[2],
                        player_values[3],
                        player_values[4]
                        )
        player_id = players_table.insert(player.serialized())
        players_table.update({'player_id': player_id}, doc_ids=[player_id])
        time.sleep(1)
