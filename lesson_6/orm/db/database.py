import sqlite3


class DataBase:
    def __init__(self, db):
        self.__connect = sqlite3.connect(db)

    def create(self):

