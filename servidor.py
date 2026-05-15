import socket

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
        clave = partes[2]
        conn.send(f"Procesando login de {usuario}".encode())
    elif comando == "registro":
        usuario = partes[1]
        conn.send(f"Registrando a {usuario}".encode())
    else:
        conn.send("Comando desconocido".encode())

    conn.close()