import sqlite3

conn = sqlite3.connect("miBBDD.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT NOT NULL UNIQUE,
        contraseña TEXT NOT NULL
    )
""")

cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES ('juan', '1234')")

conn.commit()
conn.close()
print("Base de datos creada con usuario: juan / 1234")