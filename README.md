# PFO 3-Eugenia Lucchelli

## Cómo ejecutar

1. `py crear_db.py` (solo la primera vez)
2. Terminal 1: `py servidor.py`
3. Terminal 2: `py servidor2.py`
4. Terminal 3: `py balanceador.py`
5. Terminal 4: `py cliente.py`

## Diagrama:

<img width="633" height="601" alt="DiagramaPFO3 drawio" src="https://github.com/user-attachments/assets/afb5047f-2dc4-4187-8467-b0c87a6339d5" />



## Explicación: 

Cuando el cliente envía una solicitud, el balanceador de carga la redirige a uno de los servidores disponibles. 
En este caso se usa round robin que es el algorito más común para manejar cargas de forma equitativa.
Cada servidor tiene a su vez un pool de hilos (en este caso 5) que permite que cada servidor realice un máximo de 5 tareas de forma concurrente. 
Una vez enviados los mensajes del cliente al servidor se implementa como middleware RabbitMQ que es un broker de mensajes de código abierto que permite recibir mensajes, almacenarlos en colas para que la información luego sea almacenada en bases de datos, mediante por ejemplo postgreSQL o sea almacenada como objetos por ejemplo en Amazon S3.


### Autora: Eugenia Lucchelli
