import psycopg2


class Config:
    connection = None

    def __init__(self):
        self.hostName = "127.0.0.1"
        self.userName = "postgres"
        self.password = "root"
        self.databaseName = "db_escape_game"

    def connect(self):
        if self.connection is None:
            self.connection = psycopg2.connect(host=self.hostName,
                                               user=self.userName,
                                               password=self.password,
                                               dbname=self.databaseName)
        else:
            return self.connection

    def query(self, statement, one=None):
        cur = self.connection.cursor()
        cur.execute(statement)
        if one:
            data = cur.fetchone()
        else:
            data = cur.fetchall()
        return data

    def prepare(self, statement, params, one=None):
        cur = self.connection.cursor()
        cur.execute(statement, params)
        if one:
            data = cur.fetchone()
        else:
            data = cur.fetchall()
        return data
