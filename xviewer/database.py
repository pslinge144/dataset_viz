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
    """
    The created database will have columns for:
    ImageName - Thumbnail - Class Map - Class Pixel Count
    """
    def __init__(self):
        self.db = sqlite.connect(DB_NAME)
        self.cursor = self.db.cursor()

    def add_filename(self, filename):
        sql = "INSERT INTO cubes (filename) VALUES (?)"
        query_params = (filename)

        self.perform_insert(sql, query_params)

    def get_all_files(self):
        sql = "SELECT filename FROM cubes"
        params = []

        return perform_select(sql, params)

    def perform_inset(self, sql, params):
        self.cursor.execute(sql, params)
        self.db.commit()

    def perform_select(self, sql, params):
        self.cursor.execute(sql, params)
        results = self.cursor.fetchall()

        return result

    def __del__(self):
        self.db.close()
