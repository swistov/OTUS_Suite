class BaseTable:
    __table_name__ = None

    def __init__(self):
        pass

    def create(self, *args, **kwargs):
        print(self.__dict__)
