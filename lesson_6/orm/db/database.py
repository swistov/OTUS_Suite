import sqlite3


class DataBase:
    def __init__(self, db):
        self.__connect = sqlite3.connect(db)

    @staticmethod
    def __get_all_atrribute__(table):
        return [k for k in table.__class__.__dict__.keys() if not k.startswith('__')]

    def create_db(self, table):
        field_names = self.__get_all_atrribute__(table)
        print('SELECT %s FROM %s;' % (', '.join(field_names), table.__class__.__table_name__))
