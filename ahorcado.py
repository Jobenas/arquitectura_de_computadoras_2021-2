import random

palabras = ["arqui", "conejo", "memoria", "universidad", "desierto",
            "programa", "puntero", "direccion", "esgrima", "bucle"]


def formatea_palabra(lista_palabra):
    palabra_formateada = ""
    # Escriba su codigo despues de esta linea
    for item in lista_palabra:
        palabra_formateada += item + " "
    palabra_formateada = palabra_formateada[:-1]
    # Escriba su codigo antes de esta linea

    return palabra_formateada


def reemplaza_letra_en_pos(lista_palabra, letra, pos):
    # Escriba su codigo despues de esta linea
    lista_palabra[pos] = letra
    # Escriba su codigo antes de esta linea

    return lista_palabra


def busca_letra(lista_palabra, palabra, letra):
    ocurrencias = 0
    # Escriba su codigo despues de esta linea
    for idx in range(len(palabra)):
        if letra == palabra[idx]:
            ocurrencias += 1
            lista_palabra = reemplaza_letra_en_pos(lista_palabra, letra, idx)
    # Escriba su codigo antes de esta linea

    return lista_palabra, ocurrencias


def capturar_letra():
    letra = ""
    # Escriba su codigo despues de esta linea
    while len(letra) != 1:
        letra = input("Por favor ingrese una letra: ")
    # Escriba su codigo antes de esta linea

    return letra.lower()


def init_palabra():
    palabra = random.choice(palabras)
    palabra_a_mostrar = ["_"] * len(palabra)
    vidas = 5
    num_letras = len(palabra)
    letras_incorrectas = []
    letras_correctas = []

    return palabra, palabra_a_mostrar, vidas, num_letras, letras_correctas, letras_incorrectas


def actualiza_estado_en_pantalla(palabra_a_mostrar, letras_incorrectas):
    str_palabra = formatea_palabra(palabra_a_mostrar)
    str_letras = formatea_palabra(letras_incorrectas)

    print(f"{str_palabra} -> # de intentos restantes: {vidas}, letras usadas: {str_letras}")


if __name__ == "__main__":
    # inicializacion de juego
    palabra, palabra_a_mostrar, vidas, num_letras, letras_correctas, letras_incorrectas = init_palabra()

    # mensaje de bienvenida
    print("Bienvenido al juego de Ahorcado, empecemos a jugar")

    actualiza_estado_en_pantalla(palabra_a_mostrar, letras_incorrectas)

    while vidas > 0 and num_letras > 0:
        # Escriba su codigo despues de esta linea
        letra = capturar_letra()

        # Escriba su codigo antes de esta linea

        if letra in letras_correctas:
            continue

        # Escriba su codigo despues de esta linea
        palabra_a_mostrar, ocurrencias = busca_letra(palabra_a_mostrar, palabra, letra)
        if ocurrencias == 0:
            vidas -= 1
            letras_incorrectas.append(letra)
        else:
            letras_correctas.append(letra)
            num_letras -= ocurrencias
        
        actualiza_estado_en_pantalla(palabra_a_mostrar, letras_incorrectas)

        # Escriba su codigo antes de esta linea

    if vidas > 0:
        print("Felicitaciones ha ganado el juego! =)")
    else:
        print("Lo lamento, ha perdido el juego =(")
