import sqlite3


database = sqlite.connect("data.db")
cursor = database.cursor()

create_cubes_sql = "CREATE TABLE cubes (filename TEXT)"
cursor.execute(create_cubes_sql)

database.commit()
database.close()
