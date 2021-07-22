import random
import string

from palabras import palabras


def obtener_palabra(palabras):
    # Seleccionar una palabra al azar de la lista de palabras validas.
    palabra = random.choice(palabras)

    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra.upper()


def ahorcado():

    print("=======================================")
    print("¡ Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra(palabras)

    letras_por_adivinar = set(palabra)
    letras_adivinadas = set()
    abecedario = set(string.ascii_uppercase) # El modulo string no contiene la letra Ñ

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        
