from tinydb import TinyDB, Query


class Database:
    # db = TinyDB('../dbase/db.json', indent=4)
    # db = TinyDB('db.json', indent=4)
    db = TinyDB('dbase/db.json', indent=4)
    Tournament_Query = Query()
    tournaments_table = db.table('tournaments_table')
    players_table = db.table('players_table')
    rounds_table = db.table('rounds_table')


# db = Database()
# players_table = db.players_table
# pt.remove(doc_ids=[5, 6, 7, 8, 9])
# for player in pt:
# print(f"{player.doc_id} - {player['last_name']} {player['first_name']} - Rating : {player['rating']}")
# tst = [f"{player.doc_id}, {player['last_name']}, {player['first_name']}, {player['rating']}"]
# print(pt.get(doc_id=1))
