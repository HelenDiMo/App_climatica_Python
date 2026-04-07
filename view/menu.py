from controller.control_menu import validar_opcion_menu


def mostrar_menu():
    """
    Muestra por pantalla el menú principal de la aplicación.
    No contiene lógica, solo presentación.
    """
    print("\n===== APP CLIMÁTICA =====")
    print("1. Registrar datos climáticos")
    print("2. Consultar datos por zona")
    print("3. Salir")


def pedir_opcion():
    """
    Solicita una opción al usuario y la valida.

    - Si la opción es válida → se devuelve
    - Si no es válida → se vuelve a pedir

    Este bucle evita que el programa se rompa por entradas incorrectas.
    """
    while True:
        opcion = input("Selecciona una opción: ").strip()

        # Validamos la opción usando el controller
        if validar_opcion_menu(opcion):
            return opcion

        # Mensaje de error si la opción no es válida
        print("❌ Opción no válida. Inténtalo de nuevo.")


def registrar_datos():
    """
    Punto de entrada para el registro de datos climáticos.

    Aquí se conectará posteriormente con:
    - módulo de persistencia (JSON)
    - validaciones de datos (temperatura, humedad, etc.)
    """
    print("\n[Registro de datos]")
    print("Funcionalidad en construcción...\n")


def consultar_datos():
    """
    Punto de entrada para la consulta de datos por zona.

    Aquí se conectará posteriormente con:
    - lectura de datos históricos
    - filtros por zona
    """
    print("\n[Consulta por zona]")
    print("Funcionalidad en construcción...\n")


def ejecutar_menu():
    """
    Controlador principal del flujo de la aplicación.

    - Muestra el menú
    - Pide una opción
    - Ejecuta la acción correspondiente
    - Repite hasta que el usuario decide salir

    Este bucle mantiene la aplicación en ejecución continua.
    """
    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        # Selección de acción según la opción elegida
        if opcion == "1":
            registrar_datos()

        elif opcion == "2":
            consultar_datos()

        elif opcion == "3":
            print("Saliendo de la aplicación...")
            break  # rompe el bucle y termina el programa+++