import sqlite3
from database import add_filename


def create_database():
    db = sqlite.connect("data.db")
    cursor = db.cursor()

    create_cubes_sql = "CREATE TABLE cubes (filename TEXT)"
    cursor.execute(create_cubes_sql)

    db.commit()
    db.close()
