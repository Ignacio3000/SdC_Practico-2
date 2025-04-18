import requests
import time
import json


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

start_total_time= time.perf_counter() #tomamos el tiempo al inicio dle programa

gini_info = get_gini_info("ARG","2020"); #tomamos el dato de la api

gini_float = gini_info[1][0]['value']  #guardamos el dato float

start_convertion_time = time.perf_counter() #tomamos el tiempo antes de la conversion

gini_int = int(gini_float) #convertimos el dato a entero

end_time = time.perf_counter() #tomamos el tiempo al final de la conversion

print("Valor entero:", gini_int)
print("Tiempo total de ejecucion:", (end_time - start_total_time ) * 1000 , " mili segundos")
print("Tiempo de conversion:", (end_time - start_convertion_time ) * 1000 , " mili segundos")

