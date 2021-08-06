import sqlite3
import functools


# exception decorator
def with_exception(func):
    @functools.wraps(func)
    def exception_wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ERROR] {type(e).__name__}, {e}")
    return exception_wrapper


class Factory:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Factory, cls).__new__(cls)
        return cls.instance

    @staticmethod
    def string_factory(cursor, row):
        if len(row) == 1:
            return str(row).replace("('", "").replace("',)", "")
        else:
            print(f"[WARNING] row contains more than one element")
            return str(row).replace("(", "").replace(")", "")

    @staticmethod
    def dict_factory(cursor, row):
        d = dict()
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


class sqlite():
    @with_exception
    def __init__(self, dataBase):
        self.__connection = sqlite3.connect(dataBase)
        self.__cursor = self.__connection.cursor()

    @with_exception
    def __del__(self):
        self.close()

    @with_exception
    def close(self, commit=False):
        if commit:
            self.commit()
        self.__connection.close()

    @with_exception
    def commit(self):
        self.__connection.commit()

    @with_exception
    def insert(self, table, into, values):
        self.__cursor.execute(f"""
            INSERT INTO {table}
            ({into}) VALUES ({values})
        """)

    @with_exception
    def execute(self, expression):
        self.__cursor.execute(expression)

    @with_exception
    def select_raw(self, columns_name, table_name, filter=None):
        if filter is not None:
            filter = "WHERE" + " " + filter
        self.__cursor.execute(f"""
            SELECT {columns_name}
            FROM {table_name}
            {filter}
        """)
        return self.__cursor.fetchall()

    @with_exception
    def select(self, columns_name, table_name, filter=None, factory=None):
        self.__cursor.row_factory = factory
        tuple_raw = self.select_raw(columns_name, table_name, filter)
        self.__cursor.row_factory = None
        return tuple_raw

    @with_exception
    def description(self):
        return [description[0] for description in self.__cursor.description]
