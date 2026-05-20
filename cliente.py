import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 8888))

accion = input("¿Qué querés hacer? (login/registro): ")
usuario= input("Usuario: ")
contraseña=input("Contraseña: ")
client.send(f"{accion}:{usuario}:{contraseña}".encode())

respuesta = client.recv(1024).decode()
print(f"Respuesta: {respuesta}")

if respuesta == "Login exitoso":
    accion2 = input("¿Qué querés hacer? (tareas/salir): ")
    if accion2 == "tareas":
        client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client2.connect(("localhost", 8888))
        client2.send(f"tareas:{usuario}".encode())
        print(client2.recv(1024).decode())
        client2.close()

client.close()