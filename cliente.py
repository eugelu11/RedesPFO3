import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 8888))

accion = input("¿Qué querés hacer? (login/registro): ")
usuario= input("Usuario: ")
contraseña=input("Contraseña: ")
client.send(f"{accion}:{usuario}:{contraseña}".encode())

response = client.recv(1024)
print(f"Respuesta: {response.decode()}")

client.close()