from validaciones import es_letra, es_numero, es_guion_bajo, es_punto


def contar_caracteres(nombre: str) -> tuple:
    """
    Cuenta la cantidad de letras, números, guiones bajos y puntos.
    Retorna una tupla (letras, numeros, guiones, puntos).
    """
    letras   = 0
    numeros  = 0
    guiones  = 0
    puntos   = 0

    for i in range(len(nombre)):
        c = nombre[i]

        if es_letra(c):
            letras = letras + 1
        elif es_numero(c):
            numeros = numeros + 1
        elif es_guion_bajo(c):
            guiones = guiones + 1
        elif es_punto(c):
            puntos = puntos + 1

    return letras, numeros, guiones, puntos


def mostrar_conteo(nombre: str) -> None:
    """Muestra en pantalla el conteo de cada tipo de carácter."""
    letras, numeros, guiones, puntos = contar_caracteres(nombre)

    print(f"Letras: {letras}")
    print(f"Números: {numeros}")
    print(f"Guiones bajos: {guiones}")
    print(f"Puntos: {puntos}")


def ingresar_caracter() -> str:
    """Solicita un carácter al usuario hasta que ingrese exactamente uno."""
    valido = False

    while valido == False:
        c = input("Ingresá el carácter a buscar: ")

        if len(c) == 1:
            valido = True
        else:
            print("Error: ingresá exactamente un carácter.")

    return c


def buscar_caracter(nombre: str, c: str) -> tuple:
    """
    Busca un carácter en el nombre de usuario.
    Retorna una tupla (cantidad, posiciones) donde posiciones es un string con los índices.
    """
    cantidad   = 0
    posiciones = ""

    for i in range(len(nombre)):
        if nombre[i] == c:
            cantidad = cantidad + 1
            if cantidad == 1:
                posiciones = str(i)
            else:
                posiciones = posiciones + ", " + str(i)

    return cantidad, posiciones


def mostrar_busqueda(nombre: str) -> None:
    """Solicita un carácter y muestra cuántas veces aparece y en qué posiciones."""
    c = ingresar_caracter()
    cantidad, posiciones = buscar_caracter(nombre, c)

    if cantidad == 0:
        print(f"El carácter '{c}' no aparece en el nombre.")
    elif cantidad == 1:
        print(f"El carácter '{c}' aparece 1 vez, en la posición {posiciones}.")
    else:
        print(f"El carácter '{c}' aparece {cantidad} veces, en las posiciones {posiciones}.")


def espejado(nombre: str) -> str:
    """
    Devuelve el nombre invertido concatenado con el original.
    Ejemplo: 'fabricio' -> 'fabriciooicirbaf'
    """
    invertido = ""

    for i in range(len(nombre) - 1, -1, -1):
        invertido = invertido + nombre[i]

    return nombre + invertido 


def mostrar_espejado(nombre: str) -> None:
    """
    Muestra el nombre de usuario espejado.
    """
    resultado = espejado(nombre)
    print(f"Usuario espejado: {resultado}")


def contar_repetidos_consecutivos(nombre: str) -> None:
    """
    Muestra los caracteres que se repiten de forma consecutiva y cuántas veces.
    """
    i = 0

    while i < len(nombre) - 1:
        c = nombre[i]
        siguiente = nombre[i + 1]

        if c == siguiente:
            repeticiones = 1

            while i + repeticiones < len(nombre) and nombre[i + repeticiones] == c:
                repeticiones = repeticiones + 1

            print(f"- {repeticiones - 1} repetición de {c}")
            i = i + repeticiones
        else:
            i = i + 1


def reporte_estadistico(nombre: str) -> None:
    """
    Muestra el reporte estadístico completo del nombre de usuario.
    """
    longitud = len(nombre)
    letras, numeros, guiones, puntos = contar_caracteres(nombre)
    simbolos = guiones + puntos

    porcentaje_letras   = float(letras) / float(longitud) * 100
    porcentaje_numeros  = float(numeros) / float(longitud) * 100
    porcentaje_simbolos = float(simbolos) / float(longitud) * 100

    print(f"Longitud total: {longitud}")
    print(f"Porcentaje letras: {porcentaje_letras:.1f}%")
    print(f"Porcentaje números: {porcentaje_numeros:.1f}%")
    print(f"Porcentaje símbolos: {porcentaje_simbolos:.1f}%")
    print("Caracteres repetidos consecutivos:")
    contar_repetidos_consecutivos(nombre)


def es_simetrico(nombre: str) -> bool:
    """
    Determina si el nombre es simétrico.
    La primera mitad debe ser igual a la segunda mitad.
    Solo aplica a nombres de longitud par.
    """
    longitud = len(nombre)

    if longitud % 2 != 0:
        return False

    mitad = longitud // 2
    simetrico = True
    i = 0

    while i < mitad and simetrico == True:
        if nombre[i] != nombre[mitad + i]:
            simetrico = False
        i = i + 1

    return simetrico


def mostrar_simetria(nombre: str) -> None:
    """
    Muestra si el nombre de usuario es simétrico o no.
    """
    if es_simetrico(nombre):
        print(f"'{nombre}' es simétrico.")
    else:
        print(f"'{nombre}' no es simétrico.")


def string_a_lista(nombre: str) -> list:
    """
    Convierte un string en una lista de caracteres.
    """
    lista = []
    for i in range(len(nombre)):
        lista = lista + [nombre[i]]
    return lista


def lista_a_string(lista: list) -> str:
    """
    Convierte una lista de caracteres en un string.
    """
    resultado = ""
    for i in range(len(lista)):
        resultado = resultado + lista[i]
    return resultado


def ordenar_caracteres(nombre: str, ascendente: bool) -> str:
    """
    Ordena los caracteres del nombre usando bubble sort.
    Compara por valor ASCII usando los operadores < y >.
    """
    lista = string_a_lista(nombre)
    longitud = len(lista)

    for i in range(longitud - 1):
        for j in range(longitud - 1 - i):
            if ascendente == True:
                intercambiar = lista[j] > lista[j + 1]
            else:
                intercambiar = lista[j] < lista[j + 1]

            if intercambiar == True:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux

    return lista_a_string(lista)


def ingresar_orden() -> bool:
    """
    Solicita al usuario el orden de ordenamiento hasta que ingrese una opción válida.
    """
    print("  1. Ascendente")
    print("  2. Descendente")
    opcion = input("Seleccioná una opción: ")

    if opcion == "1":
        ascendente = True
    elif opcion == "2":
        ascendente = False
    else:
        print("Error: ingresá 1 o 2.")
        ascendente = ingresar_orden()

    return ascendente


def mostrar_ordenamiento(nombre: str) -> None:
    """Muestra el nombre de usuario con sus caracteres ordenados."""
    ascendente = ingresar_orden()
    resultado  = ordenar_caracteres(nombre, ascendente)

    if ascendente == True:
        print(f"Ordenamiento Ascendente: {resultado}")
    else:
        print(f"Ordenamiento Descendente: {resultado}")