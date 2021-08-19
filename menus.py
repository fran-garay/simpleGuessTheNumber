import os
from functions import *

def menu(intervalo_numeros, cantidad_intentos):
    print("Elija una opcion")
    print("1) Modificar intervalo de numeros")
    print("2) Modificar cantidad de intentos")
    print("3) Comenzar juego\n")
    print("-------------------------------")
    print(f"Intervalo actual: 0..{intervalo_numeros}")
    print(f"Cantidad de intentos actual: {cantidad_intentos}")
    print("-------------------------------")

    numero_elegido = input()
    if esValido(numero_elegido):
        return int(numero_elegido)
    else: 
        os.system("cls")
        print("Ingrese un numero valido\n")
        return menu()

def modificarIntervalo():
    while True:
        os.system("cls")
        print("Ingrese el intervalo (- si desea volver atras): ", end="")
        intervalo_nuevo = input()
        if intervalo_nuevo == "-":
            return -1
        if esValido(intervalo_nuevo):
            intervalo_nuevo = int(intervalo_nuevo)
            if intervalo_nuevo > 0:
                return intervalo_nuevo
            else:
                return 10
            

def modificarIntentos():
    while True:
        os.system("cls")
        print("Ingrese la cantidad de intentos (- si desea volver atras): ", end="")
        intentos_nuevo = input()
        if intentos_nuevo == "-":
            return -1
        if esValido(intentos_nuevo):
            intentos_nuevo = int(intentos_nuevo)
            if intentos_nuevo > 0:
                return intentos_nuevo
            else:
                return 10