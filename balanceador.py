import socket
import threading

servidores = [
    ("localhost", 9999),
    ("localhost", 9998)
]

indice = 0
lock = threading.Lock()

def obtener_servidor():
    global indice
    with lock:
        servidor = servidores[indice]
        indice = (indice + 1) % len(servidores)
        return servidor

def manejar_cliente(cliente_conn):
    servidor_addr = obtener_servidor()
    print(f"Redirigiendo a {servidor_addr}")

    servidor_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_conn.connect(servidor_addr)

    data = cliente_conn.recv(1024)
    servidor_conn.send(data)

    respuesta = servidor_conn.recv(1024)
    cliente_conn.send(respuesta)

    cliente_conn.close()
    servidor_conn.close()

balanceador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
balanceador.bind(("localhost", 8888))
balanceador.listen(5)
print("Balanceador escuchando en puerto 8888...")

while True:
    conn, address = balanceador.accept()
    t = threading.Thread(target=manejar_cliente, args=(conn,))
    t.start()