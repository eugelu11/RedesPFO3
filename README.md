# PFO 3-Eugenia Lucchelli

## Descripción
Este proyecto transforma el sistema de gestión de usuarios de PFO 2 en una 
arquitectura distribuida usando sockets TCP. Incluye:

- Comunicación cliente-servidor mediante sockets raw (sin HTTP)
- Balanceador de carga con algoritmo Round Robin
- Dos servidores worker con pool de hilos (ThreadPoolExecutor)
- Base de datos SQLite compartida entre workers
- Diagrama del sistema con RabbitMQ, PostgreSQL y S3

## Estructura del proyecto
/proyecto
│── servidor.py       (worker 1 - puerto 9999)
│── servidor2.py      (worker 2 - puerto 9998)
│── balanceador.py    (load balancer - puerto 8888)
│── cliente.py        (cliente de consola)
│── crear_db.py       (inicializa la base de datos)
│── miBBDD.db         (se crea con crear_db.py)
│── README.md


## Cómo ejecutar

1. `py crear_db.py` (solo la primera vez)
2. Terminal 1: `py servidor.py` (inicia el 1er worker)
3. Terminal 2: `py servidor2.py` (inicia el 2ndo worker)
4. Terminal 3: `py balanceador.py` (inicia el balanceador)
5. Terminal 4: `py cliente.py` (ejecuta el cliente)

## Uso del cliente
El programa va a preguntar:
¿Qué querés hacer? (login/registro):
Usuario:
Contraseña:


## Diagrama:

<img width="633" height="601" alt="DiagramaPFO3 drawio" src="https://github.com/user-attachments/assets/afb5047f-2dc4-4187-8467-b0c87a6339d5" />



## Explicación: 

Cuando el cliente envía una solicitud, el balanceador de carga la redirige a uno de los servidores disponibles. 
En este caso se usa round robin que es el algorito más común para manejar cargas de forma equitativa.
Cada servidor tiene a su vez un pool de hilos (en este caso 5) que permite que cada servidor realice un máximo de 5 tareas de forma concurrente. 
Una vez enviados los mensajes del cliente al servidor se implementa como middleware RabbitMQ que es un broker de mensajes de código abierto que permite recibir mensajes, almacenarlos en colas para que la información luego sea almacenada en bases de datos, mediante por ejemplo postgreSQL o sea almacenada como objetos por ejemplo en Amazon S3.


### Autora: Eugenia Lucchelli
