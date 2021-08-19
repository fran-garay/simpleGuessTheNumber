from random import randint
from functions import *
from menus import *

def main():
    cantidad_intentos = 5
    intervalo_numeros = 10
    
    modo_de_juego = 0
    while modo_de_juego != 3:
        modo_de_juego = menu(intervalo_numeros, cantidad_intentos)
        
        if modo_de_juego == 2:
            resultado_modificar = modificarIntentos()
            if resultado_modificar != -1:
                cantidad_intentos = resultado_modificar
        elif modo_de_juego == 1:
            resultado_modificar = modificarIntervalo()
            if resultado_modificar != -1:
                intervalo_numeros = resultado_modificar

    empezarJuego(intervalo_numeros, cantidad_intentos)
            

def empezarJuego(intervalo_numeros, cantidad_intentos):
    numero_adivinar = int(randint(0,intervalo_numeros))
    no_acerto = True
    intento_actual = 0
    os.system("cls")
    while (intento_actual < cantidad_intentos) & no_acerto:
        intento_actual += 1
        print(f"Ingrese un numero entre 0 y {intervalo_numeros}")
        numero_ingresado = input()
        if not esValido(numero_ingresado):
            continue
        numero_ingresado = int(numero_ingresado)
        if numero_adivinar == numero_ingresado:
            no_acerto = False
        else:
            imprimirAyuda(numero_ingresado, numero_adivinar)

    os.system("cls")
    if no_acerto:
        print("Mas suerte la proxima.")
    else:
        print("Felicitaciones, has acertado!")
        
    print(f"\nEl numero era {numero_adivinar} y vos ingresaste {numero_ingresado}")
            


if __name__ == "__main__":
    main()