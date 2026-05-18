import socket
import sqlite3

def verificar_login(usuario, contraseña):
    conn_db=sqlite3.connect("miBBDD.db")
    cursor=conn_db.cursor()
    cursor.execute("SELECT*FROM usuarios WHERE usuario=? AND contraseña=?", (usuario, contraseña)
    )
    resultado=cursor.fetchone()
    conn_db.close()
    return resultado is not None


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))

server.listen(5)
print("Servidor esperando conexión...")

while True:
    conn, address = server.accept()
    print(f"Cliente conectado desde {address}")

    data = conn.recv(1024).decode()
    partes = data.split(":")
    comando = partes[0]

    if comando == "login":
        usuario = partes[1]
        contraseña= partes[2]
        if verificar_login(usuario,contraseña):
            conn.send("Login exitoso".encode())
        else: conn.send("Usuario o contraseña incorrectos".encode())
    elif comando == "registro":
        elif comando == "registro":
    usuario = partes[1]
    clave = partes[2]
    if registrar_usuario(usuario, clave):
        conn.send("Usuario registrado exitosamente".encode())
    elif
        conn.send("El usuario ya existe".encode())
    else:
        conn.send("Comando desconocido".encode())

    conn.close()