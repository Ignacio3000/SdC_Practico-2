import requests

# URL de la API REST del Banco Mundial 
base_url = "https://api.worldbank.org/v2/country"

def get_gini_info(country, year):
    url = f"{base_url}/{country}/indicator/SI.POV.GINI?date={year}&format=json"
    response = requests.get(url)
    # verificar si la solicitud fue exitosa
    if response.status_code == 200:   # status code 200 para respuestas existosas
        data = response.json()
        # imprimir la respuesta formateada para una mejor visualización
    #    print(json.dumps(data, indent=2, ensure_ascii=False))
        return data
    else:
        print("Error en la solicitud:", response.status_code)

def convert_and_add(gini_float):
    # Convertimos el float a entero y sumamos 1
    gini_int = int(gini_float) + 1
    return gini_int

def convert_and_add_million(gini_float):
    # Convertimos el float a entero y sumamos 1,  un millón de veces
    for _ in range(1000000):
        gini_int = int(gini_float) + 1
    return gini_int

def main():
    gini_info = get_gini_info("ARG","2020"); #tomamos el dato de la api
    gini_float = gini_info[1][0]['value']  #guardamos el dato float
    print( convert_and_add(gini_float))




#Conversion de float a entero +1, con ctypes una sola vez

#resultado = convert_and_add(gini_float) 

#Conversion de float a entero +1, con ctypes un millon de veces
#resultado = convert_and_add_million(gini_float) 

#print(resultado)
