import sqlite3

with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTENGER primary key, nombre VARCHAR(50));
        """
    )
