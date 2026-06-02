letras  = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"


def es_letra(c: str) -> bool:
    """
    Devuelve True si el carácter es una letra.
    """
    for i in range(len(letras)):
        if c == letras[i]:
            return True
    return False


def es_numero(c: str) -> bool:
    """
    Devuelve True si el carácter es un dígito.
    """
    for i in range(len(numeros)):
        if c == numeros[i]:
            return True
    return False


def es_guion_bajo(c: str) -> bool:
    """
    Devuelve True si el carácter es un guion bajo.
    """
    return c == "_"


def es_punto(c: str) -> bool:
    """
    Devuelve True si el carácter es un punto.
    """
    return c == "."


def tiene_espacio(c: str) -> bool:
    """
    Devuelve True si el carácter es un espacio.
    """
    return c == " "


def ingresar_usuario() -> str:
    """
    Solicita y valida el nombre de usuario hasta que sea correcto.
    """
    nombre = input("Ingresá el nombre de usuario: ")

    if len(nombre) == 0:
        print("Error: el nombre no puede estar vacío.")
        nombre = ingresar_usuario()

    elif len(nombre) < 6 or len(nombre) > 15:
        print("Error: el nombre debe tener entre 6 y 15 caracteres.")
        nombre = ingresar_usuario()

    elif es_numero(nombre[0]):
        print("Error: el nombre no puede comenzar con un número.")
        nombre = ingresar_usuario()

    else:
        tiene_letra = False
        valido = True

        for i in range(len(nombre)):
            c = nombre[i]

            if tiene_espacio(c):
                print("Error: el nombre no puede contener espacios.")
                valido = False
                break

            if not es_letra(c) and not es_numero(c) and not es_guion_bajo(c) and not es_punto(c):
                print(f"Error: el carácter '{c}' no está permitido.")
                valido = False
                break

            if es_letra(c):
                tiene_letra = True

        if not tiene_letra:
            print("Error: el nombre debe contener al menos una letra.")
            valido = False

        if not valido:
            nombre = ingresar_usuario()

    return nombre


def solo_letras(nombre: str) -> bool:
    """
    Devuelve True si el nombre contiene únicamente letras.
    """
    resultado = True
    for i in range(len(nombre)):
        if not es_letra(nombre[i]):
            resultado = False
    return resultado


def tiene_numeros(nombre: str) -> bool:
    """
    Devuelve True si el nombre contiene al menos un número.
    """
    resultado = False
    for i in range(len(nombre)):
        if es_numero(nombre[i]):
            resultado = True
    return resultado


def tiene_simbolos(nombre: str) -> bool:
    """
    Devuelve True si el nombre contiene al menos un símbolo (_ o .).
    """
    resultado = False
    for i in range(len(nombre)):
        if es_guion_bajo(nombre[i]) or es_punto(nombre[i]):
            resultado = True
    return resultado


def termina_en_simbolo(nombre: str) -> bool:
    """
    Devuelve True si el último carácter es un símbolo.
    """
    final = nombre[len(nombre) - 1]
    return es_guion_bajo(final) or es_punto(final)


def categorizar_usuario(nombre: str) -> str: #DEFINE LA CATEGORIA
    """
    Determina la categoría del nombre de usuario.
    Retorna: 'Básico', 'Intermedio', 'Avanzado' o 'Sin categoría'.
    """
    longitud = len(nombre)

    if solo_letras(nombre) and 6 <= longitud <= 8:
        categoria = "Básico"

    elif tiene_numeros(nombre) and not tiene_simbolos(nombre) and longitud >= 8:
        categoria = "Intermedio"

    elif tiene_numeros(nombre) and tiene_simbolos(nombre) and longitud >= 12 and not termina_en_simbolo(nombre):
        categoria = "Avanzado"

    else:
        categoria = "Sin categoría"

    return categoria