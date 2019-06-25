from orm.table import BaseTable
from orm.db import DataBase


class User(BaseTable):
    __table_name__ = 'users'

    id = ('int', 'required')
    username = ('char(256)', 'not_required')


if __name__ == '__main__':
    db = DataBase('my.db')

    """ Create DB"""
    user = User()
    user.id = 1
    user.username = 'test'
    # db.create_db(user)
    User.create(user)
