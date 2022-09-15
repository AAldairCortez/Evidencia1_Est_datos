import datetime
import time
import random

listaCliente = list()
listaSala = list()
listaEvento = list()

class Evento:
    def __init__(self):
        self.nombreEvento=(" ")
        self.turno=(" ")
        self.folio=( )
        self.fechaEvento=(" ")
        self.hora=(" ") 

class Cliente:

    def __init__(self):
        self.nombreCliente=(" ")
        self.claveCliente=( )
    
    #def __str__(self):
        #texto = ("Nombre: {0} - Clave: {1}")
        #return texto.format(self.nombreCliente, self.claveCliente)

class Sala:
    def __init__(self):
        self.nombreSala=(" ")
        self.cupoSala=( )
        self.claveSala=( )


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
            reservaSala()

        elif respuesta_int == 2:
            editarReservacion()

        elif respuesta_int == 3:
            consultar()

        elif respuesta_int == 4:
            registroCliente()

        elif respuesta_int == 5: 
            registroSala()

        elif respuesta_int == 6:
            break
        else: 
            print("\n Su respuesta no corresponde con ninguna de las opciones.")

def reservaSala():
    print("\n Renta de una sala")
    print("*" *30)
    evento=Evento()
    evento.nombreEvento=input("Ingrese el nombre del evento: ")
    evento.turno=input("Ingrese un turno (Matutino, Vespertino, Nocturno): ")
    evento.fechaEvento=input("Ingresa la fecha del evento en formato dd/mm/aaaa: ")
    evento.hora=input("Ingresa la hora deseada de tu evento en formato 12h: ")
    evento.folio=[random.randrange(10000000,99999999) for valor in range(1)]
    print("Clave generada unica: ", evento.folio)
    print("Registro echo")
    listaEvento.append(evento)

def editarReservacion():
    print("\n Edita el nombre de una sala")
    print("*" *30)

def consultar():
    print("\n Consulta de reservaciones")
    print("*" *30)
    fecha=input("Ingresa una fecha para validar si existe un evento en formato dd/mm/aaaa: ")
    for evento in listaEvento:
        if evento.fechaEvento == fecha:
            print("Ya existe un evento ese dia: \n",evento.nombreEvento, "-", evento.fechaEvento, "-", evento.fechaEvento)

    #agregar cambio de str a int en fecha

def registroCliente():
    print("\n Registro de un cliente")
    print("*" *30)
    cliente=Cliente()
    cliente.nombreCliente=input("Introduce el nombre: ")
    cliente.claveCliente=[random.randrange(10000000,99999999) for valor in range(1)]
    print("Clave generada unica: ", cliente.claveCliente)
    print("Registro echo")
    listaCliente.append(cliente)
    print(listaCliente)

def registroSala():
    print("\n Registro de una sala")
    print("*" *30)
    sala=Sala()
    sala.nombreSala=input("Introduce el nombre de la sala: ")
    sala.cupoSala=int(input("Introduce el cupo de la sala: "))
    sala.claveSala=[random.randrange(10000000,99999999) for valor in range(1)]
    print("Clave unica de la sala: ", sala.claveSala)
    print("Registro echo")
    listaSala.append(sala)
    print(listaSala)

menu()




#for cliente in listaCliente:
        #print(cliente.nombreCliente,"=", cliente.claveCliente, "=" )




