import sqlite3


class Database:
    def __init__(self):
        self.db = "data.db"

    def perform_inset(self, sql, params):
        conn = sqlite3.connect(self.db)

    def perform_select(self, sql, params):
        conn = sqlite3.connect(self.db)

    def perform_query(self, sql, params):
        pass
