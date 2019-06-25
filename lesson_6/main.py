from orm.table import BaseTable
from orm.field import IntegerField, TextField, BooleanField
from orm.db import DataBase


class User(BaseTable):
    __table_name__ = 'users'

    id = IntegerField(primary_key=True, auto_increment=True)
    name = TextField(not_null=True)
    active = BooleanField(not_null=True, default_value=1)


class Post(BaseTable):
    __table_name__ = 'posts'

    id = IntegerField(primary_key=True)
    name = TextField(not_null=True)
    id_user = IntegerField(foreign_key=User.id)


if __name__ == '__main__':
    db = DataBase('my.db')

    """ Create DB"""
    db.create(User)
