import sqlite3


class Database:
    def __init__(self):
        self.db = "data.db"

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
