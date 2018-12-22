import sqlite3
from database import add_filename


def create_database():
    database = sqlite.connect("data.db")
    cursor = database.cursor()

    create_cubes_sql = "CREATE TABLE cubes (filename TEXT)"
    cursor.execute(create_cubes_sql)

    database.commit()
    database.close()
