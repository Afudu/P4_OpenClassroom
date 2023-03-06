from tinydb import TinyDB


class Database:
    db = TinyDB('dbase/db.json', indent=4)
    # Tournament_Query = Query()
    tournaments_table = db.table('tournaments_table')
    players_table = db.table('players_table')
    rounds_table = db.table('rounds_table')
