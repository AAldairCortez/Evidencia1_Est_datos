import datetime
import time
import random

evento = {}
cliente = {}
sala = {}

def agregar_evento():
    global evento
    print("\n Renta de una sala")
    print("*" *30) 
    folio=int(input("genera tu folio: "))
    nombreEvento=input("Ingrese el nombre del evento: ")
    turno=input("Ingrese un turno (Matutino, Vespertino, Nocturno): ")
    fechaEvento=input("Ingresa la fecha del evento en formato dd/mm/aaaa: ")
    hora=input("Ingresa la hora deseada de tu evento en formato 12h: ")
    print("Clave generada unica: ", folio)
    print("Registro echo")

    evento[folio] = nombreEvento, turno, fechaEvento, hora
    print(evento)

def editarReservacion():
    print("\n Edita el nombre de una sala")
    print("*" *30)

def consultar():
    print("\n Consulta de reservaciones")
    print("*" *30)
    fecha=input("Ingresa una fecha para validar si existe un evento en formato dd/mm/aaaa: ")


def agregar_cliente():
    global cliente
    print("\n Registro de un cliente")
    print("*" *30)
    nombreCliente=input("Introduce el nombre: ")
    claveCliente=int(input("Genera tu clave: "))
    print("Clave generada unica: ", claveCliente)
    print("Registro echo")
    
    cliente[claveCliente] = nombreCliente
    print(cliente)

def registroSala():
    global sala
    print("\n Registro de una sala")
    print("*" *30)
    nombreSala=input("Introduce el nombre de la sala: ")
    cupoSala=int(input("Introduce el cupo de la sala: "))
    claveSala=int(input("Genera la clave tu numero de sala: "))
    print("Clave generada unica: ", claveSala)
    print("Registro echo")

    sala[claveSala] = nombreSala, cupoSala
    print(sala)

def menu():
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
            agregar_evento()

        elif respuesta_int == 2:
            editarReservacion()

        elif respuesta_int == 3:
            consultar()

        elif respuesta_int == 4:
            agregar_cliente()

        elif respuesta_int == 5: 
            registroSala()

        elif respuesta_int == 6:
            break
        else: 
            print("\n Su respuesta no corresponde con ninguna de las opciones.")

menu()









