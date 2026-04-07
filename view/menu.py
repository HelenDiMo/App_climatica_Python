from controller.control_menu import validar_opcion_menu, validar_opcion_zona, ZONAS
from model.register_weather import guardar_registro, buscar_por_zona


def mostrar_menu():
    """
    Muestra el menú principal de la aplicación.
    """
    print("\n===== APP CLIMÁTICA =====")
    print("1. Registrar datos climáticos")
    print("2. Consultar datos por zona")
    print("3. Salir")


def pedir_opcion():
    """
    Solicita una opción del menú principal y la valida.
    """
    while True:
        opcion = input("Selecciona una opción: ").strip()

        if validar_opcion_menu(opcion):
            return opcion

        print("❌ Opción no válida. Inténtalo de nuevo.")


def pedir_fecha():
    """
    Solicita la fecha al usuario.
    De momento solo comprueba que no esté vacía.
    """
    while True:
        fecha = input("Introduce la fecha (dd-mm-yyyy): ").strip()

        if fecha:
            return fecha

        print("❌ La fecha no puede estar vacía.")


def pedir_zona():
    """
    Muestra el menú de zonas y permite seleccionar una opción válida.
    """
    while True:
        print("\nSelecciona una zona:")
        print("1. Centro")
        print("2. Norte")
        print("3. Sur")
        print("4. Este")
        print("5. Oeste")

        opcion = input("Introduce el número de la zona: ").strip()

        if validar_opcion_zona(opcion):
            return ZONAS[opcion]

        print("❌ Opción de zona no válida. Inténtalo de nuevo.")


def pedir_temperatura():
    """
    Solicita la temperatura y comprueba que sea numérica.
    """
    while True:
        try:
            temperatura = float(input("Introduce la temperatura (ºC): ").strip())
            return temperatura
        except ValueError:
            print("❌ Debes introducir un número válido.")


def pedir_humedad():
    """
    Solicita la humedad y comprueba que sea numérica.
    """
    while True:
        try:
            humedad = float(input("Introduce la humedad (%): ").strip())
            return humedad
        except ValueError:
            print("❌ Debes introducir un número válido.")


def pedir_viento():
    """
    Solicita el viento y comprueba que sea numérico.
    """
    while True:
        try:
            viento = float(input("Introduce el viento (km/h): ").strip())
            return viento
        except ValueError:
            print("❌ Debes introducir un número válido.")


def volver_al_inicio():
    """
    Pausa la ejecución hasta que el usuario pulse Enter.
    """
    input("\nPulsa Enter para volver al menú principal...")


def registrar_datos():
    """
    Interfaz de registro de datos climáticos.
    """
    print("\n===== REGISTRO DE DATOS CLIMÁTICOS =====")

    fecha = pedir_fecha()
    zona = pedir_zona()
    temperatura = pedir_temperatura()
    humedad = pedir_humedad()
    viento = pedir_viento()

    print("\n✅ Datos introducidos correctamente:")
    print(f"Fecha: {fecha}")
    print(f"Zona: {zona}")
    print(f"Temperatura: {temperatura} ºC")
    print(f"Humedad: {humedad} %")
    print(f"Viento: {viento} km/h")

    volver_al_inicio()


def consultar_datos():
    """
    Interfaz de consulta por zona.
    """
    print("\n===== CONSULTA DE DATOS POR ZONA =====")

    zona = pedir_zona()

    print(f"\n🔎 Has elegido consultar la zona: {zona}")
    print("Funcionalidad de consulta en construcción.")

    volver_al_inicio()


def ejecutar_menu():
    """
    Bucle principal de la aplicación.
    """
    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == "1":
            registrar_datos()

        elif opcion == "2":
            consultar_datos()

        elif opcion == "3":
            print("\nSaliendo de la aplicación...")
            break
