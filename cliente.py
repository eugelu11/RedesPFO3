import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 9999))

usuario= input("Usuario: ")
contraseña=input("Contraseña: ")
client.send(f"login:{usuario}:{contraseña}".encode())

response = client.recv(1024)
print(f"Respuesta: {response.decode()}")

client.close()