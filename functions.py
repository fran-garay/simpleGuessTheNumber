def esValido(numero_elegido):
    try: 
        numero_elegido = int(numero_elegido)
    except:
        return False

    return numero_elegido >=1 & numero_elegido <= 3

def imprimirAyuda(numero_ingresado, numero_adivinar):
    if(numero_adivinar > numero_ingresado):
        print("El numero es mayor...")
    else:
        print("El numero es menor...")