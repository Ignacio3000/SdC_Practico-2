import requests
import convert_int_to_float

# URL de la API REST del Banco Mundial 
base_url = "https://api.worldbank.org/v2/country"

def get_gini_info(country, year):
    url = f"{base_url}/{country}/indicator/SI.POV.GINI?date={year}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 1 and data[1]:
            return data[1][0]['value']
        else:
            print("No hay datos disponibles para ese país/año.")
            return None
    else:
        print("Error en la solicitud:", response.status_code)
        return None

# Pedir datos al usuario
pais = input("Ingrese el código del país (por ejemplo, ARG para Argentina): ").strip().upper()
anio = input("Ingrese el año (por ejemplo, 2010): ").strip()

# Llamar a la función
gini_value = get_gini_info(pais, anio)

# Mostrar resultado
if gini_value is not None:
    ##print(f"Índice GINI para {pais} en {anio}: {gini_value}")
    ##print("Convertido con convertToFloat:", convert_int_to_float.convertToFloat(gini_value))
    ##print("Convertido con convertToFloatAsm:", convert_int_to_float.convertToFloatAsm(gini_value))

## Suponiendo que gini_value es un float, por ejemplo 41.8
    gini_rounded = round(gini_value)  ## redondea: 41.8 → 42, 41.2 → 41

    print("GINI (original):", gini_value)
    print("GINI (redondeado):", gini_rounded)

    print("Convertido con convertToFloat:", convert_int_to_float.convertToFloat(gini_rounded))
    print("Convertido con convertToFloatAsm:", convert_int_to_float.convertToFloatAsm(gini_rounded))
