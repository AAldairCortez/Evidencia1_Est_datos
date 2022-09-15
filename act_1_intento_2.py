import datetime
import time
import random

lista_reservaciones = []
lista_clientes = []  
lista_salas = [] 
lista_cupo_salas = [] 

while True:
    print("\n **MENU DE OPERACIONES**")
    print("*****************************")
    print("1 - Registro de una sala")
    print("2 - Editar el nombre del evento de una reservación ya hecha.")
    print("3 - Consultar reservaciones existentes")
    print("4 - Registrar un cliente")
    print("5 - Registrar una sala ")
    print("6 - Salir")
    respuesta = input("Indique la opcion deseada: ")

    try:
        respuesta_int = int(respuesta)
    except ValueError:
        print("**La respuesta no es valida**")
    except Exception:
        print("Se ha presentado una excepcion: ")
        print(Exception)

    if respuesta_int == 1:
        print("hola")

    elif respuesta_int == 4:
        lista_clientes.append(input("Indique el nombre del cliente: "))
        folio_cliente = [random.randrange(10000000,99999999) for valor in range(1)]
        #print("Cliente registrado")
        print(f"Clave del cliente: ", (folio_cliente))

    elif respuesta_int == 5: 
        lista_salas.append(input("Indique el nombre de la sala: "))
        lista_cupo_salas.append(input("Indique el cupo de la sala: "))
        clave_sala = [random.randrange(10000000,99999999) for valor in range(1)]
        print(f"Clave de la sala : ", (clave_sala))
        print(f"Lista de salas: ", (lista_salas))
        print(f"Lista de cupo", (lista_cupo_salas))

    elif respuesta_int == 6:
        break
    else: 
        print("\n Su respuesta no corresponde con ninguna de las opciones.")
        


