import psycopg2
import psycopg2.extras
from modules.config import Config


class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(Config.DATABASE_URL)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def execute_query_get_dict(self, query_str, kwargs=None):
        try:
            cursor = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
            cursor.execute(query_str, kwargs)
            return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def execute_query(self, query_str, kwargs=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query_str, kwargs)
            return cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def execute_update(self, query_str, kwargs=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query_str, kwargs)
            self.connection.commit()
            cursor.close()
            return
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)


if __name__ == '__main__':
    d = Database().execute_query("select * from version()")
    print(d)
