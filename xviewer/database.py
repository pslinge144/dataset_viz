import sqlite3


DB_NAME = "data.db"


def create_database():
    db = sqlite.connect(DB_NAME)
    cursor = db.cursor()

    create_cubes_sql = "CREATE TABLE cubes (filename TEXT)"
    cursor.execute(create_cubes_sql)

    db.commit()
    db.close()


class Database:
    def __init__(self):
        self.db = DB_NAME

    def add_filename(self, filename):
        sql = "INSERT INTO cubes (filename) VALUES (?)"
        query_params = (filename)

        self.perform_insert(sql, query_params)

    def get_all_files(self):
        sql = "SELECT filename FROM cubes"
        params = []

        return perform_select(sql, params)

    def perform_inset(self, sql, params):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute(sql, params)
        conn.commit()
        conn.close()

    def perform_select(self, sql, params):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute(sql, params)
        results = cursor.fetchall()
        conn.close()

        return result
