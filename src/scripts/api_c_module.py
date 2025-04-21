# api_c_module.py
import requests
import float_to_int_c

def get_gini_info(country, year):
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/SI.POV.GINI?date={year}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data[1][0]['value']
    else:
        return None

def convert_and_add(gini_float):
    # Convertimos el float a entero y sumamos 1
    gini_int = float_to_int_c.convert_and_add_one_time(gini_float)
    return gini_int

def convert_and_add_million(gini_float):
    # Convertimos el float a entero y sumamos 1 un millón de veces
    gini_int = float_to_int_c.convert_and_add_one_million(gini_float)
    return gini_int

def main():
    gini_float = get_gini_info("ARG", "2020")  # Tomamos el dato de la API
    resultado = convert_and_add(gini_float)    # Prueba con una sola operación
    print(resultado)

main()
