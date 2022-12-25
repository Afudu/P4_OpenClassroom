# from dataclasses import dataclass
# import time
from dbase.database import Database

db = Database()
tournaments_table = db.tournaments_table


# @dataclass
class Tournament:
    """Use to create an instance of a tournament"""

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
        tournament_data = {'tournament_name': self.name, 'venue': self.venue,
                           'start_date': self.start_date, 'number_of_rounds': self.number_of_rounds,
                           'time_control': self.time_control, 'description': self.description,
                           'player_ids': self.player_ids, 'round_ids': self.round_ids,
                           'tournament_id': self.tournament_id}

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
                                tournament_values[5],
                                tournament_values[6]
                                )
        tournament_id = tournaments_table.insert(tournament.serialized())
        tournaments_table.update({"tournament_id": tournament_id}, doc_ids=[tournament_id])

# db.insert({'type': 'apples', 'count': 8})
# tournaments_table.insert({'type': 'apples', 'count': 8})
# db.insert({'name': 'John', 'age': 22})
# print(db.all())
# print(db.search(Fruit.name == 'John'))
# print(db.get(Fruit.name == 'John').doc_id)
# print(db.get(doc_id=1))
# db.insert({'name': 'Johnny', 'age': 122})
# db.get(Tournament.type == 'apples')
# print(tournaments_table.get(doc_id=1))
# print(tournaments_table.search(Fruit.type == 'apples'))
# db.update({'value': 2}, doc_ids=[1, 2])
# tournaments_table.update({'value': 2}, doc_ids=[1])
# print(tournaments_table.insert({'name': 'Test', 'age': 32}))
# print(players_table.insert({'name': 'Test', 'age': 32}))
# t = Tournament()
# print(t)
# players_table.update({"name": 'Ali'}, Player.name == "Test")
# players_table.update({"name": 'Ali1'}, doc_ids=[1])
# p = players_table.get(Player.name == "Ali1")
# print(p.doc_id)
# print(players_table.get(doc_id=1))


# t = Tournament()
# values = ['Name', 'Venue', '13/08/2022', 4, 'Bullet', 'Description', []]
# tour = Tournament(values[0],
#                   values[1],
#                   values[2],
#                   values[3],
#                   values[4],
#                   values[5],
#                   values[6]
#                   )
# t.add_to_database(values)
# print(values[7])
# ts = tour.serialized()
# un = tour.unserialized(ts)
# print(ts)
# print(un)
# tournaments_table.remove(doc_ids=[1, 2])
# ts = tournaments_table.get(doc_id=1)
# print(ts)
# us = tour.unserialized(ts)
# print(us)
# chosen_tournament = tournaments_table.get(doc_id=1)
# tournament_object = t.unserialized(chosen_tournament)
# print(chosen_tournament)
# tdef = db.table('_default')
# tdef.remove(doc_ids=[1,2,3,4])
