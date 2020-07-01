import psycopg2

from modules.config import Config


class Database:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(Config.DATABASE_URL)
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    def execute_query(self, query_str):
        try:
            self.cursor.execute(query_str)
            return self.cursor.fetchall()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)


if __name__ == '__main__':
    d = Database().execute_query("select * from version()")
    print(d)
