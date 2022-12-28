from tinydb import TinyDB, Query


class Database:
    # db = TinyDB('../dbase/db.json', indent=4)
    # db = TinyDB('db.json', indent=4)
    db = TinyDB('dbase/db.json', indent=4)
    Tournament_Query = Query()
    tournaments_table = db.table('tournaments_table')
    players_table = db.table('players_table')
    rounds_table = db.table('rounds_table')
