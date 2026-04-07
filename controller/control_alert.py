# Pongo float porque la temperatura y el viento pueden tener decimales, y el input devuelve un string, entonces lo convierto a float para poder hacer las comparaciones numéricas.
temperatura = float(input("Introduce la temperatura actual en °C: ")) # Solicitar al operario que ingrese la temperatura actual
viento = float(input("Introduce la velocidad del viento en km/h: ")) # Solicitar al usuario que ingrese la velocidad del viento

print("\n--- ESTADO DEL SISTEMA ---")

# CODIGOS DE COLOR

ROJO = "\033[91m"
VERDE = "\033[92m"
AMARILLO = "\033[93m"
NARANJA_REAL = "\033[38;5;208m"

# Bloques de alertas para cada las temperaturas (alta y  baja) para que sea más claro y organizado
# Si se considera conveniente, se podrían juntar, pero creo que asi está mas claro
# Cada bloque tiene su propia lógica de alertas basada en los umbrales definidos para cada nivel de riesgo. 
# Además, he incluido mensajes específicos para cada nivel de alerta, y códigos de color para resaltar la gravedad de la situación.

# Lógica de Alertas para Altas Temperaturas

if temperatura >= 42:
    print(f"{ROJO} ALERTA ROJA: Riesgo extremo por calor - Riesgo para la salud muy alto.")
elif temperatura >= 39:
    print(f"{NARANJA_REAL}ALERTA NARANJA: Riesgo importante por calor - Se recomienda no salir en horas centrales del día.")
elif temperatura >= 36:
    print(f"{AMARILLO}ALERTA AMARILLA: Riesgo por calor - Se recomienda no realizar actividades al aire libre.")
else:
    print(f"{VERDE}Temperatura: Nivel Verde (Sin riesgo).")

# Lógica de Alertas para Bajas Temperaturas 

if temperatura <= -10:
    print(f"{ROJO}ALERTA ROJA: Frío extremo. Riesgo de heladas y nevadas severas.")
elif temperatura <= -6:
    print(f"{NARANJA_REAL}ALERTA NARANJA: Temperaturas gélidas. Riesgo de heladas y nevadas. Peligro en tuberías y la salud.")
elif temperatura <= -4:
    print(f"{AMARILLO}ALERTA AMARILLA: Precaución por heladas.")
else:
    print(f"{VERDE}Temperatura: Nivel Verde (Sin riesgo).")


# Lógica de Alertas para Viento

if viento >= 110:
    print(f"{ROJO}ALERTA ROJA: Viento extremo - Peligro de caída de objetos y daños estructurales.")
elif viento >= 90:
    print(f"{NARANJA_REAL}ALERTA NARANJA: Cierre preventivo de parques.")
elif viento >= 70:
    print(f"{AMARILLO}ALERTA AMARILLA: Balizas en zonas infantiles y de mayores")
else:
    print(f"{VERDE}Viento: Nivel Verde (Sin riesgo).")

# Errores de entrada