import socket
import sqlite3
from concurrent.futures import ThreadPoolExecutor

def verificar_login(usuario, contraseña):
    conn_db=sqlite3.connect("miBBDD.db")
    cursor=conn_db.cursor()
    cursor.execute("SELECT*FROM usuarios WHERE usuario=? AND contraseña=?", (usuario, contraseña)
    )
    resultado=cursor.fetchone()
    conn_db.close()
    return resultado is not None

def registrar_usuario(usuario, contraseña):
    conn_db = sqlite3.connect("miBBDD.db")
    cursor = conn_db.cursor()
    try:
        cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)", (usuario, contraseña))
        conn_db.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn_db.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))

server.listen(5)
print("Servidor esperando conexión...")

def manejar_cliente(conn):
    data = conn.recv(1024).decode().strip()
    partes = data.split(":")
    comando = partes[0]

    if comando == "login":
        usuario = partes[1]
        contraseña= partes[2]
        if verificar_login(usuario,contraseña):
            conn.send("Login exitoso".encode())
        else: conn.send("Usuario o contraseña incorrectos".encode())
    elif comando == "registro":
        usuario = partes[1]
        contraseña = partes[2]
        if registrar_usuario(usuario, contraseña):
            conn.send("Usuario registrado exitosamente".encode())
        else:
            conn.send("El usuario ya existe".encode())
    elif comando == "tareas":
        conn.send("Bienvenida Euge- estas son tus tareas".encode())

    else:
        conn.send("Comando desconocido".encode())

    conn.close()

with ThreadPoolExecutor(max_workers=5) as executor:
    while True:
        conn, address = server.accept()
        print(f"Cliente conectado desde {address}")
        executor.submit(manejar_cliente, conn)
    