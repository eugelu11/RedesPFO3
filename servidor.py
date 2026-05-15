import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9999))

server.listen(1)
print("Servidor esperando conexión...")

conn, address = server.accept()
print(f"Cliente conectado desde {address}")

data = conn.recv(1024)
print(f"Recibido: {data.decode()}")

conn.send("Hola desde el servidor!".encode())

conn.close()
server.close()