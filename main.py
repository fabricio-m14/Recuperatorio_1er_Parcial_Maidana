from validaciones import ingresar_usuario, categorizar_usuario
from analisis import mostrar_conteo, mostrar_busqueda, mostrar_espejado, reporte_estadistico, es_simetrico, mostrar_ordenamiento


def mostrar_menu() -> None:
    """
    Muestra el menú principal del programa.
    """
    print("╔══════════════════════════════════╗")
    print("║   SISTEMA DE GESTIÓN DE USUARIOS ║")
    print("╚══════════════════════════════════╝")
    print("  1. Ingresar nombre de usuario")
    print("  2. Validar formato del usuario")
    print("  3. Contar tipos de caracteres")
    print("  4. Buscar carácter específico")
    print("  5. Mostrar usuario espejado")
    print("  6. Generar reporte estadístico")
    print("  7. Verificar si el usuario es simétrico")
    print("  8. Ordenar caracteres del usuario")
    print("  0. Salir")


def verificar_usuario_ingresado(usuario: str) -> bool:
    """
    Devuelve True si ya se ingresó un usuario, si no muestra un aviso.
    """
    if len(usuario) == 0:
        print("Primero debés ingresar un nombre de usuario (opción 1).")
        return False
    return True


def main() -> None:
    """
    Función principal. Controla el flujo del programa.
    """
    usuario    = ""
    ejecutando = True

    while ejecutando == True:
        mostrar_menu()
        opcion = input("\nSeleccioná una opción: ")

        if opcion == "1":
            usuario = ingresar_usuario()
            print(f"Usuario '{usuario}' ingresado correctamente.")

        elif opcion == "2":
            if verificar_usuario_ingresado(usuario) == True:
                categoria = categorizar_usuario(usuario)
                print(f"Categoría: {categoria}")

        elif opcion == "3":
            if verificar_usuario_ingresado(usuario) == True:
                mostrar_conteo(usuario)

        elif opcion == "4":
            if verificar_usuario_ingresado(usuario) == True:
                mostrar_busqueda(usuario)

        elif opcion == "5":
            if verificar_usuario_ingresado(usuario) == True:
                mostrar_espejado(usuario)

        elif opcion == "6":
            if verificar_usuario_ingresado(usuario) == True:
                reporte_estadistico(usuario)

        elif opcion == "7":
            if verificar_usuario_ingresado(usuario) == True:
                if es_simetrico(usuario) == True:
                    print(f"'{usuario}' es simétrico.")
                else:
                    print(f"'{usuario}' no es simétrico.")

        elif opcion == "8":
            if verificar_usuario_ingresado(usuario) == True:
                mostrar_ordenamiento(usuario)

        elif opcion == "0":
            print("\n¡Hasta luego!")
            ejecutando = False

        else:
            print("Error: ingresá una opción entre 0 y 8.")


main()